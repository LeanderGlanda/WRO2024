import Motors
import State
import Roboter
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait

def calibrateHolder():
    # Motors.carrier_motor.run_time(-1000, 1000, Stop.HOLD, True)
    Motors.pickup_motor.run_until_stalled(-1000, Stop.HOLD, 80)
    State.holderOpenAngle = 0
    Motors.pickup_motor.reset_angle(0)
    return

def calibrateCarrier():
    # Letting the carrier fall down doesn't work. This is useless
    Motors.carrier_motor.run_time(-1000, 1000, Stop.HOLD, True)
    Motors.carrier_motor.stop()
    wait(100) # Leave time so the carrier falls to the ground
    State.carrierHight = 0
    Motors.carrier_motor.reset_angle(0)
    Motors.carrier_motor.hold()
    return

def moveCarrier(heightToMove):
    degressPerHeightFactor = 34 # 34 degress / mm

    rotationAngle = degressPerHeightFactor * heightToMove

    Motors.carrier_motor.run_angle(-1000, rotationAngle, Stop.HOLD)
    
    State.carrierHight += heightToMove

    return

def moveCarrierByBlocks(blocksToMove):
    moveCarrier(blocksToMove*31)
    return

# Carrier is above the blocks and should pick them up
def pickUpBlocks():
    moveCarrier(-State.carrierHight)
    moveCarrier(20)
    return

def driveForwardToBlockAndPickUp(distance, numOfBlocks):
    moveCarrierByBlocks(numOfBlocks)
    Roboter.driveBase.straight(distance)
    pickUpBlocks()
    return