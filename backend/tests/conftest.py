"""Pytest configuration."""

import asyncio
from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.base import Base, get_async_db, get_db
from app.main import app


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def test_db_url():
    """Get test database URL."""
    return str(settings.SQLALCHEMY_DATABASE_URI) + "_test"


@pytest.fixture(scope="session")
def test_async_db_url():
    """Get test async database URL."""
    return str(settings.ASYNC_SQLALCHEMY_DATABASE_URI) + "_test"


@pytest.fixture(scope="session")
def engine(test_db_url):
    """Create engine for testing."""
    engine = create_engine(test_db_url)
    yield engine
    engine.dispose()


@pytest.fixture(scope="session")
def async_engine(test_async_db_url):
    """Create async engine for testing."""
    engine = create_async_engine(test_async_db_url)
    yield engine
    asyncio.run(engine.dispose())


@pytest.fixture(scope="session")
def create_tables(engine):
    """Create all tables."""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(engine, create_tables):
    """Create new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    session_factory = sessionmaker(bind=connection)
    session = session_factory()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
async def async_db_session(async_engine, create_tables):
    """Create new async database session for a test."""
    async with async_engine.connect() as connection:
        await connection.begin()
        session_factory = sessionmaker(
            bind=connection, class_=AsyncSession, expire_on_commit=False
        )
        session = session_factory()

        yield session

        await session.close()
        await connection.rollback()


@pytest.fixture(scope="function")
def client(db_session) -> Generator:
    """Create test client."""
    app.dependency_overrides[get_db] = lambda: db_session
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
async def async_client(async_db_session) -> AsyncGenerator:
    """Create async test client."""

    async def override_get_async_db():
        yield async_db_session

    app.dependency_overrides[get_async_db] = override_get_async_db
    with TestClient(app) as test_client:
        yield test_client
