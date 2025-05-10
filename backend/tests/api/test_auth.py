"""Test authentication endpoints."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User


@pytest.fixture
def test_user(db_session: Session):
    """Create a test user."""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password=get_password_hash("password123"),
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def test_register_user(client: TestClient, db_session: Session):
    """Test user registration."""
    # Test successful registration
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "password123",
            "is_active": True,
            "is_superuser": False,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "newuser@example.com"
    assert "id" in data
    assert "password" not in data

    # Test duplicate username
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "newuser",
            "email": "another@example.com",
            "password": "password123",
            "is_active": True,
            "is_superuser": False,
        },
    )
    assert response.status_code == 400
    assert "Username already registered" in response.json()["detail"]

    # Test duplicate email
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "anotheruser",
            "email": "newuser@example.com",
            "password": "password123",
            "is_active": True,
            "is_superuser": False,
        },
    )
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]


def test_login(client: TestClient, test_user: User):
    """Test user login."""
    # Test successful login
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "testuser", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    # Test login with email
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

    # Test invalid password
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "testuser", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]

    # Test non-existent user
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "nonexistent", "password": "password123"},
    )
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]
