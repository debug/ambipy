import sys

sys.path.insert(0, "/Users/Dom/Desktop/ambipy")

from home import User, Home
from rooms import Swing, Power, Fan

user = User()
#user.email = "EMAIL HERE"
#user.password = "PASSWORD HERE"

home = Home(user)

for room in home.rooms:

#    room.swing == Swing.OFF
#    print("Mode >>", room.mode)
#    print("Power >>", room.power)
#    print("Temp >>", room.temperature)

    #room.temperature = 21.0
    #room.power = Power.ON
    #room.fan = Fan.LOW
    room.swing = Swing.AUTO
