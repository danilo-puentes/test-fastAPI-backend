from typing import Iterable, Optional

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def list_tasks(self) -> Iterable[Task]:
        return self.repository.list()

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.repository.get(task_id)

    def create_task(self, title: str, description: str | None) -> Task:
        return self.repository.create(title=title, description=description)

    def update_task(
        self,
        task_id: int,
        title: str | None,
        description: str | None,
        completed: bool | None,
    ) -> Optional[Task]:
        return self.repository.update(
            task_id=task_id,
            title=title,
            description=description,
            completed=completed,
        )

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)
