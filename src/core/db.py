from src.core.config import settings
from src.utils.logger import setup_logger
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


logger = setup_logger(__name__)


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Only needed for SQLite.
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()