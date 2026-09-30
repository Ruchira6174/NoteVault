from enum import Enum

class Visibility(str, Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"

class ResourceStatus(str, Enum):
    PENDING = "PENDING"
    PUBLISHED = "PUBLISHED"

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
