import os
import pytest
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.testclient import TestClient
from app.main import app
from app.database import Database
from app.config import get_settings


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


def get_test_settings():
    """Get test-specific settings"""
    settings = get_settings()
    # MongoDB connection settings are now handled by environment variables
    return settings


@pytest.fixture(scope="session", autouse=True)
async def setup_test_db():
    """Setup test database connection"""
    settings = get_test_settings()

    # Setup
    Database.client = AsyncIOMotorClient(settings.get_mongodb_url())
    await Database.client.test_chat_db.command("ping")  # Test connection
    yield Database.client

    # Cleanup
    if Database.client is not None:
        await Database.client.drop_database(settings.database_name)
        Database.client.close()


@pytest.fixture
async def test_client():
    """Create a test client for the FastAPI application"""
    async with TestClient(app) as client:
        yield client


@pytest.fixture
async def test_db():
    """Get test database instance with cleanup"""
    settings = get_test_settings()
    db = Database.client[settings.database_name]
    yield db
    # Cleanup after each test
    await db.conversations.delete_many({})
