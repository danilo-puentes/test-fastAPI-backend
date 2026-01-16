from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.use_cases.task_service import TaskService
from src.interfaces.api.schemas import TaskCreate, TaskResponse, TaskUpdate
from src.interfaces.container import get_task_service

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/", response_model=List[TaskResponse])
def list_tasks(service: TaskService = Depends(get_task_service)):
    tasks = service.list_tasks()
    return [TaskResponse.model_validate(task) for task in tasks]


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, service: TaskService = Depends(get_task_service)):
    task = service.create_task(title=payload.title, description=payload.description)
    return TaskResponse.model_validate(task)


@router.get("/{task_id}/", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return TaskResponse.model_validate(task)


@router.put("/{task_id}/", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdate, service: TaskService = Depends(get_task_service)):
    task = service.update_task(
        task_id=task_id,
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
    )
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return TaskResponse.model_validate(task)


@router.delete("/{task_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    deleted = service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return None
