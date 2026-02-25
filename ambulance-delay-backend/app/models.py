from sqlalchemy import Column, Integer, Float, String, DateTime
from app.database import Base
from sqlalchemy.sql import func

class Hospital(Base):
    __tablename__ = "hospitals"

    hospital_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    emergency_available = Column(Integer, nullable=False)
    
class EmergencyRequest(Base):
    __tablename__ = "emergency_requests"

    id = Column(Integer, primary_key=True, index=True)

    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    hour = Column(Integer, nullable=False)
    is_weekend = Column(Integer, nullable=False)

    hospital_name = Column(String, nullable=False)
    distance_km = Column(Float, nullable=False)
    predicted_delay = Column(Float, nullable=False)
    eta_minutes = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())