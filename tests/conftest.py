import os
import sys
from pathlib import Path
import pytest

# Make backend importable
BACKEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "backend")
)

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# IMPORTANT:
# Set the test database BEFORE importing the application/database.
env_path = Path(__file__).parent / ".env.test"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.startswith("DATABASE_URL="):
                val = line.strip().split("=", 1)[1]
                if val.endswith("/notevault"):
                    val = val.replace("/notevault", "/notevault_test")
                os.environ["DATABASE_URL"] = val

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base, get_db
from app.main import app

# Import models so SQLAlchemy registers their tables.
from app.models.user import User
from app.models.resource import Resource
from app.models.resource_file import ResourceFile

TEST_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(
    TEST_DATABASE_URL,
    pool_pre_ping=True,
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client