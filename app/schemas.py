from pydantic import BaseModel, EmailStr
from uuid import UUID


# ---------------------------
# User Schemas
# ---------------------------

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str



class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


# ---------------------------
# Patient Schemas
# ---------------------------

class PatientCreate(BaseModel):
    name: str
    age: str
    condition: str


class PatientResponse(BaseModel):
    id: UUID
    name: str
    age: str
    condition: str

    class Config:
        from_attributes = True

