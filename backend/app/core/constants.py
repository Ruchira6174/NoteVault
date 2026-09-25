from enum import Enum

class Visibility(str, Enum):
    PRIVATE = "PRIVATE"
    SEMI_PRIVATE = "SEMI_PRIVATE"
    PUBLIC = "PUBLIC"

class ResourceStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"

class AccessRequestStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class TransactionType(str, Enum):
    EARNING = "EARNING"
    WITHDRAWAL = "WITHDRAWAL"
    PURCHASE = "PURCHASE"

class ReviewRatingLimits:
    MIN_RATING = 1
    MAX_RATING = 5
