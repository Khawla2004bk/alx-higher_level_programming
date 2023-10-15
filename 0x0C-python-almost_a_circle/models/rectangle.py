#!/usr/bin/python3
""" import Base"""

from models.base import Base
""" Class Rectangle"""


class Rectangle(Base):
    """
    This class allows you to create and manipulate Rectangle objects.
    Each Rectangle is defined by its width and height
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int) : position of rectangle in x
            y (int) : position of rectangle in y
            id (int): id of the new instance

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width (side length) of the rectangle.

        Args:
            value (int): The new width for the rectangle.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height (side length) of the rectangle.

        Args:
            value (int): The new height for the rectangle.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieve the x of the rectangle.

        Returns:
            int: The x of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x (side length) of the rectangle.

        Args:
            value (int): The new x for the rectangle.

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieve the y of the rectangle.

        Returns:
            int: The y of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y (side length) of the rectangle.

        Args:
            value (int): The new y for the rectangle.

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate and returns the rectangle area """
        return (self.__width * self.__height)

    def display(self):
        """ print a rectangle using the "#" character
            based on its width and height """
        rect = ""
        for _ in range(self.__height):
            rect += "#" * self.__width + "\n"
        print(rect, end="")

    def display(self):
        """ print a rectangle using the "#" character
            based on its width, height, x and y """
        rect = ""
        for _ in range(self.__y):
            rect += "\n"

        for _ in range(self.__height):
            rect += " " * self.__x + "#" * self.__width + "\n"
        print(rect, end="")

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        x_y = str(f"{self.__x}/{self.__y}")
        w_h = str(f"{self.__width}/{self.__height}")
        return f"[Rectangle] ({self.id}) {x_y} - {w_h}"

    def update(self, *args):
        """ Update Square with *args """

        arg_list = [self.id, self.__width, self.__height, self.__x, self.__y]
        for x, arg in enumerate(args):
            arg_list[x] = arg
            if x == 4:
                break

        super().__init__(arg_list[0])
        self.width = arg_list[1]
        self.height = arg_list[2]
        self.x = arg_list[3]
        self.y = arg_list[4]

    def update(self, *args, **kwargs):
        """ Update Square with *args or **kwargs """

        if args:
            arg_l = [self.id, self.__width, self.__height, self.__x, self.__y]
            for x, arg in enumerate(args):
                arg_l[x] = arg
                if x == 4:
                    break
            super().__init__(arg_l[0])
            self.width = arg_l[1]
            self.height = arg_l[2]
            self.x = arg_l[3]
            self.y = arg_l[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method that returns the dictionary representation of a Rectangle
        """
        rect = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
        return rect
