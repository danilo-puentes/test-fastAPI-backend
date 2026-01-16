from abc import ABC, abstractmethod
from typing import Iterable, Optional

from src.domain.entities.task import Task


class TaskRepository(ABC):
    @abstractmethod
    def list(self) -> Iterable[Task]:
        raise NotImplementedError

    @abstractmethod
    def get(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def create(self, title: str, description: str | None) -> Task:
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        task_id: int,
        title: str | None,
        description: str | None,
        completed: bool | None,
    ) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        raise NotImplementedError
