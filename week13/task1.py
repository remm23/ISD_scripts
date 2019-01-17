class Shape:
    def __init__(self,sides):
        self.sides = sides

    def aera(self):
        return 0

class Retangle(Shape):
    def __init__(self,sides,length,width):
        super().__init__(sides)
        self.length = length
        self.width = width

    def aera(self):
        return self.length * self.width

class Square(Retangle):
    def __init__(self,sides,length,width):
        super().__init__(sides,length,width)
        # overwrite self.width with the value of length so all sides are equal
        self.width = length 
    
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
    


e1 = Circle(0,68.3)
print(e1.aera())