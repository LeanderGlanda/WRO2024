from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from GameRoutine import gameRoutine

#hub = PrimeHub(top_side=-Axis.X, front_side=Axis.Z)
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)


# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=51.5, axle_track=115)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
#drive_base.straight(500)

# Turn around clockwise by 180 degrees.
#drive_base.turn(360)

# Drive forward again to get back to the start.
#drive_base.straight(500)

# Turn around counterclockwise.
#rive_base.turn(-180)

gameRoutine()

#
# TODO
# Wir können run_until_stalled bei unserem carrier nicht verwenden. Dies funktioniert nicht zuverlässig.
# Lösung: Absolute Position des carrier am Anfang herausfinden und berechnungen anstellen.
#