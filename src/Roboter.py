from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import Motors

hub = PrimeHub(top_side=-Axis.X, front_side=Axis.Z)

driveBase = DriveBase(Motors.left_motor, Motors.right_motor, wheel_diameter=55.3, axle_track=102)
driveBase.use_gyro(True)
#print(Roboter.driveBase.settings())

bottomSensor = ColorSensor(Port.D)

holdDutyCycle = -70