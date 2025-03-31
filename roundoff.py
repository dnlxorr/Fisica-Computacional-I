# Simple addition with numbers that can't be exactly represented in binary
def round_off_example():
    a = 0.1
    b = 0.2
    true_sum = 0.3  # Mathematical true value
    computed_sum = a + b
    round_off_error = true_sum - computed_sum
    print(f"a = {a}, b = {b}")
    print(f"Computed sum: {computed_sum}")
    print(f"True sum: {true_sum}")
    print(f"Round-off Error: {round_off_error}")

# Repeated addition to amplify round-off error
def cumulative_round_off():
    result = 0.0
    for _ in range(1000):
        result += 0.1
    true_value = 1000 * 0.1  # 100.0
    round_off_error = true_value - result
    print(f"Computed result (1000 * 0.1): {result}")
    print(f"True value: {true_value}")
    print(f"Cumulative Round-off Error: {round_off_error}")

# Run examples
print("Simple Round-off Example:")
round_off_example()
print("\nCumulative Round-off Example:")
cumulative_round_off()