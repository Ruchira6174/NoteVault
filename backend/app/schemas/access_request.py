import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.core.constants import AccessRequestStatus

class AccessRequestCreate(BaseModel):
    resource_id: uuid.UUID
    request_message: Optional[str] = Field(None, max_length=1000)

class AccessApprovalRequest(BaseModel):
    owner_message: Optional[str] = Field(None, max_length=1000)

class AccessRejectRequest(BaseModel):
    owner_message: Optional[str] = Field(None, max_length=1000)

class AccessRequestResponse(BaseModel):
    id: uuid.UUID
    resource_id: uuid.UUID
    buyer_id: uuid.UUID
    owner_id: uuid.UUID
    status: AccessRequestStatus
    request_message: Optional[str]
    owner_response: Optional[str]
    requested_at: datetime
    responded_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
