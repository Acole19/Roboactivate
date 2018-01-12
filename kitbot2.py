import RoboPiLib as RPL
import time
def cease():
    exit(0)
RPL.RoboPiInit("/dev/ttyAMA0",115200)
RPL.digitalWrite(18,1)
RPL.digitalWrite(20,0)
RPL.servoWrite(1,0)
RPL.servoWrite(0,0)
def stop():
    RPL.servoWrite(0,0)
    RPL.servoWrite(1,0)
def hard_turn_left():
    RPL.servoWrite(0,1500)
def turn_left():
    RPL.servoWrite(0,1000)
def turn_right():
    RPL.servoWrite(1,1000)
def hard_turn_right():
    RPL.ServoWrite(1,1500)
print "Input command"
command = raw_input("> ")
if command == "Initialize":
    while True:
        if RPL.readDistance(1) < 30:
            turn_left()
            start_time = time.time()
            if time.time - start_time > 3 and RPL.readDistance(1) < 30:
                cease()
        elif readDistance(0) < 30:
            turn_right()
            start_time=time.time()
            if time.time - start_time > 3 and RPL.readDistance(1) < 30:
                cease()

        else:
            turn_left()
            turn_right()
            halt = raw_input("> ")
            if halt == "Halt":
                cease()
