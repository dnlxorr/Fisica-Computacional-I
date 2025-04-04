import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
from mpmath import *

f_scalar = lambda x: math.sin(x)
f_array = lambda x: np.sin(x)

a, b = 0, np.pi
exact_value = quad(sin, [a,b])

def trapezoid_rule(f, _a, _b, n):
    x = np.linspace(_a, _b, n + 1)
    y = f(x)
    h = (_b - _a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson_rule(f, _a, _b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par para la regla de Simpson")
    x = np.linspace(_a, _b, n + 1)
    y = f(x)
    h = (_b - _a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

ns = np.arange(2, 100, 2)
trap_errors = [abs(trapezoid_rule(f_array, a, b, n) - exact_value) for n in ns]
simp_errors = [abs(simpson_rule(f_array, a, b, n) - exact_value) for n in ns]

plt.plot(ns, trap_errors, label="Error Regla del Trapecio")
plt.plot(ns, simp_errors, label="Error Regla de Simpson")
plt.yscale("log")
plt.xlabel("Número de subintervalos (n)")
plt.ylabel("Error absoluto")
plt.title("Comparación de errores numéricos")
plt.legend()
plt.grid(True)
plt.show()