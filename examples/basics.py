import sys

sys.path.insert(0, "/Users/Dom/Desktop/ambipy")

from home import User, Home
from rooms import Swing, Power

user = User()
#user.email = "EMAIL HERE"
#user.password = "PASSWORD HERE"

home = Home(user)

for room in home.rooms:

#    room.swing == Swing.OFF
#    print("Mode >>", room.mode)
#    print("Power >>", room.power)
#    print("Temp >>", room.temperature)
    # Tip: any operations such as temperature change, swing mode etc need to be performed before any power OFF action as these will switch the AC unit back on.
    room.temperature = 21.0
    room.power = Power.OFF
#    print("Fan >>", room.fan)
