
# ''''''''
# Abstract class
# Aabstract method
# ''''''''

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Circule(Shape):

    def __init__(self,side):
        self.__side=side

    def area(self):
        return 2*3.142*(self.__side**2)

    def draw(self):
        return "circule is drawing"

side=float(input("enter the sides in cm : "))
circule=Circule(side)
area=circule.area()
print(area)
draw=circule.draw()
print(draw)


# ''''''''
# Encapsulation
# ''''''''


class Car:
    def __init__(self,speed,value):
        self.__speed=speed
        self.__color=value

    def set_speed(self,speed):
        self.__speed=speed

    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.__color=value

    def get_color(self):
        return self.__color

car=Car(speed=0,value=None)
car.set_speed("200")
print(car.get_speed())
car.set_speed(500)
print(car.get_speed())
car.set_color("25")
print(car.get_color())
car.set_color("red")
print(car.get_color())



# ''''''
# Private methods
# ''''''

class Hello:
    def __init__(self,name):
        self.a=10
        self._b=20
        self.__c=30

    def public_method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print("public")
        #so to call the private method in side the call
        #we call the private method inside the pulic method
        #using "self" keyword
        self.__private_method()

    def __private_method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print("private")

hello=Hello("name")
hello.public_method()

#we can not the call the private method out side the class
# hello.__private_method()


# ''''''
# Inheritance
# ''''''

class Polygon:

    __Width=None
    __Height=None

    def set_values(self,width,height):
        self.__Width=width
        self.__Height=height

    def get_width(self):
        return self.__Width

    def get_height(self):
        return self.__Height

class Rectangle(Polygon):

    def area(self):
        return self.get_height() * self.get_width()



class Triangle(Polygon):

    def area(self):
        return self.get_width() * self.get_height() / 2

rect = Rectangle()

tri = Triangle()

rect.set_values(50,40)
tri.set_values(50,40)

print(rect.area())
print(tri.area())

