import datetime
from collections import deque
from typing import Callable, Iterator, Generator

from src.tasks_models import Task


class TaskQueue:
    """
    Очередь задач с поддержкой итерации, фильтрации и управления
    """

    def __init__(self):
        self._tasks_queue = deque()
        self._iter_index = 0
        self._archive = []

    def add_task(self, task: Task):
        self._tasks_queue.append(task)

    def __len__(self) -> int:
        return len(self._tasks_queue)

    def __getitem__(self, index: int):
        return self._tasks_queue[index]

    def __iter__(self) -> Iterator[Task]:
        self._iter_index = 0
        return self

    def __next__(self) -> Task:
        if self._iter_index >= len(self._tasks_queue):
            raise StopIteration
        task = self._tasks_queue[self._iter_index]
        self._iter_index += 1
        return task

    def filter(self, condition: Callable[[Task], bool]):
        for task in self._tasks_queue:
            if condition(task):
                yield task

    def filter_by_status(self, status: str) -> Generator[Task]:
        return self.filter(lambda task: task.status == status)

    def filter_by_priority(self, priority: int) -> Generator[Task]:
        return self.filter(lambda task: task.priority == priority)

    def filter_by_deadline(self) -> Generator[Task]:
        return self.filter(lambda task: task.deadline <= datetime.datetime.now())

    def find_by_id(self, task_id: int) -> Task | None:
        for task in self._tasks_queue:
            if task.task_id == task_id:
                return task
        return None

    def pop_left(self):
        if self._tasks_queue:
            return self._tasks_queue.popleft()
        return None
