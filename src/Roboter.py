from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import Motors

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)

driveBase = DriveBase(Motors.left_motor, Motors.right_motor, wheel_diameter=55.6, axle_track=115)
driveBase.use_gyro(True)
driveBase.settings(straight_acceleration=300)
# print(driveBase.settings())