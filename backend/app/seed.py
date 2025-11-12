from app.db import SessionLocal, engine
from app.models import Base, Device, Measurement
from random import random

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Device).count() == 0:
            d1 = Device(name="Inversor-01", location="Usina A")
            d2 = Device(name="Medidor-42", location="Usina B")
            db.add_all([d1, d2])
            db.commit()
        devices = db.query(Device).all()
        for d in devices:
            for _ in range(10):
                db.add(Measurement(device_id=d.id, value=round(100*random(), 2)))
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed()