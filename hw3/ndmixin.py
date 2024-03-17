import numpy as np


class StrMagicNumberMixin(object):
    def __str__(self):
        return 42


class SaveMagicNumberMixin(object):
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.value))


class MagicNumber(np.lib.mixins.NDArrayOperatorsMixin, StrMagicNumberMixin, SaveMagicNumberMixin):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x.value if isinstance(x, MagicNumber) else x for x in inputs)
        if ufunc.__name__ == 'matmul':
            ufunc = np.multiply
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)


mn1 = MagicNumber(100)
mn2 = MagicNumber(200)


a = mn1 + mn2
a.save_to_file('hw3_2/magicnumber+.txt')
b = mn1 * mn2
b.save_to_file('hw3_2/magicnumber_mul.txt')
c = mn1 @ mn2
c.save_to_file('hw3_2/magicnumber_@.txt')
