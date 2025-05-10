"""Flower monitoring endpoints module."""

import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.core.celery_config import flower_basic_auth

router = APIRouter()
security = HTTPBasic()


def get_current_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> str:
    """Validate basic auth credentials."""
    # Parse flower_basic_auth list
    valid_credentials = {}
    for auth in flower_basic_auth:
        if ":" in auth:
            username, password = auth.split(":", 1)
            valid_credentials[username] = password

    if credentials.username not in valid_credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    if not secrets.compare_digest(
        credentials.password, valid_credentials[credentials.username]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


@router.get("/", response_class=HTMLResponse)
async def flower_dashboard(
    request: Request, username: str = Depends(get_current_user)
) -> RedirectResponse:
    """Redirect to Flower dashboard."""
    return RedirectResponse(url="/flower/dashboard")


@router.get("/dashboard", response_class=HTMLResponse)
async def flower_dashboard_page(
    username: str = Depends(get_current_user),
) -> HTMLResponse:
    """Flower dashboard HTML page."""
    # This is a simple HTML page that embeds the Flower dashboard
    # In a real-world scenario, you would use a reverse proxy to forward requests
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flower Dashboard</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
                overflow: hidden;
            }
            iframe {
                width: 100%;
                height: 100%;
                border: none;
            }
        </style>
    </head>
    <body>
        <iframe src="http://localhost:5555" frameborder="0"></iframe>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
