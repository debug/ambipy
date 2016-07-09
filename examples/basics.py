import sys

sys.path.insert(0, "/Users/Dom/Desktop/ambipy")

from home import User, Home
from rooms import Swing, Power

user = User()
#user.email = "EMAIL HERE"
#user.password = "PASSWORD HERE"

home = Home(user)

for room in home.rooms:
    room.power = Power.ON
#    room.swing == Swing.OFF
#    print("Mode >>", room.mode)
#    print("Power >>", room.power)
#    print("Temp >>", room.temperature)
    room.temperature = 20.6
#    print("Fan >>", room.fan)
