class Shape:
    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


s = Circle()
s.draw()

s = Rectangle()
s.draw()