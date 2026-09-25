import os

files = {
    "frontend/package.json": """{
  "name": "notevault-ai",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "15.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "postcss": "^8",
    "tailwindcss": "^3.4.1"
  }
}
""",
    "frontend/tsconfig.json": """{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
""",
    "frontend/tailwind.config.ts": """import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
export default config;
""",
    "frontend/postcss.config.js": """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
""",
    "frontend/next.config.mjs": """/** @type {import('next').NextConfig} */
const nextConfig = {};

export default nextConfig;
""",
    "frontend/.env.example": """NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_APP_URL=http://localhost:3000
""",
    "frontend/components.json": """{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
""",
    "frontend/app/layout.tsx": """import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AppProvider } from "@/providers/AppProvider";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "NoteVault AI",
  description: "AI-powered study material marketplace",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* TODO: Add proper layout structure */}
        <AppProvider>{children}</AppProvider>
      </body>
    </html>
  );
}
""",
    "frontend/app/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
  }
  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
  }
}
""",
    "frontend/app/page.tsx": """import React from 'react';

// Landing page for NoteVault AI
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>Welcome to NoteVault AI</h1>
      {/* TODO: Implement landing page */}
    </main>
  );
}
""",
    "frontend/app/(auth)/login/page.tsx": """import React from 'react';

// Login page
export default function LoginPage() {
  return (
    <div>
      <h1>Login</h1>
      {/* TODO: Implement login form */}
    </div>
  );
}
""",
    "frontend/app/(auth)/register/page.tsx": """import React from 'react';

// Registration page
export default function RegisterPage() {
  return (
    <div>
      <h1>Create Account</h1>
      {/* TODO: Implement registration form */}
    </div>
  );
}
""",
    "frontend/app/(dashboard)/dashboard/page.tsx": """import React from 'react';

// Main student dashboard
export default function DashboardPage() {
  return (
    <div>
      <h1>Dashboard</h1>
      {/* TODO: Display overview of resources, wallet, etc. */}
    </div>
  );
}
""",
    "frontend/app/(dashboard)/profile/page.tsx": """import React from 'react';

// Student profile management
export default function ProfilePage() {
  return (
    <div>
      <h1>My Profile</h1>
      {/* TODO: Implement profile editor (college, university, etc.) */}
    </div>
  );
}
""",
    "frontend/app/(dashboard)/library/page.tsx": """import React from 'react';

// Personal library for uploaded/purchased notes
export default function LibraryPage() {
  return (
    <div>
      <h1>Personal Library</h1>
      {/* TODO: Display organized notes, subject/semester filters */}
    </div>
  );
}
""",
    "frontend/app/(dashboard)/wallet/page.tsx": """import React from 'react';

// Earnings and transactions
export default function WalletPage() {
  return (
    <div>
      <h1>My Wallet</h1>
      {/* TODO: Display earnings, transaction history */}
    </div>
  );
}
""",
    "frontend/app/(marketplace)/marketplace/page.tsx": """import React from 'react';

// Public marketplace to discover resources
export default function MarketplacePage() {
  return (
    <div>
      <h1>Marketplace</h1>
      {/* TODO: Implement search, filters, list of resources */}
    </div>
  );
}
""",
    "frontend/app/(marketplace)/resource/[id]/page.tsx": """import React from 'react';

// Resource details and preview
export default function ResourceDetailsPage({ params }: { params: { id: string } }) {
  return (
    <div>
      <h1>Resource Details: {params.id}</h1>
      {/* TODO: Display AI score, preview pages, price, buy/request access button */}
    </div>
  );
}
""",
    "frontend/components/layout/Navbar.tsx": """import React from 'react';

export function Navbar() {
  return (
    <nav>
      {/* TODO: Navigation links */}
    </nav>
  );
}
""",
    "frontend/components/layout/Sidebar.tsx": """import React from 'react';

export function Sidebar() {
  return (
    <aside>
      {/* TODO: Dashboard sidebar links */}
    </aside>
  );
}
""",
    "frontend/components/layout/Footer.tsx": """import React from 'react';

export function Footer() {
  return (
    <footer>
      {/* TODO: Footer links */}
    </footer>
  );
}
""",
    "frontend/components/profile/ProfileCard.tsx": """import React from 'react';

// Reusable profile card component
export function ProfileCard() {
  return (
    <div>
      {/* TODO: Show user avatar, bio, stats */}
    </div>
  );
}
""",
    "frontend/components/resource/ResourceCard.tsx": """import React from 'react';

// Displays a resource in marketplace or library
export function ResourceCard() {
  return (
    <div>
      {/* TODO: Resource thumbnail, title, AI score, price */}
    </div>
  );
}
""",
    "frontend/components/resource/UploadForm.tsx": """import React from 'react';

