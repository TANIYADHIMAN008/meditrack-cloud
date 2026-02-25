from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
import time

from .database import engine
from . import models
from .routes import users, patients

app = FastAPI(
    title="MediTrack Cloud API",
    version="1.0.0"
)

# ----------------------------
# WAIT FOR DATABASE ON STARTUP
# ----------------------------
@app.on_event("startup")
def wait_for_db():
    while True:
        try:
            models.Base.metadata.create_all(bind=engine)
            print("✅ Database connected!")
            break
        except OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(2)

# ----------------------------
# CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# ROUTERS
# ----------------------------
app.include_router(users.router)
app.include_router(patients.router)

@app.get("/")
def root():
    return {"message": "MediTrack API Running 🚀"}