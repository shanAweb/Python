class Point:
    def draw(self):
        print("Draw")
    def run(self):
        print("Run")


point1=Point()
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)
point1.draw()
point1.run()