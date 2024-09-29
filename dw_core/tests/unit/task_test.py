from unittest import TestCase

from dw_core.adapters import Task
from dw_core.ports import TaskETACallback, TaskProgressCallback


class TaskTest(TestCase):
    def test_task_add_progress_callback(self):
        class MyTask(Task):
            def run(self):
                self.set_progress(40)

        class Progress(TaskProgressCallback):
            def __init__(self):
                self.percentage = 0

            def set_progress(self, percentage: float) -> None:
                self.percentage = percentage

        progress = Progress()
        self.assertEqual(progress.percentage, 0)

        task = MyTask()
        task.add_progress_callback(progress)
        task.run()

        self.assertEqual(progress.percentage, 40)

    def test_task_add_eta_callback(self):
        class MyTask(Task):
            def run(self):
                self.set_eta(25)

        class ETA(TaskETACallback):
            def __init__(self):
                self.seconds = None

            def set_eta(self, seconds: float) -> None:
                self.seconds = seconds

        eta = ETA()

        task = MyTask()
        task.add_eta_callback(eta)
        task.run()

        self.assertEqual(eta.seconds, 25)

    def test_task_continuos_progress(self):
        class YieldTask(Task):
            def run(self):
                for i in range(10):
                    progress = i * 10
                    self.set_progress(progress)
                    yield progress

        task = YieldTask()

        class Progress(TaskProgressCallback):
            def __init__(self):
                self.percentage = 0

            def set_progress(self, percentage: float) -> None:
                self.percentage = percentage

        progress = Progress()
        task.add_progress_callback(progress)

        for actual in task.run():
            self.assertEqual(progress.percentage, actual)

    def test_task_continuos_eta(self):
        class YieldTask(Task):
            def run(self):
                for i in range(10):
                    eta = i * 5
                    self.set_eta(eta)
                    yield eta

        task = YieldTask()

        class ETA(TaskETACallback):
            def __init__(self):
                self.seconds = None

            def set_eta(self, seconds: float) -> None:
                self.seconds = seconds

        eta = ETA()
        task.add_eta_callback(eta)

        for actual in task.run():
            self.assertEqual(eta.seconds, actual)
