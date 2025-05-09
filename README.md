# DataPulse

DataPulse is a monorepo project with a Python backend and React frontend.

## Project Structure

- `backend/`: Python backend using FastAPI and Poetry
- `frontend/`: React frontend using TypeScript and PNPM
- `infra/`: Infrastructure configuration
- `docker-compose.yml`: Docker Compose configuration for local development

## Setup

### Prerequisites

- Python 3.9+
- Node.js 18+
- PNPM
- Poetry
- Docker and Docker Compose

### Backend Setup

```bash
cd backend
poetry install
poetry shell
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
pnpm install
pnpm dev
```

### Infrastructure Setup

```bash
docker-compose up -d
```

## Development

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. To install:

```bash
pip install pre-commit
pre-commit install
```

### Backend Development

The backend is built with:
- FastAPI for the web framework
- SQLAlchemy for ORM
- Alembic for database migrations
- Poetry for dependency management

### Frontend Development

The frontend is built with:
- React for the UI library
- TypeScript for type safety
- Vite for the build tool
- PNPM for package management
