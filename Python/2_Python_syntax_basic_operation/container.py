from enum import Enum

array = [1, 2, 3]

colors = ["red", "blue"]

print(type(colors))
print(type(colors[0]))

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    ORANGE = 4

print(Color.GREEN)