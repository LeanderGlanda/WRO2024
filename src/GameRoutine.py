from enum import Enum
import Roboter.Functions
import Roboter.Motor
import Roboter.State

class GameState(Enum):
    CALIBRATION = 0


def gameRoutine():

    state = GameState.CALIBRATION

    match state:
        case GameState.CALIBRATION:
            Roboter.Functions.calibrateHolder()
            Roboter.Functions.calibrateCarrier()

    return 0

