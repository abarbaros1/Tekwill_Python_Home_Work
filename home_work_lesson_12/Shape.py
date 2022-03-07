from collections import defaultdict


class Shape:
    instances = []

    def __init__(self, _inner_color=None, _border_color=None):
        self._inner_color = _inner_color
        self._border_color = _border_color

    def set_inner_color(self, new_inner_color=None):
        self._inner_color = new_inner_color
        return self

    def get_inner_color(self):
        return self._inner_color

    def set_border_color(self, new_border_color=None):
        self._border_color = new_border_color
        return self

    def get_border_color(self):
        return self._border_color

    def __str__(self):
        try:
            return f'{type(self).__name__} with Inner Color {self._inner_color} and with Border Color {self._border_color} '
        except Exception as excpt:
            return f' Attributes are missing, return of value is not possible due {excpt} '


if __name__ == '__main__':
    a = Shape()
    # print(a)
    #
    a.set_inner_color('red').set_border_color('green')
    # # a.set_border_color('black')
    # print(a)
    # print(a.get_border_color())
    a.set_inner_color('orange')
    #b = Shape()
    # print(b)




