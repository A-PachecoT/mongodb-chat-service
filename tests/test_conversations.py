import pytest
from httpx import AsyncClient
from app.main import app

pytestmark = pytest.mark.asyncio


class TestConversations:
    """Test suite for conversation endpoints"""

    @pytest.fixture(autouse=True)
    async def setup(self, setup_test_db):
        """Setup for each test"""
        self.base_url = "http://test"

    async def test_create_conversation(self):
        async with AsyncClient(app=app, base_url=self.base_url) as ac:
            response = await ac.post(
                "/conversations/",
                json={"title": "Test Conversation", "participants": ["user1", "user2"]},
            )

            assert response.status_code == 200
            data = response.json()
            assert data["title"] == "Test Conversation"
            assert data["participants"] == ["user1", "user2"]
            assert "messages" in data
            assert len(data["messages"]) == 0
            assert "_id" in data

    async def test_get_conversations(self):
        async with AsyncClient(app=app, base_url=self.base_url) as ac:
            # Create a test conversation first
            await ac.post(
                "/conversations/",
                json={"title": "Test Conversation", "participants": ["user1", "user2"]},
            )

            response = await ac.get("/conversations/")
            assert response.status_code == 200
            data = response.json()
            assert len(data) > 0
            assert isinstance(data, list)

    async def test_add_message(self):
        async with AsyncClient(app=app, base_url=self.base_url) as ac:
            # Create a conversation
            conv_response = await ac.post(
                "/conversations/",
                json={"title": "Test Conversation", "participants": ["user1", "user2"]},
            )
            conv_id = conv_response.json()["_id"]

            # Add a message
            response = await ac.post(
                f"/conversations/{conv_id}/messages",
                json={"content": "Hello, World!", "sender": "user1"},
            )

            assert response.status_code == 200
            assert response.json()["status"] == "success"

    async def test_delete_conversation(self):
        async with AsyncClient(app=app, base_url=self.base_url) as ac:
            # Create a conversation
            conv_response = await ac.post(
                "/conversations/",
                json={"title": "Test Conversation", "participants": ["user1", "user2"]},
            )
            conv_id = conv_response.json()["_id"]

            # Delete the conversation
            response = await ac.delete(f"/conversations/{conv_id}")
            assert response.status_code == 200
            assert response.json()["status"] == "success"

            # Verify deletion
            get_response = await ac.get(f"/conversations/{conv_id}")
            assert get_response.status_code == 404
