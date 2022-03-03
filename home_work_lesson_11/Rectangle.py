from Shape import Shape

class Rectangle(Shape):
    def __init__(self,inner_color,border_color, width, length):
        super().__init__(inner_color,border_color)
        self.width = width
        self.length = length
    def __str__(self):
        return f"{type(self).__name__} has width {self.width} and length {self.length}, with inner color {self.inner_color.upper()} and with border color {self.border_color.upper()} "

a=Rectangle('red', 'green', 4,5)
print(a)