from math import *
class Quadratic:
    def quadratic(self,a,b,c):
        delta=b**2-(4*a*c)
        if delta>0:
            Root1 = int((-b + sqrt(delta)) / (2 * a))
            Root2 = int((-b - sqrt(delta)) / (2 * a))
            return Root1, Root2
        else:
            return "it is an imaginary line"


