class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def draw():
        print("Draw")
    def run():
        print("Run")

point1=Point(10, 20)
print(point1.x)
point1.x=11
print(point1.x)