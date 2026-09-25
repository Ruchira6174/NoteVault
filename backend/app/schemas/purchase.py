import uuid
from typing import Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from app.schemas.resource import ResourceCardResponse

class PurchaseResponse(BaseModel):
    id: uuid.UUID
    resource_id: Optional[uuid.UUID]
    buyer_id: uuid.UUID
    amount: Decimal
    currency: str
    transaction_id: Optional[str]
    purchased_at: datetime
    expires_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

class PurchasedResourceResponse(BaseModel):
    purchase_info: PurchaseResponse
    resource_preview: ResourceCardResponse
    download_permission: bool = True

    model_config = ConfigDict(from_attributes=True)
