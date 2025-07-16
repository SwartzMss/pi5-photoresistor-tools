import time
import RPi.GPIO as GPIO  # type: ignore


__all__ = ["rc_time"]


def rc_time(pin: int) -> int:
    """Return the charge time for the given GPIO pin."""
    count = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == GPIO.LOW:
        count += 1
    return count
