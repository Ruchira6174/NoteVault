# NoteVault AI Architecture

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
