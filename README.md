# Chat Service API

A FastAPI-based chat service with MongoDB Atlas integration, providing CRUD operations for managing conversations. Built with modern Python async features and containerized with Docker.

## Features

- 🚀 FastAPI for high-performance async API
- 📦 MongoDB Atlas integration using Motor
- 🔒 Environment-based configuration
- 🐳 Docker and Docker Compose setup
- ✅ Comprehensive test suite
- 📝 Full CRUD operations for conversations
- 🔄 Real-time message management
- 📚 Auto-generated API documentation

## Prerequisites

- Docker and Docker Compose
- MongoDB Atlas account
- Python 3.11+ (for local development)

## Project Structure

```
chat_service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── conversation.py
│   └── routes/
│       ├── __init__.py
│       └── conversation.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_conversations.py
├── .env
├── .dockerignore
├── docker-compose.yml
├── docker-compose.prod.yml
├── Dockerfile
├── Makefile
└── requirements.txt
```

## Environment Setup

1. Create a `.env` file in the root directory:

```env
MONGODB_USER=your_username
MONGODB_PASSWORD=your_password
MONGODB_HOST=your_cluster.mongodb.net
ENVIRONMENT=development
HOST=0.0.0.0
PORT=8000
```

## Quick Start

1. Build the Docker containers:
```bash
make build
```

2. Start the application:
```bash
make up
```

3. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

4. Run tests:
```bash
make test
```

## API Endpoints

### Conversations

- `POST /conversations/` - Create a new conversation
- `GET /conversations/` - List all conversations
- `GET /conversations/{conversation_id}` - Get a specific conversation
- `POST /conversations/{conversation_id}/messages` - Add a message to a conversation
- `DELETE /conversations/{conversation_id}` - Delete a conversation

## Development

### Local Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

### Docker Commands

- Build containers: `make build`
- Start services: `make up`
- Stop services: `make down`
- View logs: `make logs`
- Run tests: `make test`
- Clean up: `make clean`

## Production Deployment

1. Create a `.env.production` file with production settings

2. Deploy using production compose file:
```bash
docker compose -f compose.prod.yml up -d
```

## Testing

The project includes a comprehensive test suite using pytest:

```bash
# Run tests in Docker
make test

# Run tests locally
pytest tests/ -v
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Available Make Commands

```bash
make help     # Show help message with all commands
make build    # Build all docker containers
make up       # Start all containers in detached mode
make down     # Stop all containers
make test     # Run tests in container
make logs     # View container logs
make clean    # Stop and remove all containers, volumes, and orphans
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.