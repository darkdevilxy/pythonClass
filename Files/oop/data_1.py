numbers = [1, 2, 3, 4, 5]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point(10, 20)
print(point1.x, point1.y)
point1.draw()

point2 = Point(20, 30)
point2.move()
point2.z = 40
print(point2.x, point2.y, point2.z)