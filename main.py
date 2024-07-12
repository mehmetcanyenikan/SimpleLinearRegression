import numpy as np
from functools import reduce


class Summarizer:
    def _init_(self):
        self._x = []

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    def summarize(self) -> float:
        return sum(self._x)


class Multiplication:
    def multiply(self, list1, list2):
        return [x * y for x, y in zip(list1, list2)]


class Averages:
    def mean(self, values):
        return sum(values) / len(values)


class Regression:
    def _init_(self, xy_mean, x_mean, y_mean, xx_mean):
        self.xy_mean = xy_mean
        self.x_mean = x_mean
        self.y_mean = y_mean
        self.xx_mean = xx_mean

    def a(self) -> float:
        return ((self.xy_mean) - ((self.x_mean) * (self.y_mean))) / ((self.xx_mean) - ((self.x_mean) * (self.x_mean)))

    def b(self) -> float:
        a_value = self.a()
        return (self.y_mean - a_value * self.x_mean)


def main():
    x1 = [1, 2, 3, 4, 5]
    y1 = [1.2, 1.8, 2.6, 3.2, 3.8]

    summarizer = Summarizer()

    summarizer.x = x1
    x_sum = summarizer.summarize()
    print('x sum:  ', x_sum)

    summarizer.x = y1
    y_sum = summarizer.summarize()
    print('y sum:  ', y_sum)

    multiplication = Multiplication()
    xy_product = multiplication.multiply(x1, y1)
    xx_product = multiplication.multiply(x1, x1)

    summarizer.x = xy_product
    xy_sum = summarizer.summarize()
    print('xy sum: ', xy_sum)

    summarizer.x = xx_product
    xx_sum = summarizer.summarize()
    print('xx sum: ', xx_sum)

    averages = Averages()
    x_avg = averages.mean(x1)
    y_avg = averages.mean(y1)
    xy_avg = averages.mean(xy_product)
    xx_avg = averages.mean(xx_product)

    reg = Regression(xy_avg, x_avg, y_avg, xx_avg)
    print('coeff: ', reg.a())
    print('slope: ', reg.b())


if _name_ == '_main_':
    main()
