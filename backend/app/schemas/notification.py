import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class NotificationResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    message: str
    is_read: bool
    notification_type: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationUpdate(BaseModel):
    is_read: Optional[bool] = None
