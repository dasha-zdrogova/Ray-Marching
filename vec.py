from __future__ import annotations
import math
import os

class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, float):
            return vec2(self.x + other, self.y + other)
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if isinstance(other, float):
            return vec2(self.x - other, self.y - other)
        return vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if isinstance(other, float):
            return vec2(self.x * other, self.y * other)
        return vec2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        if isinstance(other, float):
            return vec2(self.x / other, self.y / other)
        return vec2(self.x / other.x, self.y / other.y)
    
    def length(self) -> float:
        return (self.x * self.x + self.y * self.y)**0.5
    

class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        if isinstance(other, float):
            return vec3(self.x + other, self.y + other, self.z + other)
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        if isinstance(other, float):
            return vec3(self.x - other, self.y - other, self.z - other)
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, float):
            return vec3(self.x * other, self.y * other, self.z * other)
        return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        if isinstance(other, float):
            return vec3(self.x / other, self.y / other, self.z / other)
        return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    
    def length(self) -> float:
        return (self.x * self.x + self.y * self.y + self.z * self.z)**0.5
    def norm(self) -> vec3:
        return self/self.length()
    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z