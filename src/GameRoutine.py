import Functions
import Motors
import State
import Roboter
from pybricks.tools import wait
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop

def enum(**enums: int):
    return type('Enum', (), enums)

GameState = enum(CALIBRATION=0, FIRSTBLOCKS_PICKUP=1, FIRSTBLOCKS_READCOLOURS=2, DEAD=3, TEST=4, MOVETOFIRSTBLOCKS=5, FIRSTBLOCKS_PUTYELLOW=6, MOVETOSECONDBLOCKS=7, SECONDBLOCKS_PICKUPRED=8, SECONDBLOCKS_PUTRED=9, DRIVETOOTHERFIELD=10, BRINGTRASHTOAREA=11, TREE=12)
# state = GameState.MOVETOFIRSTBLOCKS
state = GameState.DRIVETOOTHERFIELD
# state = GameState.TEST

def gameRoutine():

    global GameState
    global state

    if state == GameState.TEST:
        Roboter.driveBase.drive(50, 0)
        print("Color: " + str(Roboter.bottomSensor.hsv()))
        wait(200)
        return

    if state == GameState.DRIVETOOTHERFIELD:
        Functions.moveCarrier(20)
        Roboter.driveBase.turn(-40)
        Roboter.driveBase.settings(straight_acceleration=800, straight_speed=800)
        Roboter.driveBase.straight(-1310)
        Roboter.driveBase.turn(40)
        Roboter.driveBase.straight(150)
        state = GameState.CALIBRATION
        return

    if state == GameState.CALIBRATION:
        Functions.moveCarrierToAbsolutePosition(40)
        Functions.calibrateHolder()
        # Functions.calibrateCarrier()
        state=GameState.MOVETOFIRSTBLOCKS
        return
    
    elif state == GameState.MOVETOFIRSTBLOCKS:
        Functions.driveFromStartingPositionToWall()
        # Functions.driveUntilColor(Color.RED)
        Roboter.driveBase.drive(50,0)
        Functions.waitUntilHSVInRange(335, 345, 35)
        Roboter.driveBase.stop()
        Functions.waitUntilDriveBaseDone()
        Roboter.driveBase.straight(51) # Mit schwachem Akku 38, aufgeladen 37 -> eventuell, 38 ist eigentlich eher korrekt auch aufgeladen
        state=GameState.FIRSTBLOCKS_PICKUP
        return

    elif state == GameState.FIRSTBLOCKS_PICKUP:
        Functions.activelyHoldBlocks()

        # Picking up the first block requires a lot of force, as the holder needs to be wideend
        Functions.pickUpBlocks(downDuty=40)
        
        for i in range(2):
            Functions.driveForwardToBlockAndPickUp(100, 1)
        Functions.driveForwardToBlockAndPickUp(100, 1, 13)

        # This wait may be unnecessary
        wait(1000)
        state=GameState.FIRSTBLOCKS_PUTYELLOW
        return
    
    elif state == GameState.FIRSTBLOCKS_PUTYELLOW:
        # We picked up the first 4 blocks and now want to bring the two yellow ones to the middle.
        Roboter.driveBase.turn(-90)
        # Maybe wait "So long bis da Roboter de scheiß Wand berührt"
        # We could defenitely accelerate here and drive in an angle
        # Maybe this works:
        oldSettings = Functions.setHighSpeed()
        Roboter.driveBase.straight(50)
        Roboter.driveBase.turn(-23)
        Roboter.driveBase.straight(326)
        Roboter.driveBase.turn(23)
        Roboter.driveBase.straight(75) # Calculated 80 but could be too far because of rounding.
        Functions.setNormalSpeed(oldSettings)

        # Otherwise: This works:
        # Roboter.driveBase.straight(250)
        # Roboter.driveBase.turn(-90)
        # Roboter.driveBase.straight(115)
        # Roboter.driveBase.turn(90)
        # Roboter.driveBase.straight(175)

        Functions.releaseBlocks(2)
        Functions.activelyHoldBlocks()
        Roboter.driveBase.straight(-150)
        Functions.moveCarrierToAbsolutePosition(15)

        state=GameState.MOVETOSECONDBLOCKS
        return
    
    elif state == GameState.MOVETOSECONDBLOCKS:
        Roboter.driveBase.turn(-135)
        oldSettings = Functions.setHighSpeed()
        Roboter.driveBase.straight(-935)
        Roboter.driveBase.turn(45)
        Roboter.driveBase.straight(100)
        Functions.setNormalSpeed(oldSettings)

        # Now we are at the second starting position, just drive the same manuver as at the start of the game to the wall
        Functions.driveFromStartingPositionToWall()
        Functions.pickUpBlocks()
        Functions.moveCarrier(50)
        # Functions.driveUntilColor(Color.RED)
        Roboter.driveBase.drive(50,0)
        Functions.waitUntilHSVInRange(345, 360, 20)
        print("Stopped at color: " + str(Roboter.bottomSensor.hsv()))
        Roboter.driveBase.stop()
        Functions.waitUntilDriveBaseDone()
        # On this side the distance from the red outline to the block outline is 1-2mm larger than on the other side.
        Roboter.driveBase.straight(49)
        state=GameState.SECONDBLOCKS_PICKUPRED
        return
    
    elif state == GameState.SECONDBLOCKS_PICKUPRED:
        Functions.activelyHoldBlocks()
        # In this situation where 2 red blocks are stored in the carrier, it takes a lot of force to take this 3rd block.
        Functions.pickUpBlocks(downDuty=41)
        Functions.driveForwardToBlockAndPickUp(100, 1, 13)
        # This wait is probably unnecesarry
        wait(1000)
        Motors.pickup_motor.hold()
        state=GameState.SECONDBLOCKS_PUTRED
        return
    
    elif state == GameState.SECONDBLOCKS_PUTRED:
        Roboter.driveBase.turn(-90)
        # Maybe wait "So long bis da Roboter de scheiß Wand berührt"
        oldSettings = Functions.setHighSpeed()
        Roboter.driveBase.straight(300)
        Roboter.driveBase.turn(90)
        Roboter.driveBase.straight(475)
        # Functions.driveUntilColor(Color.BLACK, speed=50)

        # Roboter.driveBase.drive(50,0)
        # Functions.waitUntilHSVInRange(200, 280, 5)
        # print("Stopped at color: " + str(Roboter.bottomSensor.hsv()))
        # Roboter.driveBase.stop()
        # Functions.waitUntilDriveBaseDone()

        # Functions.driveUntilColor(Color.RED)
        Roboter.driveBase.turn(-90)
        Roboter.driveBase.straight(120)
        Functions.setNormalSpeed(oldSettings)

        Functions.releaseBlocks(4)
        Roboter.driveBase.straight(-150)
        Functions.moveCarrierToAbsolutePosition(30)

        state=GameState.BRINGTRASHTOAREA
        return

    elif state == GameState.BRINGTRASHTOAREA:

        Roboter.driveBase.turn(45)
        oldSettings = Functions.setHighSpeed()
        Roboter.driveBase.straight(900)
        Functions.setNormalSpeed(oldSettings)

        state=GameState.TREE
        return
    
    elif state == GameState.TREE:
        oldSettings = Functions.setHighSpeed()
        # 90mm zurück, drehen, von drehachse 260mm nach vorn -> länge von drehachse zu greifermittelpunkt abziehen
        Roboter.driveBase.straight(-100)
        Roboter.driveBase.turn(135)
        Motors.left_motor.dc(-60)
        Motors.right_motor.dc(-60)
        wait(800)
        Motors.left_motor.hold()
        Motors.right_motor.hold()
        wait(500)
        Roboter.driveBase.straight(110)
        Roboter.driveBase.turn(-90)
        Functions.driveUntilColor(Color.WHITE, -50)
        Functions.moveCarrierToAbsolutePosition(100)
        Roboter.driveBase.straight(410)
        Motors.pickup_motor.dc(-100)
        wait(200)
        Motors.pickup_motor.hold()
        Functions.moveCarrierToAbsolutePosition(10)
        Roboter.driveBase.straight(1500)
        Roboter.driveBase.turn(90)
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