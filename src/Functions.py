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
    degressPerHeightFactor = 12 # 12 degress / mm

    rotationAngle = degressPerHeightFactor * heightToMove

    Motors.carrier_motor.run_angle(+750, rotationAngle, Stop.HOLD)
    
    State.carrierHight += heightToMove

    return

def moveCarrierByBlocks(blocksToMove, factor=36):
    moveCarrier(blocksToMove*factor)
    return

# Carrier is above the blocks and should pick them up
def pickUpBlocks(up = 23, downDuty=10):
    # Motors.pickup_motor.stop()
    Motors.pickup_motor.dc(downDuty)
    moveCarrier(-State.carrierHight)
    Motors.pickup_motor.dc(Roboter.holdDutyCycle)
    wait(500)
    moveCarrier(up)
    return

def driveForwardToBlockAndPickUp(distance, numOfBlocks, up=23):
    moveCarrierByBlocks(numOfBlocks)
    Roboter.driveBase.straight(distance)
    pickUpBlocks(up)
    return

def waitUntilColor(color):
    while Roboter.bottomSensor.color() != color:
        wait(5)

def waitUntilHSVInRange(hLowerBound, hUpperBound, sLowerBound):
    while Roboter.bottomSensor.hsv().h < hLowerBound or Roboter.bottomSensor.hsv().h > hUpperBound and Roboter.bottomSensor.hsv().s < sLowerBound:
        wait(5)
    print("Stopped at color: " + str(Roboter.bottomSensor.hsv()))

def waitUntilColor(color):
    while Roboter.bottomSensor.color() != color:
        wait(5)
    print("Stopped at color: " + str(Roboter.bottomSensor.hsv()))

def driveUntilColor(color, speed=50):
    Roboter.driveBase.drive(speed,0)
    while Roboter.bottomSensor.color() != color:
        wait(5)
    print("Stopped at color: " + str(Roboter.bottomSensor.hsv()))
    Roboter.driveBase.stop()
    waitUntilDriveBaseDone()

 

def driveFromStartingPositionToWall():
    oldSettings = setHighSpeed()
    Roboter.driveBase.turn(-20)
    Roboter.driveBase.straight(-200)
    Motors.left_motor.dc(-40)
    Motors.right_motor.dc(-50)
    wait(600)
    Motors.left_motor.dc(50)
    Motors.right_motor.dc(40)
    wait(1500)
    Motors.left_motor.dc(-45)
    Motors.right_motor.dc(-40)
    wait(1000)
    Motors.left_motor.dc(40)
    Motors.right_motor.dc(30)
    wait(400)
    waitUntilColor(Color.WHITE)
    Motors.left_motor.stop()
    Motors.right_motor.stop()
    setNormalSpeed(oldSettings)

def waitUntilDriveBaseDone():
    while(Roboter.driveBase.state()[1]>5):
        wait(10)

def releaseBlocks(countOfBlocks):
    Motors.pickup_motor.dc(100)
    wait(200)
    Motors.pickup_motor.hold()
    # moveCarrierByBlocks(countOfBlocks, 33)
    moveCarrierToAbsolutePosition(countOfBlocks*33+5)
    Motors.pickup_motor.dc(-100)
    wait(200)
    Motors.pickup_motor.hold()
    moveCarrier(10)

def moveCarrierToAbsolutePosition(position):
    moveCarrier(position-State.carrierHight)

def activelyHoldBlocks():
    Motors.pickup_motor.dc(Roboter.holdDutyCycle)

def setHighSpeed():
    oldSettings = Roboter.driveBase.settings()
    Roboter.driveBase.settings(straight_acceleration=800, straight_speed=400)
    return oldSettings

def setNormalSpeed(oldSettings):
    Roboter.driveBase.settings(oldSettings[0], 100, oldSettings[2], oldSettings[3])
