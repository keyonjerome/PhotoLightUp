import RPi.GPIO as GPIO
import time

def runLEDS(LEDs,sleep_time):
    print("Turning on LEDS.")
    for i in LEDs:
        GPIO.output(i,True)
    time.sleep(sleep_time)

LED1 = 7
LED2 = 11

LED3 = 12
LED4 = 13

LED5 = 15
LED6 = 16

LED7 = 18

allLEDs = [LED1,LED2,LED3,LED4,LED5]

GPIO.setmode(GPIO.BOARD)

for LED in allLEDs:
    GPIO.setup(LED, GPIO.OUT)
print("LED setup complete!")

runLEDS(allLEDs,5)
print("Cleaning up/turning off all LEDS.")
GPIO.cleanup()

#GPIO.output(7, True)
#print("outputting")
#time.sleep(5)
#print("ending output")
#GPIO.output(7, False)
