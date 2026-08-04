from __future__ import annotations


class CompositeTaskSpec:
    """A task broken into tasks.

    Each child is a BackgroundTask with its own progress and ETA;
    the parent holds the STRUCTURE and the ARITHMETIC:

    - progress is the weighted rollup of the children's progress
      (weights come from the work itself — chunk durations);
    - ETA divides remaining weight by MEASURED throughput, so the
      effective parallelism of whatever runs the children is
      observed, never assumed — the abstraction knows no provider;
    - execution goes through ONE port, TaskRunner.submit(task):
      today an in-process runner, tomorrow a pool, someday a queue
      of lambda workers — the arithmetic never changes;
    - the finalizer (the stitch) runs only after every child is
      done; a failed child fails the parent and names itself.
    """

    def given_children(self, weighted):
        """weighted: list of (label, weight, behavior) where
        behavior is 'done' or 'fail'."""
        raise NotImplementedError()

    def given_the_clock_advances(self, seconds_per_child: float):
        """Each child's completion advances the fake clock."""
        raise NotImplementedError()

    def when_run(self):
        raise NotImplementedError()

    def submitted_labels(self):
        raise NotImplementedError()

    def reported_progress(self):
        """Every parent progress value reported, in order."""
        raise NotImplementedError()

    def reported_etas(self):
        raise NotImplementedError()

    def finalized(self) -> bool:
        raise NotImplementedError()

    def failure(self) -> str | None:
        raise NotImplementedError()

    def test_every_child_goes_through_the_runner(self):
        self.given_children([('a', 1, 'done'), ('b', 1, 'done'),
                             ('c', 1, 'done')])

        self.when_run()

        assert self.submitted_labels() == ['a', 'b', 'c']

    def test_progress_is_the_weighted_rollup(self):
        """Three seconds of video done out of four is 75 percent,
        no matter how many chunks carried them."""
        self.given_children([('long', 3, 'done'),
                             ('short', 1, 'done')])

        self.when_run()

        assert self.reported_progress()[0] == 75.0
        assert self.reported_progress()[-1] == 100.0

    def test_eta_divides_remaining_weight_by_measured_rate(self):
        """Four equal children, each taking 5s of wall clock: after
        the first completes the measured rate is one weight per 5s,
        so three remain -> 15s. The runner's parallelism is inside
        the measurement, never a parameter."""
        self.given_children([('a', 1, 'done'), ('b', 1, 'done'),
                             ('c', 1, 'done'), ('d', 1, 'done')])
        self.given_the_clock_advances(5.0)

        self.when_run()

        assert self.reported_etas()[0] == 15.0
        assert self.reported_etas()[-1] == 0.0

    def test_the_finalizer_waits_for_the_last_child(self):
        self.given_children([('a', 1, 'done'), ('b', 1, 'done')])

        self.when_run()

        assert self.finalized() is True

    def test_a_failed_child_fails_the_parent_and_names_itself(self):
        self.given_children([('good', 1, 'done'),
                             ('bad', 1, 'fail')])

        self.when_run()

        assert self.finalized() is False
        assert 'bad' in (self.failure() or '')

    def test_children_with_their_own_progress_roll_up_live(self):
        """A child that reports 50 percent contributes half its
        weight before it finishes."""
        self.given_children([('halfway', 1, 'halfway-then-done'),
                             ('other', 1, 'done')])

        self.when_run()

        assert 25.0 in self.reported_progress()
