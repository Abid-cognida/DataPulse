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

## Development

- Run tests: `pytest`
- Format code: `black .`
- Sort imports: `isort .`
- Lint code: `flake8 .`
