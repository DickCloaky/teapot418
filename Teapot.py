#
# Gertbot testing - requires python3?  Hope this is OK with the other bits...
#
import time
# the Gertbot drivers
import gertbot as gb
import UltraBorg3 as UltraBorg


# Forwards and backwards are the same for left and right
#all my motors move clockwise when set to FORWD
# The trick is to reverse the motor connections for one  :-) 
RAMP  = gb.RAMP_010 # ramp speed=0.1 seconds
FORWD = gb.MOVE_A
BACKW = gb.MOVE_B
STOP  = gb.MOVE_STOP

class Teapot(object):
# This is for the development environment:
    BOARD = 3           # Which board we talk to 
    MOTORA = 1
    MOTORB = 3 
    MOTORC = 0

    def __init__(self):
#        print('open_uart')
        gb.open_uart(0)

# Setup the channels for brushed motors
        gb.set_mode(self.BOARD,self.MOTORA,gb.MODE_BRUSH)
        gb.set_mode(self.BOARD,self.MOTORB,gb.MODE_BRUSH)
        gb.set_mode(self.BOARD,self.MOTORC,gb.MODE_BRUSH)
# set a ramp-up speed in case motors are big
        gb.set_brush_ramps(self.BOARD,self.MOTORA, RAMP,RAMP,0);
        gb.set_brush_ramps(self.BOARD,self.MOTORB, RAMP,RAMP,0);
        gb.set_brush_ramps(self.BOARD,self.MOTORC, RAMP,RAMP,0);

# initialise the ultraborg
        self.ub = UltraBorg.UltraBorg()
        self.ub.Init()
        time.sleep(0.5) # because that is what the docs say?
#variables for the golf ball catcher
        self.caddyservoincrement = 0.1 # how far we move with each button press
        self.ubposition4 = 0.0
        self.ub.SetServoPosition4(self.ubposition4) # this is where we attach the golf ball catcher

        self.ub.SetServoPosition1(0.0) # this is where we attach the nerf gun

# self.direction = true to drive with the spout forwards
# self.direction = false to drive with the spout at the back
        self.direction = True 

    def fire(self):
        '''use the servo to pull the nerf gun trigger'''
        self.ub.SetServoPosition1(0.4)
        time.sleep(0.5)
        self.ub.SetServoPosition1(0.0)

    def toggle(self):
        '''change the driving direction'''
        if self.direction:
            self.direction = False
        else:
            self.direction = True
#        print("drive with the spout at the front: %r"%self.direction)

    def catcher_up(self):
        self.ubposition4 -= self.caddyservoincrement
        if self.ubposition4 < -1.0:
            self.ubposition4 = -1.0
        self.ub.SetServoPosition4(self.ubposition4)

    def catcher_down(self):
        self.ubposition4 += self.caddyservoincrement
        if self.ubposition4 > 1.0:
            self.ubposition4 = 1.0
        self.ub.SetServoPosition4(self.ubposition4)

    def forwards(self):
        if self.direction:
            self._forwards()
        else:
            self._backwards()

    def backwards(self):
        if self.direction:
            self._backwards()
        else:
            self._forwards()

    def _forwards(self):
#        print('teapot.forwards')
        gb.move_brushed(self.BOARD,self.MOTORA,STOP)
        gb.move_brushed(self.BOARD,self.MOTORB,FORWD)
        gb.move_brushed(self.BOARD,self.MOTORC,BACKW)

    def _backwards(self):
        gb.move_brushed(self.BOARD,self.MOTORA,STOP)
        gb.move_brushed(self.BOARD,self.MOTORB,BACKW)
        gb.move_brushed(self.BOARD,self.MOTORC,FORWD)

    def right(self):
        if self.direction:
            self._right()
        else:
            self._left()

    def left(self):
        if self.direction:
            self._left()
        else:
            self._right()

    def _right(self):
#really need A to be a bit slower than B? but this is actually not bad as is...
        gb.move_brushed(self.BOARD,self.MOTORA,BACKW)
        gb.move_brushed(self.BOARD,self.MOTORB,FORWD)
        gb.move_brushed(self.BOARD,self.MOTORC,STOP)

    def _left(self):
#need A to be slower than B?
        gb.move_brushed(self.BOARD,self.MOTORA,FORWD)
        gb.move_brushed(self.BOARD,self.MOTORB,STOP)
        gb.move_brushed(self.BOARD,self.MOTORC,BACKW)

    def anticlockwise(self):
        if self.direction:
            self._anticlockwise()
        else:
            self._clockwise()

    def clockwise(self):
        if self.direction:
            self._clockwise()
        else:
            self._anticlockwise()

    def _anticlockwise(self):
        gb.move_brushed(self.BOARD,self.MOTORA,FORWD)
        gb.move_brushed(self.BOARD,self.MOTORB,FORWD)
        gb.move_brushed(self.BOARD,self.MOTORC,FORWD)

    def _clockwise(self):
        gb.move_brushed(self.BOARD,self.MOTORA,BACKW)
        gb.move_brushed(self.BOARD,self.MOTORB,BACKW)
        gb.move_brushed(self.BOARD,self.MOTORC,BACKW)

    def stop(self):
        gb.move_brushed(self.BOARD,self.MOTORA,STOP)
        gb.move_brushed(self.BOARD,self.MOTORB,STOP)
        gb.move_brushed(self.BOARD,self.MOTORC,STOP)

    def move(self, motor, what):
        gb.move_brushed(self.BOARD, motor, what)

    def speed(self, percent):
#        print('setting speed to %d'%percent)
        gb.pwm_brushed(self.BOARD,self.MOTORA,5000,percent)
        gb.pwm_brushed(self.BOARD,self.MOTORB,5000,percent)
        gb.pwm_brushed(self.BOARD,self.MOTORC,5000,percent)

    @property
    def sensorF(self):
        return self.ub.GetDistance1()

    @property
    def sensorL(self):
        return self.ub.GetDistance2()

    @property
    def sensorR(self):
        return self.ub.GetDistance3()

    def pwm_brushed(self, motor, percent):
        gb.pwm_brushed(self.BOARD,motor,5000,percent)

