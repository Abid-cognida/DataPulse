# DataPulse Infrastructure

This directory contains infrastructure-related files and configurations for the DataPulse project.

## Components

- `postgres/`: PostgreSQL database configuration
- `redis/`: Redis cache configuration

## Usage

The infrastructure is managed using Docker Compose. To start all services:

```bash
docker-compose up -d
```

To stop all services:

```bash
docker-compose down
```

## Configuration

- PostgreSQL 15 is used as the primary database
- Redis is used for caching and message queuing
