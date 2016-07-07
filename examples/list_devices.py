import sys

sys.path.insert(0, "/Users/Dom/Desktop/ambipy")

from home import User, Home

user = User()
home = Home(user)

for room in home.rooms:
    print(room.name)
