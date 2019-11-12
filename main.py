import RPi.GPIO as GPIO
import time
import pygame

def runLEDs(LEDs,sleep_time):
    print("Turning on LEDS.")
    for i in LEDs:
        GPIO.output(i,True)
    time.sleep(sleep_time)
    
def runLEDsInSequence(LEDs):
    sleep_time = 1
    for i in LEDs:
        GPIO.output(i,True)
        # play sound
        time.sleep(sleep_time)
        GPIO.output(i,False)
    
def button_callback(channel):
    print("Button was pushed!")
    
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("pygame mixer:",pygame.mixer.get_busy())
    while pygame.mixer.get_busy() == 0:
        pass

# define all LEDs
LED1 = 7
LED2 = 11
LED3 = 12
LED4 = 13
LED5 = 15
LED6 = 16 #unsure of port
LED7 = 18 #unsure of port
LED8 = -1 #unsure of port

events = [
    (LED1,2),
    (LED2,2),
    (LED3,2),
    (LED4,2),
    (LED5,2),
    (LED6,2),
    (LED7,2),
    (LED8,2)]
    
button = 10

allLEDs = [LED1,LED2,LED3,LED4,LED5]

# set up GPIO module
GPIO.setmode(GPIO.BOARD)

# set up pygame audio player
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
play_sound("voice.mp3")

for LED in allLEDs:
    GPIO.setup(LED, GPIO.OUT)
print("LED setup complete!")

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button,GPIO.RISING,callback=button_callback)
print("Button setup complete!")

print("Current button state:",GPIO.input(button))
runLEDsInSequence(allLEDs)

print("Cleaning up/turning off all LEDS.")
GPIO.cleanup()

