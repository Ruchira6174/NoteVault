from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from app.core.config import get_settings

settings = get_settings()

# SQLAlchemy 2.0 style engine with connection pooling
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Enable connection health checks
    pool_size=10,        # Number of connections to keep open
    max_overflow=20      # Max additional connections to create
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """
    Database dependency for FastAPI routes.
    Yields a database session and ensures it is closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
