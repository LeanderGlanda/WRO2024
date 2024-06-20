from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from GameRoutine import gameRoutine

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)

driveBase = DriveBase(Motor.left_motor, Motor.right_motor, wheel_diameter=51.5, axle_track=115)
driveBase.use_gyro(True)

gameRoutine()