from Shape import Shape

class Circle(Shape):

    def __init__(self, inner_color=None,border_color=None,_radius=None):
        super().__init__(inner_color,border_color)
        self._radius = _radius

    def get_radius(self,new_radius):
        self._radius = new_radius

    def __str__(self):
        try:
            return f"{type(self).__name__} has radius of {self.radius} with inner color {self.inner_color.upper()} and with border color {self.border_color.upper()} "
        except Exception as excpt :
            return f'Attributes are missing, return of value is not possible due to {excpt}'

a= Circle()
a.get_radius(5)
print(a)
