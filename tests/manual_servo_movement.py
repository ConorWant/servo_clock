from adafruit_servokit import ServoKit

BOARD1_CHANNELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
BOARD2_CHANNELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
PULSE_MIN = 500
PULSE_MAX = 2500
GROUP1 = list(range(0, 7))
GROUP2 = list(range(7, 14))

def servo_on(kit, channels):
    for ch in channels:
        kit.servo[ch].angle = 180

def servo_off(kit, channels):
    for ch in channels:
        kit.servo[ch].angle = 120

def change_number(kit, group, number):
    NUMBERS = {
        "0": zero, "1": one, "2": two, "3": three, "4": four,
        "5": five, "6": six, "7": seven, "8": eight, "9": nine,
    }
    if number in NUMBERS:
        servo_off(kit, group)
        NUMBERS[number](kit)

def one(kit):
    servo_on(kit, [1, 2])

def two(kit):
    servo_on(kit, [0, 1, 3, 4, 6])

def three(kit):
    servo_on(kit, [0, 1, 2, 3, 6])

def four(kit):
    servo_on(kit, [1, 2, 5, 6])

def five(kit):
    servo_on(kit, [0, 2, 3, 5, 6])

def six(kit):
    servo_on(kit, [0, 2, 3, 4, 5, 6])

def seven(kit):
    servo_on(kit, [0, 1, 2])

def eight(kit):
    servo_on(kit, [0, 1, 2, 3, 4, 5, 6])

def nine(kit):
    servo_on(kit, [0, 1, 2, 3, 5, 6])

def zero(kit):
    servo_on(kit, [0, 1, 2, 3, 4, 5])

def main():
    kit1 = ServoKit(channels=16, address=0x40)
    kit2 = ServoKit(channels=16, address=0x41)

    for ch in BOARD1_CHANNELS:
        kit1.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
    for ch in BOARD2_CHANNELS:
        kit2.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)

    servo_off(kit1, GROUP1)
    servo_off(kit1, GROUP2)
    servo_off(kit2, GROUP1)
    servo_off(kit2, GROUP2)

    GROUPS = {
        "b1g1": (kit1, GROUP1),
        "b1g2": (kit1, GROUP2),
        "b2g1": (kit2, GROUP1),
        "b2g2": (kit2, GROUP2),
    }

    print("Manual servo control")
    print("Format: <group> <number> e.g. 'b1g1 5'")
    print("Type 'off' to turn all servos off, 'q' to quit.\n")

    while True:
        user_input = input("Command: ").strip().lower()

        if user_input == "q":
            print("Bye!")
            break

        if user_input == "off":
            for kit, group in GROUPS.values():
                servo_off(kit, group)
            print("  ? all servos off")
            continue

        parts = user_input.split()
        if len(parts) != 2:
            print("  Format: <group> <number> e.g. 'b1g1 5'")
            print("  Or type 'off' to turn all servos off.")
            continue

        group_name, number = parts
        if group_name not in GROUPS:
            print(f"  Unknown group '{group_name}' use b1g1, b1g2, b2g1, or b2g2.")
            continue

        if number not in "0123456789" or len(number) != 1:
            print("  Number must be a single digit 0-9.")
            continue

        kit, group = GROUPS[group_name]
        change_number(kit, group, number)
        print(f"  ? {group_name} set to {number}")

if __name__ == "__main__":
    main()
