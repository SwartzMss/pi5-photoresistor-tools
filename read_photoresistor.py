import time
import RPi.GPIO as GPIO  # type: ignore

PIN = 4  # 光敏电阻电路连接的 GPIO 引脚编号


def rc_time(pin: int) -> int:
    """测量引脚从低电平变为高电平所需的时间。"""
    count = 0

    # 放电
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    # 切换到输入模式
    GPIO.setup(pin, GPIO.IN)

    # 计数直到引脚为高电平
    while GPIO.input(pin) == GPIO.LOW:
        count += 1
    return count


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    try:
        while True:
            value = rc_time(PIN)
            print(f"光照值: {value}")
            time.sleep(1)
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
