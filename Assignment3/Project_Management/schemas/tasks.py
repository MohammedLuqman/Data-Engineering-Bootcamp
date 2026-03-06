from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    description: str

class TaskCreate(TaskBase):
    project_id: int
    assigned_to: int

class TaskUpdate(BaseModel):
    description: Optional[str] = None

class TaskRead(TaskBase):
    id: int
    project_id: int
    assigned_to: int

    class Config:
        from_attributes = True