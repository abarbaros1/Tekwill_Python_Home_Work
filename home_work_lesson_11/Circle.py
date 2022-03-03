from Shape import Shape

class Circle(Shape):

    def __init__(self, inner_color,border_color,radius):
        super().__init__(inner_color,border_color)
        self.radius = radius

    def __str__(self):
        return f"{type(self).__name__} has radius of {self.radius} with inner color {self.inner_color.upper()} and with border color {self.border_color.upper()} "

# a= Circle('red','green',5)
# print(a)
