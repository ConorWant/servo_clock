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
          
def one(kit):
    channels = [1, 2]
    servo_on(kit, channels)
        
def two(kit):
    channels = [0, 1, 3, 4, 6]
    servo_on(kit, channels)
    
def three(kit):
    channels = [0, 1, 2, 3, 6]
    servo_on(kit, channels) 
       
def four(kit):
    channels = [1, 2, 5, 6]
    servo_on(kit, channels)
        
def five(kit):
    channels = [0, 2, 3, 5, 6]
    servo_on(kit, channels)
       
def six(kit):
    channels = [0, 2, 3, 4, 5, 6]
    servo_on(kit, channels)
        
def seven(kit):
    channels = [0, 1, 2]
    servo_on(kit, channels)
        
def eight(kit):
    channels = [0, 1, 2, 3, 4, 5, 6]
    servo_on(kit, channels)
    
def nine(kit):
    channels = [0, 1, 2, 3, 5, 6]
    servo_on(kit, channels)
       
def zero(kit):
    channels = [0, 1, 2, 3, 4, 5]
    servo_on(kit, channels)
            
def main():
    kit1 = ServoKit(channels=16, address=0x40)
    kit2 = ServoKit(channels=16, address=0x41)
    
    for ch in BOARD1_CHANNELS:
        kit1.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
    for ch in BOARD2_CHANNELS:
        kit2.servo[ch].set_pulse_width_range(PULSE_MIN, PULSE_MAX)
        
    servo_off(kit2, GROUP1)
    
    
    NUMBERS = {
        "0": zero,
        "1": one,
        "2": two,
        "3": three,
        "4": four,
        "5": five,
        "6": six,
        "7": seven,
        "8": eight,
        "9": nine,
    }

    while True:
        user_input = input("Type a number: ")

        if user_input.lower() == "q":
            break
        elif user_input in NUMBERS:
            servo_off(kit2, GROUP1)
            NUMBERS[user_input](kit2)

        else:
            servo_off(kit2, GROUP1)
                

            
if __name__ == "__main__":
    main()
