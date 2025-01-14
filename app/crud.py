from sqlalchemy.orm import Session
from .models import Listing

def create_listing(db: Session, title: str, description: str, views: int, service_type: str, url: str):
    db_listing = Listing(title=title, description=description, views=views, service_type=service_type, url=url)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing

def get_listings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Listing).offset(skip).limit(limit).all()
