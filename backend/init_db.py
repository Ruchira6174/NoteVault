from app.core.database import Base, engine

# Import every model so SQLAlchemy registers them
from app.models.user import User
from app.models.resource import Resource
from app.models.wallet import Wallet
from app.models.purchase import Purchase
from app.models.review import Review
from app.models.permission import PermissionRequest


def init():
    Base.metadata.create_all(bind=engine)
    print("Database created successfully!")


if __name__ == "__main__":
    init()