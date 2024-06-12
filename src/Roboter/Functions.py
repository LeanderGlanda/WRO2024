import Roboter.Functions
import Roboter.Motor
import Roboter.State
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop

def calibrateHolder():
    Roboter.Motor.carrier_motor.run_time(-1000, 1000, Stop.HOLD, True)
    Roboter.Motor.pickup_motor.run_until_stalled(-1000, Stop.HOLD, 80)
    Roboter.State.holderOpenAngle = 0
    return

def calibrateCarrier():

    Roboter.Motor.carrier_motor.run_time(-1000, 1000, Stop.HOLD, True)
    Roboter.Motor.carrier_motor.stop()
    Roboter.State.carrierHight = 0
    Roboter.Motor.carrier_motor.hold()
    return