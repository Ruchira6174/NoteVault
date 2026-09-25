import uuid
from typing import List, Optional
from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class MonthlyRevenue(BaseModel):
    month: str
    revenue: Decimal
    
    model_config = ConfigDict(from_attributes=True)

class ResourcePerformance(BaseModel):
    resource_id: uuid.UUID
    title: str
    views: int
    downloads: int
    sales_count: int
    revenue_generated: Decimal
    
    model_config = ConfigDict(from_attributes=True)

class CreatorStatistics(BaseModel):
    average_rating: float
    total_followers: int
    top_performing_subject: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)

class DashboardAnalytics(BaseModel):
    total_resources: int
    total_revenue: Decimal
    monthly_revenue: List[MonthlyRevenue]
    top_resources: List[ResourcePerformance]
    statistics: CreatorStatistics
    
    model_config = ConfigDict(from_attributes=True)
