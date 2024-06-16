import math

class Circle:
    def __init__(self, val, val_type):
        self.val = val
        self.val_type = val_type

    def __repr__(self):
        type = ''
        if self.val_type == 'r':
            type == 'r'
        elif self.val_type == 'd':
            type == 'd'
        else:
            raise TypeError(f"{self.val_type} is not a valid circle measurment")
        return(f"{self.__class__.__name__} : {self.val} {type}")
    def get_area(self):
        area = 0
        if self.val_type == 'r':
            area = self.val*2*(math.pi)
        elif self.val_type == 'd':
            area = self.val*(math.pi)
        else:
            raise TypeError(f"{self.val_type} is not a valid circle measurment")
        return area
    def __gt__(self, other):
        if self.get_area() > other.get_area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.get_area() == other.get_area():
            return True
        else:
            return False
    def __add__(self, other):
        if isinstance(other, int):
            new_val = (self.val + other)
        elif isinstance(other, Circle):
            new_val = (self.val + other.val)
        return(Circle(new_val, self.val_type))

