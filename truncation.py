import math

def taylor_exp(x, terms):
    """Calculate e^x using Taylor series with a given number of terms."""
    result = 0
    for n in range(terms):
        result += (x ** n) / math.factorial(n)
    return result

# True value of e^1 using math.exp
x = 1.0
true_value = math.exp(x)
print(f"True value of e^{x}: {true_value}")

# Approximate with different numbers of terms
for terms in [2, 4, 6]:
    approx = taylor_exp(x, terms)
    truncation_error = true_value - approx
    print(f"Terms: {terms}, Approximation: {approx}, Truncation Error: {truncation_error}")