import math

class Vector:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise "error"
    
    def substract(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise "error"

    def multiply(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def divide(self, scalar: float):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def dot(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise "error"
    
    def cross(self, other):
        if isinstance(other, Vector):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector(x, y, z)
        else:
            raise "error"
    
    def length(self):
        return math.sqrt(self.dot(self))

    def normalize(self):
        return self.divide(self.length())