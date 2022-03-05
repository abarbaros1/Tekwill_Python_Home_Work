import Shape from Shape
import Circle from Circle
import Rectangle from Rectangle
import Square from Square

class ShapeService:
    def __init__(self, _inner_color=None, _border_color=None):
        if _inner_color is None:
            self._inner_color = self.default_inner_color
        else:
            self._inner_color = _inner_color
        if _border_color is None:
            self._border_color = self.default_border_color
        else:
            self._border_color = _border_color

#########################################################################################

    @property
    def default_inner_color(self):
        return 'white'

    @property
    def default_border_color(self):
        return 'black'

##########################################################################################
