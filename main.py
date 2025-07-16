import argparse
import time
import lgpio

from photoresistor import rc_time


def main() -> None:
    parser = argparse.ArgumentParser(description="Read photoresistor value")
    parser.add_argument(
        "--pin",
        type=int,
        default=17,
        help="GPIO pin connected to the photoresistor",
    )
    args = parser.parse_args()

    handle = lgpio.gpiochip_open(0)
    try:
        while True:
            value = rc_time(handle, args.pin)
            print(f"\u5149\u7167\u503C: {value}")
            time.sleep(1)
    finally:
        lgpio.gpiochip_close(handle)


if __name__ == "__main__":
    main()
