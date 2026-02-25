import pandas as pd
from app.database import SessionLocal
from app.models import Hospital

# Load CSV
df = pd.read_csv("data/hospitals_clean.csv", sep="\t")

# Normalize columns
df.columns = df.columns.str.strip().str.lower()

# Filter emergency hospitals
df = df[df["emergency_available"] == 1]

db = SessionLocal()

for _, row in df.iterrows():
    hospital = Hospital(
        hospital_id=row["hospital_id"],
        name=row["name"],
        lat=row["lat"],
        lon=row["lon"],
        emergency_available=row["emergency_available"]
    )
    db.add(hospital)

db.commit()
db.close()

print("Hospitals inserted successfully!")