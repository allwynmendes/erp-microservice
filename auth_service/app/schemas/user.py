# erp-microservice/auth_service/app/schemas/user.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

# Shared properties for all user models
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to receive via API on update
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

# Properties to return via API
class UserInDB(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Public user model (what we return from API)
class User(UserInDB):
    pass

# User authentication schema
class UserLogin(BaseModel):
    username: str
    password: str