// Form to upload PDFs, notes, set visibility and price
export function UploadForm() {
  return (
    <form>
      {/* TODO: File input, visibility dropdown, price input */}
    </form>
  );
}
""",
    "frontend/lib/utils.ts": """import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
""",
    "frontend/lib/api.ts": """// Axios or fetch configuration for API calls
export const apiClient = {};
// TODO: Setup interceptors for auth tokens
""",
    "frontend/hooks/useAuth.ts": """// Hook for authentication state
export function useAuth() {
  // TODO: Implement auth state (context/zustand/redux)
  return { user: null, isAuthenticated: false };
}
""",
    "frontend/hooks/useResource.ts": """// Hook for resource actions
export function useResource() {
  // TODO: Implement fetch/upload resource logic
  return {};
}
""",
    "frontend/types/index.ts": """// Global types for frontend
export interface UserProfile {
  id: string;
  name: string;
  username: string;
  // TODO: Add remaining profile fields
}

export interface Resource {
  id: string;
  title: string;
  // TODO: Add remaining resource fields
}
""",
    "frontend/providers/AppProvider.tsx": """'use client';
import React from 'react';

// Global providers wrapper
export function AppProvider({ children }: { children: React.ReactNode }) {
  return (
    <>
      {/* TODO: Wrap with Redux/ReactQuery/ThemeProvider */}
      {children}
    </>
  );
}
""",
    "backend/requirements.txt": """fastapi==0.109.2
uvicorn[standard]==0.27.1
sqlalchemy==2.0.27
alembic==1.13.1
psycopg2-binary==2.9.9
redis==5.0.1
langchain==0.1.9
chromadb==0.4.22
boto3==1.34.49
python-dotenv==1.0.1
pydantic==2.6.1
""",
    "backend/.env.example": """DATABASE_URL=postgresql://user:password@localhost:5432/notevault
REDIS_URL=redis://localhost:6379
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_BUCKET_NAME=notevault-storage
OPENAI_API_KEY=your_openai_key
""",
    "backend/app/main.py": """from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(title="NoteVault AI API")

# TODO: Add CORS middleware

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to NoteVault AI API"}
""",
    "backend/app/core/config.py": """from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "NoteVault AI"
    # TODO: Add DB, Redis, AWS, AI config variables

    class Config:
        env_file = ".env"

settings = Settings()
""",
    "backend/app/core/database.py": """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# TODO: Setup database connection
# engine = create_engine(settings.DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
""",
    "backend/app/core/security.py": """# Security utilities (hashing, JWT)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # TODO: Implement verification
    pass

def get_password_hash(password: str) -> str:
    # TODO: Implement hashing
    pass
""",
    "backend/app/api/api_v1/api.py": """from fastapi import APIRouter
from app.api.api_v1.endpoints import users, resources, marketplace, wallet, permissions

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(resources.router, prefix="/resources", tags=["resources"])
api_router.include_router(marketplace.router, prefix="/marketplace", tags=["marketplace"])
api_router.include_router(permissions.router, prefix="/permissions", tags=["permissions"])
api_router.include_router(wallet.router, prefix="/wallet", tags=["wallet"])
""",
    "backend/app/api/api_v1/endpoints/users.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def read_user_me():
    # TODO: Get current user profile
    pass

@router.put("/me")
def update_user_me():
    # TODO: Update user profile (college, course, etc.)
    pass
""",
    "backend/app/api/api_v1/endpoints/resources.py": """from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_resource():
    # TODO: Handle file upload, save metadata
    pass

@router.get("/")
def get_library():
    # TODO: Get user's personal library
    pass
""",
    "backend/app/api/api_v1/endpoints/marketplace.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def browse_marketplace():
    # TODO: Return public and semi-private resources
    pass
""",
    "backend/app/api/api_v1/endpoints/permissions.py": """from fastapi import APIRouter

router = APIRouter()

@router.post("/request")
def request_access():
    # TODO: Buyer requests access to a resource
    pass

@router.post("/{request_id}/approve")
def approve_access():
    # TODO: Owner approves access
    pass
