
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


app = FastAPI()


DATABASE_URL = "postgresql+psycopg2://postgres:your_new_password@localhost/fastapi"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()