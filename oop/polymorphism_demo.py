# polymorphism_demo.py

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Rectangle shape defined by length and width."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate area of the rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calculate area of the circle (π × r²)."""
        return math.pi * self.radius ** 2
