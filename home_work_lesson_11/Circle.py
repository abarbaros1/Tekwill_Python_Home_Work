from Shape import Shape
class Circle:
    def __init__(self, inner_color,border_color,radius):
        super().__init__(inner_color,border_color)
        self.radius = radius

a= Circle('red','green',5)
print(a)
