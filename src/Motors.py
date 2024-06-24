from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop


carrier_motor = Motor(Port.E)
pickup_motor = Motor(Port.A, profile=5)
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)