from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop


carrier_motor = Motor(Port.D)
pickup_motor = Motor(Port.B)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)