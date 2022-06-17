"""it is the Celery section."""
from celery import Celery


REDIS_URL = 'redis://localhost:6379/0'

app = Celery('tasks', backend=REDIS_URL, broker=REDIS_URL)


@app.task
def add(first_term: int, second_term: int) -> int:
    """
    Task for adding two terms.

    Using Celery
    """
    return first_term + second_term
