import Functions
import Motors
import State
import Roboter
from pybricks.tools import wait
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop

def enum(**enums: int):
    return type('Enum', (), enums)

GameState = enum(CALIBRATION=0, FIRSTBLOCKS_PICKUP=1, FIRSTBLOCKS_READCOLOURS=2, DEAD=3, TEST=4, MOVETOFIRSTBLOCKS=5)
state = GameState.CALIBRATION

def gameRoutine():

    global GameState
    global state

    if state == GameState.TEST:
        # Functions.calibrateHolder()
        # Roboter.driveBase.curve(-200, -180)
        Roboter.driveBase.straight(-500)
        state = GameState.DEAD
        return

    if state == GameState.CALIBRATION:
        Functions.moveCarrier(20)
        Functions.calibrateHolder()
        # Functions.calibrateCarrier()
        # wait(1000000)
        state=GameState.MOVETOFIRSTBLOCKS
        return
    
    elif state == GameState.MOVETOFIRSTBLOCKS:
        Roboter.driveBase.turn(-50)
        Roboter.driveBase.straight(115)
        Roboter.driveBase.turn(70, Stop.COAST)
        Functions.moveCarrierByBlocks(1)
        Roboter.driveBase.straight(-252, Stop.COAST)
        # Roboter.driveBase.turn(-5, Stop.HOLD)
        state=GameState.FIRSTBLOCKS_PICKUP
        # state=GameState.DEAD
        return

    elif state == GameState.FIRSTBLOCKS_PICKUP:
        # Roboter.driveBase.curve(500, 20) # This probably doesn't work out
        # Functions.driveForwardToBlockAndPickUp(-100, 1)
        Functions.pickUpBlocks()
        for i in range(3):
            Functions.driveForwardToBlockAndPickUp(-100, 1)
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