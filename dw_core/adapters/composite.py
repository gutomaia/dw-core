from __future__ import annotations

import time
from abc import ABCMeta, abstractmethod

from dw_core.adapters.task import Task
from dw_core.ports.tasks import (
    BackgroundTask,
    TaskProgressCallback,
    TaskProgressListenerInterface,
)


class TaskRunner(metaclass=ABCMeta):
    """The one seam between task structure and task execution.

    Today an in-process runner; tomorrow a pool; someday a queue
    feeding lambda workers. The composite's arithmetic never
    learns which.
    """

    @abstractmethod
    def submit(self, task: BackgroundTask) -> None:
        raise NotImplementedError()


class InThreadRunner(TaskRunner):
    """Runs the task right here, right now — the reference runner
    and the natural fit for single-flow hosts."""

    def submit(self, task: BackgroundTask) -> None:
        task.run()


class _ChildRun(Task):
    """A child wrapped for submission: reports its completion or
    failure back to the parent, whatever runner carried it."""

    def __init__(self, child, on_progress, on_done, on_failed):
        super().__init__()
        self.child = child
        self._on_done = on_done
        self._on_failed = on_failed
        if isinstance(child, TaskProgressListenerInterface):
            child.add_progress_callback(
                _Relay(on_progress)
            )

    def run(self):
        try:
            self.child.run()
        except Exception as failure:
            self._on_failed(self.child, failure)
            return
        self._on_done(self.child)


class _Relay(TaskProgressCallback):
    def __init__(self, receive):
        self._receive = receive

    def set_progress(self, percentage: float) -> None:
        self._receive(percentage)


class CompositeTask(Task):
    """A task broken into tasks.

    Progress is the weighted rollup of the children; ETA divides
    the remaining weight by MEASURED throughput, so the effective
    parallelism of whatever runs the children is observed, never
    assumed. The finalizer runs only when the last child is done;
    a failed child fails the whole and names itself.
    """

    def __init__(
        self,
        *,
        children,
        finalizer=None,
        clock=time.monotonic,
    ) -> None:
        super().__init__()
        self._children = list(children)
        self._finalizer = finalizer
        self._clock = clock
        self._total = sum(weight for _, weight in self._children)
        self._fractions = {
            id(child): 0.0 for child, _ in self._children
        }
        self._weights = {
            id(child): weight for child, weight in self._children
        }
        self._done_weight = 0.0
        self._failure: Exception | None = None

    def run(self, runner: TaskRunner) -> None:
        self._started = self._clock()
        for child, _ in self._children:
            runner.submit(_ChildRun(
                child,
                on_progress=self._child_progress(child),
                on_done=self._child_done,
                on_failed=self._child_failed,
            ))
        if self._failure is not None:
            raise self._failure

    def _child_progress(self, child):
        def receive(percentage):
            self._fractions[id(child)] = percentage / 100.0
            self._report()
        return receive

    def _child_done(self, child):
        self._fractions[id(child)] = 1.0
        self._done_weight += self._weights[id(child)]
        self._report()
        if self._done_weight >= self._total:
            if self._finalizer is not None:
                self._finalizer()

    def _child_failed(self, child, failure):
        label = getattr(child, 'label', None) or repr(child)
        self._failure = RuntimeError(
            f'child {label} failed: {failure}'
        )

    def _report(self):
        if not self._total:
            return
        weighted = sum(
            self._fractions[id(child)] * weight
            for child, weight in self._children
        )
        self.set_progress(100.0 * weighted / self._total)
        elapsed = self._clock() - self._started
        if self._done_weight > 0 and elapsed > 0:
            rate = self._done_weight / elapsed
            remaining = self._total - self._done_weight
            self.set_eta(remaining / rate)
