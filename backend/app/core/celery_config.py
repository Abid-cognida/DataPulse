"""Celery configuration module."""

from kombu import Exchange, Queue

from app.core.config import settings

# Broker settings
broker_url = settings.REDIS_URI
result_backend = settings.REDIS_URI

# Task settings
task_serializer = "json"
accept_content = ["json"]
result_serializer = "json"
timezone = "UTC"
enable_utc = True

# Task execution settings
worker_concurrency = 8
worker_prefetch_multiplier = 1
worker_max_tasks_per_child = 1000

# Task result settings
task_ignore_result = False
task_store_errors_even_if_ignored = True
task_track_started = True

# Task retry settings
task_default_retry_delay = 3  # 3 seconds
task_max_retries = 5

# Exponential backoff retry settings
task_retry_backoff = True
task_retry_backoff_max = 600  # 10 minutes
task_retry_jitter = True  # Add random jitter to retry delays

# Task time limits
task_time_limit = 60 * 5  # 5 minutes
task_soft_time_limit = 60 * 3  # 3 minutes

# Queue settings
task_default_queue = "default"
task_default_exchange = "default"
task_default_routing_key = "default"

# Define exchanges
default_exchange = Exchange("default", type="direct")

# Define queues
task_queues = (
    Queue("default", default_exchange, routing_key="default"),
    Queue("high_priority", default_exchange, routing_key="high_priority"),
    Queue("low_priority", default_exchange, routing_key="low_priority"),
)

# Task routing
task_routes = {
    "app.tasks.high_priority.*": {"queue": "high_priority"},
    "app.tasks.low_priority.*": {"queue": "low_priority"},
}

# Logging
worker_hijack_root_logger = False
worker_log_format = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
# Format for task logs
worker_task_log_format = (
    "[%(asctime)s: %(levelname)s/%(processName)s]"
    "[%(task_name)s(%(task_id)s)] %(message)s"
)

# Security
security_key = settings.SECRET_KEY

# Flower settings
flower_port = 5555
flower_basic_auth = ["admin:admin"]  # Format: ["user:password"]
