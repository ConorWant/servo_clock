from adafruit_servokit import ServoKit

BOARD1_CHANNELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
BOARD2_CHANNELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
PULSE_MIN = 500
PULSE_MAX = 2500
GROUP1 = list(range(0, 7))
GROUP2 = list(range(7, 14))


def servo_on(kit, group):
    for ch in group:
        kit.servo[ch].angle = 180

def servo_off(kit, group):
    for ch in group:
        kit.servo[ch].angle = 120  

        
def main():
    kit1 = ServoKit(channels=16, address=0x40)
    kit2 = ServoKit(channels=16, address=0x41)
    
    for ch in BOARD1_CHANNELS:
        kit1.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
    for ch in BOARD2_CHANNELS:
        kit2.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
        
    servo_off(kit2, GROUP1)
    servo_state = 0
    
    while True:
        user_input = input("Type to move the servo: ")
        
        if user_input.lower() == "q":
            break
        elif servo_state == 0: 
            servo_on(kit2, GROUP1)
            servo_state = 1
        else:
            servo_off(kit2, GROUP1)
            servo_state = 0

        
if __name__ == "__main__":
    main()
