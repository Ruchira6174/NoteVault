import uuid
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.models.resource import Resource
from app.schemas.resource import ResourceCreate, ResourceUpdate
from app.core.constants import Visibility, ResourceStatus

class ResourceService:
    @staticmethod
    def create_resource(db: Session, user_id: uuid.UUID, resource_in: ResourceCreate) -> Resource:
        db_resource = Resource(
            owner_id=user_id,
            **resource_in.model_dump(exclude_unset=True)
        )
        db.add(db_resource)
        db.commit()
        db.refresh(db_resource)
        return db_resource

    @staticmethod
    def get_my_resources(db: Session, user_id: uuid.UUID) -> List[Resource]:
        return db.query(Resource).filter(
            Resource.owner_id == user_id
        ).order_by(Resource.created_at.desc()).all()

    @staticmethod
    def get_resource_by_id(db: Session, resource_id: uuid.UUID, user_id: uuid.UUID) -> Resource:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
            
        if resource.owner_id != user_id:
            if resource.visibility == Visibility.PRIVATE or resource.status == ResourceStatus.PENDING:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this private resource")
                
        return resource

    @staticmethod
    def update_resource(db: Session, resource_id: uuid.UUID, user_id: uuid.UUID, resource_in: ResourceUpdate) -> Resource:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
            
        if resource.owner_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to edit this resource")
        
        update_data = resource_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(resource, field, value)
            
        db.commit()
        db.refresh(resource)
        return resource

    @staticmethod
    def delete_resource(db: Session, resource_id: uuid.UUID, user_id: uuid.UUID):
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
            
        if resource.owner_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this resource")
            
        db.delete(resource)
        db.commit()
        return None

    @staticmethod
    def publish_resource(db: Session, resource_id: uuid.UUID, user_id: uuid.UUID, publish: bool) -> Resource:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
            
        if resource.owner_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to edit this resource")
            
        resource.status = ResourceStatus.PUBLISHED if publish else ResourceStatus.PENDING
        db.commit()
        db.refresh(resource)
        return resource
