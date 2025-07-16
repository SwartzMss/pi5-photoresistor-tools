import time
import lgpio


__all__ = ["rc_time"]


def rc_time(handle: int, pin: int) -> int:
    """Return the charge time for the given GPIO pin."""
    count = 0
    lgpio.gpio_claim_output(handle, pin, lgpio.LOW)
    time.sleep(0.1)
    lgpio.gpio_claim_input(handle, pin)
    while lgpio.gpio_read(handle, pin) == lgpio.LOW:
        count += 1
    lgpio.gpio_free(handle, pin)
    return count
