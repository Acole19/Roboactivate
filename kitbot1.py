import RoboPiLib as RPL
import setup
RPL.digitalWrite(18,1)
RPL.servowrite(1,0)
RPL.servowrite(0,0)
turn_left = rpl.servowrite(1,1000)
if rpl.readDistance(1) > 30:
    RPL.servowrite(1,1000)
