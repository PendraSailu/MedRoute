from app.database import SessionLocal
from app.models import Hospital

def get_emergency_hospitals():
    db = SessionLocal()
    hospitals = db.query(Hospital).filter(
        Hospital.emergency_available == 1
    ).all()
    db.close()
    return hospitals
