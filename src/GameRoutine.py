import Functions
import Motor
import State

def enum(**enums: int):
    return type('Enum', (), enums)

GameState = enum(CALIBRATION=0, TWO=2, THREE=3)


def gameRoutine():
    state = GameState.CALIBRATION

    if state == GameState.CALIBRATION:
            Functions.calibrateHolder()
            Functions.calibrateCarrier()

    return 0