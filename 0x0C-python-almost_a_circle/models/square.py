""" import Rectangle class """

from models.rectangle import Rectangle
""" Class Square """


class Square(Rectangle):
    """
    This class allows you to create and manipulate Square objects.
    Each Square is defined by its width and height
    """
    def __init__(self, size, x=0, y=0, id=None):

        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int) : position of rectangle in x
            y (int) : position of rectangle in y
            id (int): id of the new instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size (side length) of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size> """
        x_y = str(f"{self.x}/{self.y}")
        return f"[Square] ({self.id}) {x_y} - {self.width}"

    def update(self, *args, **kwargs):
        """ Update Square with *args or **kwargs """
        if args:
            arg_list = list(args)
            if len(arg_list) > 0:
                self.id = arg_list[0]
            if len(arg_list) > 1:
                self.size = arg_list[1]
            if len(arg_list) > 2:
                self.x = arg_list[2]
            if len(arg_list) > 3:
                self.y = arg_list[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method that returns the dictionary representation of a Rectangle
        """
        square = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return square
