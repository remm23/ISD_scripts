class Shape:
    def __init__(self,sides):
        self.sides = sides

    def aera(self):
        return "unknown shape"

class Circle(Shape):
    def __init__(self,sides,radius):
        self.sides = sides
        self.radius = radius

    def aera(self):
        return ("%.2f") % (3.14 * (self.radius ** 2))

class Elipse(Circle):    
    #has two radiuses
    def __init__(self,sides,radius,radius_2):
        super().__init__(sides,radius)
        self.radius_2 = radius_2

    def aera(self):
        # multply the x and y distance from the center
        # multply that result by pi(3.14)
        return ("%.2f") % (3.14 * (self.radius * self.radius_2))

class Square(Shape):
    def __init__(self,sides,length):
        super().__init__(sides)
        self.length = length

    def aera(self):
        return self.length * self.length

class Retangle(Square):
    def __init__(self,sides,length,width):
        super().__init__(sides,length)
        self.width = width

    def aera(self):
        return self.length * self.width

shape1 = Shape(6)
circle1 = Circle(0,5)
elipse1 = Elipse(0,5,7)
square1 = Square(4,5)
retangle1 = Retangle(4,5,7)


print(shape1.aera())
print(circle1.aera())
print(elipse1.aera())
print(square1.aera())
print(retangle1.aera())
    
