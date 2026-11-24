from app.core.database import Base, engine
from app.models import (
    User,
    Patient,
    Appointment,
    BiomarkerReport,
    XrayPrediction,
    CombinedPrediction,
    DoctorNote
)

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("DATABASE TABLES CREATED SUCCESSFULLY!")

if __name__ == "__main__":
    create_tables()