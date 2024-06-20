import Functions
import Motors
import State
import Main

def enum(**enums: int):
    return type('Enum', (), enums)

GameState = enum(CALIBRATION=0, FIRSTBLOCKS_PICKUP=1, FIRSTBLOCKS_READCOLOURS=2)


def gameRoutine():
    state = GameState.CALIBRATION

    if state == GameState.CALIBRATION:
        Functions.calibrateHolder()
        Functions.calibrateCarrier()
        Functions.moveCarrier(10)
        state=GameState.FIRSTBLOCKS_PICKUP
        return

    elif state == GameState.FIRSTBLOCKS_PICKUP:
        # TODO: Move so we can drive straight at the blocks
        Main.driveBase.curve(500, 20)
        Functions.driveForwardToBlockAndPickUp(50, 1)
        for i in range(3):
            Functions.driveForwardToBlockAndPickUp(50, 1)
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

    return 0