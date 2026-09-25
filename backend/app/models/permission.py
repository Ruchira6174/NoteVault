from sqlalchemy import Column, Integer, String
from app.core.database import Base

class PermissionRequest(Base):
    __tablename__ = "permission_requests"
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Track buyer, resource, status (pending, approved)
