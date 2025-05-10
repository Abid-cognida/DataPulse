"""Example tasks module."""

from celery import shared_task


@shared_task(
    name="app.tasks.example.add",
    bind=True,
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
    max_retries=5,
)
def add(self, x, y):
    """Add two numbers."""
    return x + y


@shared_task(
    name="app.tasks.high_priority.process_urgent",
    queue="high_priority",
    bind=True,
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
    max_retries=5,
)
def process_urgent(self, data):
    """Process urgent data with high priority."""
    return {"status": "processed", "data": data, "priority": "high"}


@shared_task(
    name="app.tasks.low_priority.process_background",
    queue="low_priority",
    bind=True,
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
    max_retries=5,
)
def process_background(self, data):
    """Process background data with low priority."""
    return {"status": "processed", "data": data, "priority": "low"}
