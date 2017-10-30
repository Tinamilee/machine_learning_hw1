import functools as ft
import matplotlib.pyplot as plt
import numpy as np
import math

def function(x):
    return x * x

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


def derivative(x):
    return 2 * x

def partial_difference_quotient(f, v, i, h):
    """計算 f 在 v 中第 i 個元素所對應的差商"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]




derivative_estimate = ft.partial(difference_quotient, function, h=0.0001)

x = range(-10, 10)

plt.title("Actual derivatives vs. Estimates")
plt.plot(x, list(map(derivative, x)), 'rx')
plt.plot(x, list(map(derivative_estimate, x)), 'b+')
plt.legend(loc = 9)
plt.show()