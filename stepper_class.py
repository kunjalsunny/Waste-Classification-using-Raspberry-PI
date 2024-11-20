import RPi.GPIO as GPIO
import time

class Stepper:
    def __init__(self, pins, direction, ms, steps):
        self.pins = pins
        self.direction = direction
        self.ms = ms
        self.steps = steps
        self.CCWStep = (0x01, 0x02, 0x04, 0x08)
        self.CWStep = (0x08, 0x04, 0x02, 0x01)
#         GPIO.setmode(GPIO.BOARD)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)        
        
    
#     CW, CCW rotation
    def cwRotation(self):
        for j in range(0,4,1):      # cycle for power supply order
            for i in range(0,4,1):
                GPIO.output(self.pins[i],((self.CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        
    def ccwRotation(self):
        for j in range(0,4,1):      # cycle for power supply order
            for i in range(0,4,1):
                GPIO.output(self.pins[i],((self.CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        
    # as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
    def moveOnePeriod(self):   
          # assign to each pin
            if (self.direction == 1):# power supply order clockwise
                self.cwRotation()
            else :              # power supply order anticlockwise
                self.ccwRotation()
                
            if(self.ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
                self.ms = 3
            time.sleep(self.ms*0.001)
        
# continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle
    def moveSteps(self):
        for i in range(self.steps):
            self.moveOnePeriod()
    
# function used to stop motor
    def motorStop(self):
        for i in range(0,4,1):
            GPIO.output(self.pins[i],GPIO.LOW)
        
    def drop(self):
        if self.direction == 1:
            print('Rotating...')
            self.cwRotation()
            time.sleep(5)
            self.ccwRotation()
        else:
            print('Rotating...')
            self.ccwRotation()
            time.sleep(5)
            self.cwRotation()

    def destroy(self):
        for pin in self.pins:
            GPIO.cleanup(pin)