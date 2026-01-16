from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from src.application.use_cases.task_service import TaskService
from src.infrastructure.db.database import SessionLocal, engine, Base
from src.infrastructure.repositories.task_repository_impl import TaskRepositoryImpl


# Ensure tables exist at import time so the app starts ready.
Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repository = TaskRepositoryImpl(db)
    return TaskService(repository)
