import random
import time
from datetime import datetime, timedelta
from queue import Queue

from loguru import logger


def random_time():
    return datetime.now() + timedelta(random.randint(0, 60))


def random_message():
    words = [
        "Hola", "Adios", "Buenas tardes"
    ]
    return random.choice(words)


def generate_messages(transcribe_queue: Queue):
    alternate = True
    while True:
        dt = random_time()
        speaker = "cliente" if not alternate else "agente"
        message = random_message()
        output = {"speaker": speaker, "timestamp": dt, "message": message}
        logger.info(f"Generating {output}")
        transcribe_queue.put(output)
        alternate = not alternate
        time.sleep(3)
