import Functions
import Motors
import State
import Roboter
from pybricks.tools import wait
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop

def enum(**enums: int):
    return type('Enum', (), enums)

GameState = enum(CALIBRATION=0, FIRSTBLOCKS_PICKUP=1, FIRSTBLOCKS_READCOLOURS=2, DEAD=3, TEST=4, MOVETOFIRSTBLOCKS=5, FIRSTBLOCKS_PUTYELLOW=6)
state = GameState.CALIBRATION
# state = GameState.TEST

def gameRoutine():

    global GameState
    global state

    if state == GameState.TEST:
        # Roboter.driveBase.turn(-360)
        state = GameState.DEAD
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
        Roboter.driveBase.straight(38) # Mit schwachem Akku 37, aufgeladen 36
        state=GameState.FIRSTBLOCKS_PICKUP
        return

    elif state == GameState.FIRSTBLOCKS_PICKUP:
        Motors.pickup_motor.dc(-50)
        Functions.pickUpBlocks()
        
        for i in range(2):
            Functions.driveForwardToBlockAndPickUp(100, 1)
        Functions.driveForwardToBlockAndPickUp(100, 1, 13)
        wait(1000)
        Motors.pickup_motor.hold()
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

        state=GameState.FIRSTBLOCKS_READCOLOURS
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