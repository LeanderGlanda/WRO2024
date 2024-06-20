import Functions
import Motor
import State
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop

def calibrateHolder():
    Motor.carrier_motor.run_time(-1000, 1000, Stop.HOLD, True)
    Motor.pickup_motor.run_until_stalled(-1000, Stop.HOLD, 80)
    State.holderOpenAngle = 0
    return

def calibrateCarrier():

    Motor.carrier_motor.run_time(-1000, 1000, Stop.HOLD, True)
    Motor.carrier_motor.stop()
    State.carrierHight = 0
    Motor.carrier_motor.hold()
    return