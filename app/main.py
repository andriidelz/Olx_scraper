import time
import psycopg2
import os

from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

from .scraping import scrape_olx
from .scheduler import schedule_scraping

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/olx_db")

app = FastAPI()

def create_db_connection():
    retries = 5
    for i in range(retries):
        try:
            engine = create_engine(DATABASE_URL)
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            db = SessionLocal()
            db.execute(text("SELECT 1"))
            return db
        except psycopg2.OperationalError as e:
            print(f"Connection failed. Retrying ({i + 1}/{retries})...")
            time.sleep(5)
    raise Exception("Unable to connect to the database after several retries.")

@app.on_event("startup")
async def on_startup():
    create_db_connection()
    # schedule_scraping()
    print("Connected to the database successfully!")

@app.get("/")
def read_root():
    return {"message": "OLX Scraper is running!"}
