from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from ..auth import require_role

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

# ===============================
# CREATE PATIENT (Doctor Only)
# ===============================

@router.post("/", response_model=schemas.PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("doctor"))
):
    new_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        condition=patient.condition,
        doctor_id=current_user.id
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# ===============================
# GET MY PATIENTS (Doctor Only)
# ===============================

@router.get("/", response_model=list[schemas.PatientResponse])
def get_my_patients(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("doctor"))
):
    patients = db.query(models.Patient).filter(
        models.Patient.doctor_id == current_user.id
    ).all()

    return patients


# ===============================
# UPDATE PATIENT (Doctor Only)
# ===============================

@router.put("/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(
    patient_id: int,
    updated_data: schemas.PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("doctor"))
):

    patient = db.query(models.Patient).filter(
        models.Patient.id == patient_id,
        models.Patient.doctor_id == current_user.id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    patient.name = updated_data.name
    patient.age = updated_data.age
    patient.condition = updated_data.condition

    db.commit()
    db.refresh(patient)

    return patient


# ===============================
# DELETE PATIENT (Doctor Only)
# ===============================

@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("doctor"))
):

    patient = db.query(models.Patient).filter(
        models.Patient.id == patient_id,
        models.Patient.doctor_id == current_user.id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return


# ===============================
# ADMIN: GET ALL PATIENTS
# ===============================

@router.get("/all")
def get_all_patients(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):
    return db.query(models.Patient).all()