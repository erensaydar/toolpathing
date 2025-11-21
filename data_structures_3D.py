import math
import numpy as np
from abc import ABC, abstractmethod
from typing import Any



class Vec3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vec3D") -> "Vec3D":
        assert type(other) == Vec3D
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        
        return Vec3D(new_x, new_y, new_z)

    def __sub__(self, other: "Vec3D") -> "Vec3D":
        assert type(other) == Vec3D
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        
        return Vec3D(new_x, new_y, new_z)
        

   
    def __mul__(self, scale: float) -> "Vec3D":
        #assert type(scale) == float
        assert isinstance(scale, float) or isinstance(scale, np.floating)
        
        new_x = self.x * scale
        new_y = self.y * scale
        new_z = self.z * scale
        
        return Vec3D(new_x, new_y, new_z)
    
    __rmul__ = __mul__

    def __eq__(self, other: Any) -> bool:
      
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True

        return False

    def dot(self, other: "Vec3D") -> float:
        assert type(other) == Vec3D
        
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))
            
      
      

# =========================



# Parametric curves go from 0 -> 1 by convention
class Curve3D(ABC):
    @abstractmethod
    def parametric(self, t: float) -> Vec3D: pass

    @abstractmethod
    def tangent(self, t: float) -> Vec3D: pass

    @abstractmethod
    def length(self) -> float: pass


class Line3D(Curve3D):
    def __init__(self, v0: Vec3D, v1: Vec3D):
        self.v0 = v0
        self.v1 = v1
        self.new_vector = v1 - v0

    def parametric(self, t: float) -> Vec3D:
        return self.v0 + (self.new_vector * t)
               
    def tangent(self, t: float) -> Vec3D:
        return self.new_vector

    def length(self) -> float:
        return self.new_vector.length()


class Helix3D(Curve3D):
    def __init__(self, radius: float, turns: float, height: float, center: Vec3D):
        self.radius = radius
        self.n = turns
        self.h = height
        self.center = center

    def parametric(self, t: float) -> Vec3D:
        theta = 2 * math.pi * self.n * t
        x = self.center.x + self.radius * math.cos(theta)
        y = self.center.y + self.radius * math.sin(theta)
        z = self.center.z + self.h * (1 - t) # from h to 0
        return Vec3D(x, y, z)

    def tangent(self, t: float) -> Vec3D:
        pass

    def length(self) -> float:
        pass