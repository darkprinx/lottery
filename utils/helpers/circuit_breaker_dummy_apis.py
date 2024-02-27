from datetime import datetime
import random

from core.settings import breaker


@breaker
def send_message():
    rand_data = random.randint(0, 3)
    if rand_data == 2:
        raise Exception("message send failed")
    return f"Hello, msg sent at {datetime.now()}"
