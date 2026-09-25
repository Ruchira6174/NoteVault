from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from decimal import Decimal
from typing import List
from app.models.resource import Resource
from app.schemas.resource import ResourceCreate, ResourceUpdate
from app.core.constants import Visibility, ResourceStatus

class ResourceService:
    @staticmethod
    def create_resource(db: Session, user_id: UUID, resource_in: ResourceCreate) -> Resource:
        db_resource = Resource(
            owner_id=user_id,
            **resource_in.model_dump(exclude_unset=True)
        )
        db.add(db_resource)
        db.commit()
        db.refresh(db_resource)
        return db_resource

    @staticmethod
    def get_my_resources(db: Session, user_id: UUID) -> List[Resource]:
        return db.query(Resource).filter(
            Resource.owner_id == user_id,
            Resource.status != ResourceStatus.DELETED
        ).all()

    @staticmethod
    def get_resource_by_id(db: Session, resource_id: UUID, user_id: UUID) -> Resource:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
        if resource.owner_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to access this resource")
        if resource.status == ResourceStatus.DELETED:
            raise HTTPException(status_code=404, detail="Resource not found")
        return resource

    @staticmethod
    def update_resource(db: Session, resource_id: UUID, user_id: UUID, resource_in: ResourceUpdate) -> Resource:
        resource = ResourceService.get_resource_by_id(db, resource_id, user_id)
        
        update_data = resource_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(resource, field, value)
            
        db.commit()
        db.refresh(resource)
        return resource

    @staticmethod
    def delete_resource(db: Session, resource_id: UUID, user_id: UUID) -> dict:
        resource = ResourceService.get_resource_by_id(db, resource_id, user_id)
        resource.status = ResourceStatus.DELETED
        db.commit()
        return {"message": "Resource successfully soft deleted"}

    @staticmethod
    def publish_resource(db: Session, resource_id: UUID, user_id: UUID, publish: bool) -> Resource:
        resource = ResourceService.get_resource_by_id(db, resource_id, user_id)
        resource.status = ResourceStatus.PUBLISHED if publish else ResourceStatus.DRAFT
        db.commit()
        db.refresh(resource)
        return resource

    @staticmethod
    def update_visibility(db: Session, resource_id: UUID, user_id: UUID, visibility: Visibility) -> Resource:
        resource = ResourceService.get_resource_by_id(db, resource_id, user_id)
        resource.visibility = visibility
        db.commit()
        db.refresh(resource)
        return resource

    @staticmethod
    def update_price(db: Session, resource_id: UUID, user_id: UUID, is_paid: bool, price: Decimal, currency: str = "INR") -> Resource:
        if price < 0:
            raise HTTPException(status_code=400, detail="Price cannot be negative")
            
        resource = ResourceService.get_resource_by_id(db, resource_id, user_id)
        resource.is_paid = is_paid
        resource.price = price
        resource.currency = currency
        db.commit()
        db.refresh(resource)
        return resource
