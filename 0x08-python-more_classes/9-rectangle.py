#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """A class to represent a Rectangle
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the rectangle.
        Args:
            width (int): The of the rectangle (default is 0)
            height (int): The height of the rectangle (default is 0)
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle
        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Arg:
            value (int): The new width value
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Arg:
            value (int): The new height value.
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle
        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle
        Returns:
            str: A string representing the rectangle with '#' characters.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            row = str(self.print_symbol) * self.width
            rect_str += row + '\n'
        return rect_str[:-1]

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance of the rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return the bigger rectangle based on the area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The first rectangle.
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        Returns:
            Rectangle: The rectangle with the larger area,
             or rect_1 if they have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to create a new instance of Rectangle as a square.
        Arg:
            size (int, optional): The size of the square
             (both width and height). Default is 0.
        Returns:
            Rectangle: A new instance of Rectangle with equal width
             and height (a square).
        """
        return cls(size, size)
