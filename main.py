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
    start_playback(events)
    
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def start_playback(playback_events):
    print("this workin?")
    play_sound("voice.mp3")
    for event in playback_events:
        print("outputting")
        GPIO.output(event[0],True)
        time.sleep(event[1])
        GPIO.output(event[0],False)
    print("Cleaning up/turning off all LEDS.")
    GPIO.cleanup()
    
        
# define all LEDs
LED1 = 7
LED2 = 8
LED3 = 11
LED4 = 12
LED5 = 13
LED6 = 15 
LED7 = 16 
LED8 = 18

juan_water = 7
juan_fight = 8 
juan_look = 18
juan_marry = 16

keyon_water = 11
keyon_fight = 12
keyon_look = 13 
keyon_marry = 15



events = [
    (juan_marry,2.25),
    (keyon_marry,3),
    (keyon_fight,3),
    (juan_fight,3),
    (juan_water,4),
    (keyon_water,5),
    (keyon_look,2),
    (juan_look,2),
    (keyon_look,5)]
    
button = 10

allLEDs = [LED1,LED2,LED3,LED4,LED5,LED6,LED7,LED8]

# set up GPIO module
GPIO.setmode(GPIO.BOARD)

# set up pygame audio player
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

for LED in allLEDs:
    GPIO.setup(LED, GPIO.OUT)
print("LED setup complete!")

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button,GPIO.RISING,callback=button_callback)
print("Button setup complete!")

print("Current button state:",GPIO.input(button))
#runLEDsInSequence(allLEDs)
while True:
    pass
#start_playback(events)


