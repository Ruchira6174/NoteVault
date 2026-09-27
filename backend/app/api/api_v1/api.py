# pyrefly: ignore [missing-import]
from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    auth,
    users,
    resources,
    marketplace,
    wallet,
    permissions,
)

api_router = APIRouter()

# Authentication
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

# Users
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)

# Resources
api_router.include_router(
    resources.router,
    prefix="/resources",
    tags=["Resources"],
)

# Marketplace
api_router.include_router(
    marketplace.router,
    prefix="/marketplace",
    tags=["Marketplace"],
)

# Permissions
api_router.include_router(
    permissions.router,
    prefix="/permissions",
    tags=["Permissions"],
)

# Wallet
api_router.include_router(
    wallet.router,
    prefix="/wallet",
    tags=["Wallet"],
)