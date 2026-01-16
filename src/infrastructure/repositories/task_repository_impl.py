from datetime import datetime
from typing import Iterable, Optional

from sqlalchemy import Boolean, Column, DateTime, Integer, String, select
from sqlalchemy.orm import Session

from src.domain.entities.task import Task
from src.domain.repositories.task_repository import TaskRepository
from src.infrastructure.db.database import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


def _to_entity(model: TaskModel) -> Task:
    return Task(
        id=model.id,
        title=model.title,
        description=model.description,
        completed=model.completed,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class TaskRepositoryImpl(TaskRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> Iterable[Task]:
        stmt = select(TaskModel)
        results = self.session.execute(stmt).scalars().all()
        return [_to_entity(row) for row in results]

    def get(self, task_id: int) -> Optional[Task]:
        task = self.session.get(TaskModel, task_id)
        return _to_entity(task) if task else None

    def create(self, title: str, description: str | None) -> Task:
        model = TaskModel(title=title, description=description, completed=False)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return _to_entity(model)

    def update(
        self,
        task_id: int,
        title: str | None,
        description: str | None,
        completed: bool | None,
    ) -> Optional[Task]:
        model = self.session.get(TaskModel, task_id)
        if not model:
            return None

        if title is not None:
            model.title = title
        if description is not None:
            model.description = description
        if completed is not None:
            model.completed = completed

        model.updated_at = datetime.now(datetime.timezone.utc)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return _to_entity(model)

    def delete(self, task_id: int) -> bool:
        model = self.session.get(TaskModel, task_id)
        if not model:
            return False
        self.session.delete(model)
        self.session.commit()
        return True
