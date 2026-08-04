from unittest import TestCase

from dw_core.adapters import Task
from dw_core.adapters.composite import CompositeTask, InThreadRunner
from dw_core.ports import TaskETACallback, TaskProgressCallback
from dw_core.tests.composite_task_spec import CompositeTaskSpec


import threading

_MEETING = threading.Barrier(2, timeout=5.0)


class _Child(Task):
    def __init__(self, label, behavior, clock):
        super().__init__()
        self.label = label
        self.behavior = behavior
        self._clock = clock

    def run(self):
        if self.behavior == 'rendezvous':
            _MEETING.wait()
        if self.behavior == 'halfway-then-done':
            self.set_progress(50.0)
        self._clock.tick()
        if self.behavior == 'fail':
            raise RuntimeError(f'{self.label} broke')
        self.set_progress(100.0)


class _Clock:
    def __init__(self):
        self.now = 0.0
        self.step = 0.0

    def tick(self):
        self.now += self.step

    def __call__(self):
        return self.now


class _RecordingRunner(InThreadRunner):
    def __init__(self):
        self.labels = []

    def submit(self, task):
        wrapped = getattr(task, 'child', None)
        if wrapped is not None:
            self.labels.append(wrapped.label)
        super().submit(task)


class _Recorder(TaskProgressCallback, TaskETACallback):
    def __init__(self):
        self.progress = []
        self.etas = []

    def set_progress(self, percentage):
        self.progress.append(percentage)

    def set_eta(self, seconds):
        self.etas.append(seconds)


class CompositeTaskTest(CompositeTaskSpec, TestCase):
    def setUp(self):
        self.clock = _Clock()
        self.runner = _RecordingRunner()
        self.recorder = _Recorder()
        self.finalizer_ran = False
        self.error = None

    def given_children(self, weighted):
        self.children = [
            (_Child(label, behavior, self.clock), weight)
            for label, weight, behavior in weighted
        ]

    def given_the_clock_advances(self, seconds_per_child):
        self.clock.step = seconds_per_child

    def when_run(self):
        def finalize():
            self.finalizer_ran = True

        composite = CompositeTask(
            children=self.children,
            finalizer=finalize,
            clock=self.clock,
        )
        composite.add_progress_callback(self.recorder)
        composite.add_eta_callback(self.recorder)
        try:
            composite.run(self.runner)
        except RuntimeError as failure:
            self.error = str(failure)

    def submitted_labels(self):
        return self.runner.labels

    def reported_progress(self):
        return self.recorder.progress

    def reported_etas(self):
        return self.recorder.etas

    def finalized(self):
        return self.finalizer_ran

    def failure(self):
        return self.error

    def when_run_pooled(self, workers):
        from dw_core.adapters.composite import PoolRunner

        def finalize():
            self.finalizer_ran = True

        composite = CompositeTask(
            children=self.children,
            finalizer=finalize,
            clock=self.clock,
        )
        composite.add_progress_callback(self.recorder)
        composite.add_eta_callback(self.recorder)
        runner = PoolRunner(workers=workers)
        composite.run(runner)
        runner.wait()
