import math
import numpy as np
from abc import ABC, abstractmethod
from typing import Any



class Vec2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vec2D") -> "Vec2D":
        assert type(other) == Vec2D
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        
        return Vec2D(new_x, new_y)

    def __sub__(self, other: "Vec2D") -> "Vec2D":
        assert type(other) == Vec2D
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        
        return Vec2D(new_x, new_y)
        

    # let's ignore the left vs right multiplication distinction
    def __mul__(self, scale: float) -> "Vec2D":
        #assert type(scale) == float
        assert isinstance(scale, float) or isinstance(scale, np.floating)
        
        new_x = self.x * scale
        new_y = self.y * scale
        
        return Vec2D(new_x, new_y)
    
    __rmul__ = __mul__

    def __eq__(self, other: Any) -> bool:
      
        if self.x == other.x and self.y == other.y:
            return True

        return False

    def dot(self, other: "Vec2D") -> float:
        assert type(other) == Vec2D
        
        return self.x * other.x + self.y * other.y

    def length(self) -> float:
        
        return math.sqrt((self.x ** 2) + (self.y ** 2))
            
      
      

# =========================



# Parametric curves go from 0 -> 1 by convention
class Curve2D(ABC):
    @abstractmethod
    def parametric(self, t: float) -> Vec2D: pass

    @abstractmethod
    def tangent(self, t: float) -> Vec2D: pass

    @abstractmethod
    def length(self) -> float: pass

class Line2D(Curve2D):
    def __init__(self, v0: Vec2D, v1: Vec2D):
        self.v0 = v0
        self.v1 = v1
        self.new_vector = v1 - v0

    def parametric(self, t: float) -> Vec2D:
        return self.v0 + (self.new_vector * t)
               
    def tangent(self, t: float) -> Vec2D:
        return self.new_vector

    def length(self) -> float:
        return self.new_vector.length()

    
class Arc2D(Curve2D):
    def __init__(self, start: Vec2D, center: Vec2D, angle_deg: float):
        self.start = start
        self.center = center
        self.angle_rad = (angle_deg * math.pi) / 180
        self.r0 = start - center # vector from center to start

        self.radius = self.r0.length()

    def parametric(self, t: float) -> Vec2D:
        theta = t * self.angle_rad

        # matrix vs vector multiplication of rotation matrix vs "vector from center to start"
        x = self.r0.x*math.cos(theta) - self.r0.y * math.sin(theta)
        y = self.r0.x*math.sin(theta) + self.r0.y * math.cos(theta)
        
        r1 = Vec2D(x, y) #rotated "vector from center to start"

        return self.center + r1

    def tangent(self, t: float) -> Vec2D:
        return self.r0

    def length(self) -> float:
        return abs(self.radius * self.angle_rad)
    
