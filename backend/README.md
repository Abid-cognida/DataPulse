# DataPulse Backend

This is the backend service for the DataPulse application.

## Setup

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Activate the virtual environment:
   ```bash
   poetry shell
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure

- `app/`: Main application package
  - `api/`: API endpoints
  - `core/`: Core functionality (config, security, etc.)
  - `db/`: Database models and utilities
  - `models/`: SQLAlchemy models
  - `schemas/`: Pydantic schemas
  - `services/`: Business logic
  - `tasks/`: Celery tasks
  - `worker.py`: Celery worker configuration

## Development

- Run tests: `pytest`
- Format code: `black .`
- Sort imports: `isort .`
- Lint code: `flake8 .`

## Celery and Flower

### Running Celery Worker

To run the Celery worker in development:

```bash
./run_celery.sh worker
```

### Running Flower Dashboard

To run the Flower monitoring dashboard:

```bash
./run_celery.sh flower
```

You can access the Flower dashboard at:
- Direct access: http://localhost:5555
- Through FastAPI: http://localhost:8000/api/v1/flower

The Flower dashboard is protected with basic authentication:
- Username: `admin`
- Password: `admin`

### Running Both Worker and Flower

To run both the Celery worker and Flower dashboard:

```bash
./run_celery.sh all
```

### Using Docker Compose

You can also run the entire stack using Docker Compose:

```bash
docker-compose up -d
```

This will start the FastAPI application, Celery worker, Flower dashboard, PostgreSQL, and Redis.
