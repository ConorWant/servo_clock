from adafruit_servokit import ServoKit
from datetime import datetime
from time import sleep

CHANNELS = list(range(0, 14))
PULSE_MIN = 500
PULSE_MAX = 2500
SERVO_ON_ANGLE = 180
SERVO_OFF_ANGLE = 100
GROUP1 = list(range(0, 7))
GROUP2 = list(range(7, 14))

DIGIT_SEGMENTS = {
    "0": [0, 1, 2, 3, 4, 5],
    "1": [1, 2],
    "2": [0, 1, 3, 4, 6],
    "3": [0, 1, 2, 3, 6],
    "4": [1, 2, 5, 6],
    "5": [0, 2, 3, 5, 6],
    "6": [0, 2, 3, 4, 5, 6],
    "7": [0, 1, 2],
    "8": [0, 1, 2, 3, 4, 5, 6],
    "9": [0, 1, 2, 3, 5, 6],
}


def servo_on(kit, channels):
    for ch in channels:
        kit.servo[ch].angle = SERVO_ON_ANGLE


def servo_off(kit, channels):
    for ch in channels:
        kit.servo[ch].angle = SERVO_OFF_ANGLE


def change_number(kit, group, number):
    if number in DIGIT_SEGMENTS:
        offset = group[0]
       	servo_off(kit, group)
       	servo_on(kit, [ch + offset for ch in DIGIT_SEGMENTS[number]])


def main():
    kit1 = ServoKit(channels=16, address=0x40)
    kit2 = ServoKit(channels=16, address=0x41)

    for kit in (kit1, kit2):
        for ch in CHANNELS:
            kit.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
        servo_off(kit, GROUP1)
        servo_off(kit, GROUP2)

    try:
        while True:
            second = datetime.now().strftime("%S")[1]
            print(second)
            change_number(kit2, GROUP2, second)
            sleep(1)
            
    except KeyboardInterrupt:
        for kit in (kit1, kit2):
            servo_off(kit, GROUP1)
            servo_off(kit, GROUP2)

if __name__ == "__main__":
    main()
