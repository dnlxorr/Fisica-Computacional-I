import math

def derivative_approx(f, x, h):
    """Approximate f'(x) using forward difference."""
    return (f(x + h) - f(x)) / h

# True derivative of sin(x) is cos(x)
x = 1.0
true_deriv = math.cos(x)
h_values = [0.1, 0.01, 0.001]

for h in h_values:
    approx = derivative_approx(math.sin, x, h)
    total_error = true_deriv - approx
    # Truncation error dominates with larger h, round-off with smaller h
    print(f"h = {h}, Approx: {approx}, True: {true_deriv}, Total Error: {total_error}")