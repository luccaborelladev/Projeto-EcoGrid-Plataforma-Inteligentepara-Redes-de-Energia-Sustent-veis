from fastapi import FastAPI
import os
import psycopg2

app = FastAPI(title="EcoGrid API", version="0.1.0")

def db_health():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "ecogrid"),
            user=os.getenv("POSTGRES_USER", "ecouser"),
            password=os.getenv("POSTGRES_PASSWORD", "ecopass"),
            host=os.getenv("POSTGRES_HOST", "db"),
            port=int(os.getenv("POSTGRES_PORT", "5432")),
            connect_timeout=2
        )
        conn.close()
        return True
    except Exception:
        return False

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": app.version,
        "db": "up" if db_health() else "down"
    }