from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session



SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:sanjarsql@localhost:5432/Bilmdon_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
