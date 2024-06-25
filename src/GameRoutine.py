import Functions
import Motors
import State
import Roboter
from pybricks.tools import wait
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop

def enum(**enums: int):
    return type('Enum', (), enums)

GameState = enum(CALIBRATION=0, FIRSTBLOCKS_PICKUP=1, FIRSTBLOCKS_READCOLOURS=2, DEAD=3, TEST=4, MOVETOFIRSTBLOCKS=5, FIRSTBLOCKS_PUTYELLOW=6, MOVETOSECONDBLOCKS=7, SECONDBLOCKS_PICKUPRED=8, SECONDBLOCKS_PUTRED=9, DRIVETOOTHERFIELD=10)
# state = GameState.CALIBRATION
state = GameState.DRIVETOOTHERFIELD

def gameRoutine():

    global GameState
    global state

    if state == GameState.DRIVETOOTHERFIELD:
        Functions.moveCarrier(20)
        Roboter.driveBase.turn(-35)
        Roboter.driveBase.settings(straight_acceleration=800, straight_speed=800)
        Roboter.driveBase.straight(-1350)
        Roboter.driveBase.turn(35)
        Roboter.driveBase.straight(150)
        state = GameState.CALIBRATION
        return

    if state == GameState.CALIBRATION:
        Functions.moveCarrier(20)
        Functions.calibrateHolder()
        # Functions.calibrateCarrier()
        state=GameState.MOVETOFIRSTBLOCKS
        return
    
    elif state == GameState.MOVETOFIRSTBLOCKS:
        Functions.driveFromStartingPositionToWall()
        Functions.moveCarrier(20)
        Functions.driveUntilColor(Color.RED)
        Roboter.driveBase.straight(38) # Mit schwachem Akku 38, aufgeladen 37
        state=GameState.FIRSTBLOCKS_PICKUP
        return

    elif state == GameState.FIRSTBLOCKS_PICKUP:
        Motors.pickup_motor.dc(Roboter.holdDutyCycle)
        Functions.pickUpBlocks(downDuty=40)
        
        for i in range(2):
            Functions.driveForwardToBlockAndPickUp(100, 1)
        Functions.driveForwardToBlockAndPickUp(100, 1, 13)
        wait(1000)
        # Motors.pickup_motor.hold()
        state=GameState.FIRSTBLOCKS_PUTYELLOW
        return
    
    elif state == GameState.FIRSTBLOCKS_PUTYELLOW:
        # We picked up the first 4 blocks and now want to bring the two yellow ones to the middle.
        Roboter.driveBase.turn(-90)
        # Maybe wait "So long bis da Roboter de scheiß Wand berührt"
        Roboter.driveBase.straight(250)
        Roboter.driveBase.turn(-90)
        Roboter.driveBase.straight(115)
        Roboter.driveBase.turn(90)
        Roboter.driveBase.straight(175)

        Functions.releaseBlocks(2)
        Roboter.driveBase.straight(-150)
        Functions.moveCarrierToAbsolutePosition(15)

        state=GameState.MOVETOSECONDBLOCKS
        return
    
    elif state == GameState.MOVETOSECONDBLOCKS:
        Motors.pickup_motor.dc(Roboter.holdDutyCycle)
        Roboter.driveBase.turn(-135)
        Roboter.driveBase.straight(-950)
        Roboter.driveBase.turn(45)
        Roboter.driveBase.straight(100)
        Functions.driveFromStartingPositionToWall()
        Functions.moveCarrier(50)
        Functions.driveUntilColor(Color.RED)
        # Auf dieser Seite ist der Abstand von der roten Außenline zum roten Block etwas größer. Um 1-2 mm
        Roboter.driveBase.straight(39)
        state=GameState.SECONDBLOCKS_PICKUPRED
        return
    
    elif state == GameState.SECONDBLOCKS_PICKUPRED:
        Motors.pickup_motor.dc(Roboter.holdDutyCycle)
        Functions.pickUpBlocks(downDuty=40)
        Functions.driveForwardToBlockAndPickUp(100, 1, 13)
        wait(1000)
        Motors.pickup_motor.hold()
        state=GameState.SECONDBLOCKS_PUTRED
        return
    
    elif state == GameState.SECONDBLOCKS_PUTRED:
        # We picked up the first 4 blocks and now want to bring the two yellow ones to the middle.
        Roboter.driveBase.turn(-90)
        # Maybe wait "So long bis da Roboter de scheiß Wand berührt"
        Roboter.driveBase.straight(300)
        Roboter.driveBase.turn(90)
        Roboter.driveBase.straight(100)
        Functions.driveUntilColor(Color.NONE, speed=50)
        Functions.driveUntilColor(Color.RED)
        Roboter.driveBase.straight(120)
        Roboter.driveBase.turn(-90)
        Roboter.driveBase.straight(120)

        Functions.releaseBlocks(4)
        Roboter.driveBase.straight(-150)
        Functions.moveCarrierToAbsolutePosition(15)

        # Trümmerteil

        Roboter.driveBase.turn(45)
        Roboter.driveBase.settings(straight_acceleration=400, straight_speed=800)
        Roboter.driveBase.straight(800)

        state=GameState.DEAD
        return

    
    elif state == GameState.FIRSTBLOCKS_READCOLOURS:
        # Drive left so that we stand in line with the green / blue blocks with the colour sensor
        # start driving at a defined speed asyncronally
        # start reading colour sensor and determain if we see the green/blue ground or the blocks.
        # Possible options: 
        # Blue Green Brown Blue Green -> no blocks
        # Blue Brown Blue -> two blocks
        # Blue Green Brown Green -> 1 block at 2nd position


        return 

    return