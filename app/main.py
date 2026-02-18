from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import users,patients

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(patients.router)

@app.get("/")
def root():
    return {"message": "MediTrack API is running 🚀"}
