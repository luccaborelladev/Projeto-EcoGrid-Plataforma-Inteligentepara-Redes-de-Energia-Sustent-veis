import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_NAME = os.getenv("POSTGRES_DB", "ecogrid")
DB_USER = os.getenv("POSTGRES_USER", "ecouser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "ecopass")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)