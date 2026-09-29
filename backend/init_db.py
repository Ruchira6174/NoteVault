from app.core.database import Base, engine

# Import ALL SQLAlchemy models so they get registered
from app.models.user import User
from app.models.resource import Resource
from app.models.resource_file import ResourceFile

from app.models.wallet import Wallet
from app.models.purchase import Purchase
from app.models.review import Review
from app.models.permission import PermissionRequest


def init():
    Base.metadata.create_all(bind=engine)
    print("Database created successfully!")


if __name__ == "__main__":
    init()