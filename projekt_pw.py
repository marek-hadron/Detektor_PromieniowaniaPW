import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

resistorPin = 7

while True:
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    
    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff  = time.time() - currentTime
        
    print(diff * 1000)
    time.sleep(1)

    if(diff*1000<500):

	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
	GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

 	GPIO.output(11, GPIO.HIGH) # Turn on
 	time.sleep(1) # Sleep for 1 second
 	GPIO.output(11, GPIO.LOW) # Turn off
	time.sleep(1) # Sleep for 1 second
