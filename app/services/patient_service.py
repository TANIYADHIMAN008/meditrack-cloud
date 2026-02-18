from sqlalchemy.orm import Session
from app import models, schemas


def create_patient(db: Session, patient: schemas.PatientCreate, doctor_id):
    new_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        condition=patient.condition,
        doctor_id=doctor_id
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


def get_doctor_patients(db: Session, doctor_id):
    return db.query(models.Patient).filter(
        models.Patient.doctor_id == doctor_id
    ).all()
