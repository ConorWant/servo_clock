from adafruit_servokit import ServoKit

CHANNELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
PULSE_MIN = 500
PULSE_MAX = 2500


def move_servos(kit, channels, angle):
    for ch in channels:
        kit.servo[ch].angle = angle
        
def get_angle():
    user_input = input("Enter an angle between 0 and 180 (q to quit): ")
    
    if user_input.lower() == "q":
        return None
    try:
        angle = float(user_input)
        if not 0 <= angle <= 180:
            print("Angle must be between 0 and 180")
            return get_angle()
        return angle
    except ValueError:
        print("Invalid input, enter an angle between 0 and 180 (q to quit)")
        
def main():
    kit = ServoKit(channels=16)
    for ch in CHANNELS:
        kit.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
    
    while True:
        angle = get_angle()
        
        if angle == None:
            print("Thank you, Bye!")
            break
        
        move_servos(kit, CHANNELS, angle)
        
if __name__ == "__main__":
    main()