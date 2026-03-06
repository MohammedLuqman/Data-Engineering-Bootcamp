from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr
    @field_validator("email")
    def check_gmail(cls, v):
        if not v.endswith("@gmail.com"):
            raise ValueError("Only Gmail addresses allowed")
        return v

class UserCreate(UserBase):
    pass
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True