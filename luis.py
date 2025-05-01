import numpy as np

def f(x, y):
    return x**2 + y**2

# Regla de Simpson para una sola dimensión
def simpson_rule(f, _a, _b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par para la regla de Simpson")
    x = np.linspace(_a, _b, n + 1, endpoint=False)  # evitar incluir 1
    y = f(x)
    h = (_b - _a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def integral_y(x, y_range, n_y):
    f_y = lambda y: x**2 + y**2
    return simpson_rule(f_y, y_range[0], y_range[1], n_y)

# Integración con respecto a x (después de integrar con respecto a y)
def integral_x(y_range, x_range, n_x, n_y):
    total_integral = 0
    for x in np.linspace(x_range[0], x_range[1], n_x):
        integral_xy = integral_y(x,y_range, n_y)
        total_integral += integral_xy
    # Sumamos los resultados de la integración con respecto a x
    return (x_range[1] - x_range[0]) / n_x * total_integral

# Parámetros
x_range = [-100, 35]  # Intervalo para x
y_range = [-20, 200]  # Intervalo para y
n_x = 60  # Número de subintervalos para x
n_y = 60  # Número de subintervalos para y

# Resultado final
result = integral_x(y_range, x_range, n_x, n_y)
print(f"Resultado de la integral: {result}")
