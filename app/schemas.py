from pydantic import BaseModel, EmailStr
from typing import Optional


# ===========================
# USER SCHEMAS
# ===========================

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str


class UserResponse(BaseModel):
    id: int   # 🔥 FIXED (was UUID)
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


# ===========================
# PATIENT SCHEMAS
# ===========================

class PatientCreate(BaseModel):
    name: str
    age: int
    condition: str


class PatientResponse(BaseModel):
    id: int   # 🔥 FIXED (was UUID)
    name: str
    age: int
    condition: str
    doctor_id: Optional[int]   # 🔥 FIXED (was UUID)

    class Config:
        from_attributes = True