""",
    "backend/app/api/api_v1/endpoints/wallet.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_wallet_balance():
    # TODO: Return user wallet balance and history
    pass
""",
    "backend/app/models/user.py": """from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Add profile fields (username, bio, college, branch, etc.)
""",
    "backend/app/models/resource.py": """from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Add visibility (Private, Semi-private, Public), price, etc.
""",
    "backend/app/models/permission.py": """from sqlalchemy import Column, Integer, String
from app.core.database import Base

class PermissionRequest(Base):
    __tablename__ = "permission_requests"
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Track buyer, resource, status (pending, approved)
""",
    "backend/app/models/wallet.py": """from sqlalchemy import Column, Integer, String
from app.core.database import Base

class WalletTransaction(Base):
    __tablename__ = "wallet_transactions"
    id = Column(Integer, primary_key=True, index=True)
    # TODO: Track earnings, purchases
""",
    "backend/app/schemas/user.py": """from pydantic import BaseModel

class UserProfileResponse(BaseModel):
    id: int
    # TODO: Add Pydantic schema fields
""",
    "backend/app/schemas/resource.py": """from pydantic import BaseModel

class ResourceCreate(BaseModel):
    # TODO: Schema for resource creation
    pass
""",
    "backend/app/schemas/permission.py": """from pydantic import BaseModel

class PermissionResponse(BaseModel):
    # TODO: Schema for permission responses
    pass
""",
    "backend/app/schemas/wallet.py": """from pydantic import BaseModel

class WalletResponse(BaseModel):
    # TODO: Schema for wallet balance
    pass
""",
    "backend/app/services/user_service.py": """# Service logic for Users
class UserService:
    # TODO: Business logic for user profiles
    pass
""",
    "backend/app/services/resource_service.py": """# Service logic for Resources
class ResourceService:
    # TODO: Business logic for handling uploads and library
    pass
""",
    "backend/app/services/ai_service.py": """# Coordinates AI operations
class AIService:
    # TODO: Trigger OCR, RAG, Verification on upload
    pass
""",
    "backend/app/services/wallet_service.py": """# Service logic for Wallet
class WalletService:
    # TODO: Handle credits, deductions on purchase
    pass
""",
    "backend/app/services/permission_service.py": """# Service logic for Permissions
class PermissionService:
    # TODO: Handle access requests and approvals
    pass
""",
    "backend/app/ai/ocr.py": """# OCR Extraction
def extract_text(file_path: str):
    # TODO: Use appropriate OCR library
    pass
""",
    "backend/app/ai/rag.py": """# RAG Pipeline
def generate_summary(text: str):
    # TODO: LangChain integration for summary/quiz
    pass
""",
    "backend/app/ai/verifier.py": """# AI Quality Verification
def verify_quality(text: str):
    # TODO: Generate AI Quality Report, score, plagiarism check
    pass
""",
    "backend/app/ai/embeddings.py": """# Vector Embeddings
def generate_and_store_embeddings(text: str):
    # TODO: ChromaDB integration
    pass
""",
    "backend/app/storage/s3.py": """# AWS S3 Integration
def upload_to_s3(file_data):
    # TODO: Implement secure upload, generate signed URLs
    pass
""",
    "backend/app/storage/watermark.py": """# Watermarking
def generate_watermarked_preview(file_data):
    # TODO: Create preview for marketplace
    pass
""",
    "backend/app/middleware/auth_middleware.py": """# Authentication Middleware
# TODO: Implement request interceptor to check JWT
""",
    "backend/app/middleware/logging.py": """# Logging Middleware
# TODO: Log API requests
""",
    "backend/app/dependencies/auth.py": """# FastAPI Auth Dependencies
def get_current_user():
    # TODO: Extract and verify user from token
    pass
""",
    "backend/app/dependencies/db.py": """# Database session dependency
def get_db():
    # TODO: Yield DB session
    pass
""",
    "backend/app/utils/helpers.py": """# Utility functions
def format_currency():
    pass
""",
    "docker/docker-compose.yml": """version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: notevault
    ports:
      - "5432:5432"

  redis:
    image: redis:7
    ports:
      - "6379:6379"

  backend:
    build:
      context: ../backend
      dockerfile: ../docker/Dockerfile.backend
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis

  frontend:
    build:
      context: ../frontend
      dockerfile: ../docker/Dockerfile.frontend
    ports:
      - "3000:3000"
""",
    "docker/Dockerfile.backend": """FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt .
# TODO: Install dependencies
# RUN pip install -r requirements.txt

COPY backend/ .
# TODO: Expose port and run uvicorn
""",
    "docker/Dockerfile.frontend": """FROM node:20-alpine

WORKDIR /app
COPY frontend/package*.json ./
# TODO: npm install

COPY frontend/ .
# TODO: Build Next.js and run
""",
    "docs/architecture.md": """# NoteVault AI Architecture

## Overview
This document describes the layered architecture of NoteVault AI.

## Layers
1. **API**: FastAPI routes
2. **Services**: Business logic
3. **Models/Schemas**: SQLAlchemy and Pydantic
4. **AI**: LangChain, ChromaDB
5. **Storage**: S3

## Rules
- No business logic in API endpoints.
- All AI operations are encapsulated in the `ai` module.
""",
    "docs/api_spec.md": """# NoteVault AI API Specification

## Endpoints
- `/users/me`
- `/resources/upload`
- `/permissions/request`
...
""",
    "shared/openapi.json": """{
  "openapi": "3.1.0",
  "info": {
    "title": "NoteVault AI API",
    "version": "0.1.0"
  },
  "paths": {}
}
"""
}

for filepath, content in files.items():
    dir_name = os.path.dirname(filepath)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Files generated successfully.")
