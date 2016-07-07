import sys

sys.path.insert(0, "/Users/Dom/Desktop/ambipy")

from home import User, Home

user = User()
#user.email = "EMAIL HERE"
#user.password = "PASSWORD HERE"

home = Home(user)

for room in home.rooms:
    print(room.name)
    print(room.power)
