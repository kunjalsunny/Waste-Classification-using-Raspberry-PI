import RPi.GPIO as GPIO
import time

class Proximity:
    
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
        GPIO.input(self.pin)
    # Set up GPIO

    def ready(self):
        
        print('Ready...')
        time.sleep(1)
        print('\nDrop now!')
    
    def detected(self, callback):
        print('Object detected')
        callback()
    
    def loop(self):
        if GPIO.input(self.pin):
            print('Hello World!')
            while GPIO.input(self.pin):
                time.sleep(0.1)
        else:
            print('Object detected')

    def destroy(self):
        GPIO.cleanup(self.pin)