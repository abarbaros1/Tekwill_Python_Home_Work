class NumbersList(list):

    def __init__(self, iterable):
        self._check_is_iterable_numeric(iterable)
        super().__init__(iterable)

    def _check_is_iterable_numeric(self, iterable):
        for i in iterable:
            if type(i) not in [int,float]:
                raise TypeError('Expected Integer or Float')

    def append(self, __object) -> None:
        self._check_is_iterable_numeric([__object])
        super().append(__object)

    def extend(self, __iterable) -> None:
        self._check_is_iterable_numeric(__iterable)
        super().extend(__iterable)

    def get_average(self):
        total_count = 0
        total_sum = sum(self)
        for el in self:
            total_count += 1
        return total_sum/total_count

    def get_sum(self):
        return sum(self)


if __name__ == '__main__':
    my_str_list = NumbersList([1, 2, 3,1.2])
    my_str_list.append(4)
    print(my_str_list)
    print(my_str_list[0])
    my_str_list[0] = 1
    print(my_str_list[0])
    print(my_str_list)
    print(sum(my_str_list))
    print(my_str_list)
    print(my_str_list.get_average())
    print(my_str_list.get_sum())

