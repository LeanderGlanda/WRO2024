from GameRoutine import gameRoutine
import Roboter

print(Roboter.hub.battery.voltage())

while True:
    
    gameRoutine()