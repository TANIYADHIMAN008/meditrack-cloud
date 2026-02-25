from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

    # Relationship with Patient
    patients = relationship(
        "Patient",
        back_populates="doctor",
        cascade="all, delete"
    )


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    condition = Column(String(255))

    doctor_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    doctor = relationship("User", back_populates="patients")