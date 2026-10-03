"""Fibonacci sequence generator.

This script generates the first n numbers of the Fibonacci series using an
iterative approach with constant extra space.
"""

def fibonacci(n):
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


if __name__ == "__main__":
    print(fibonacci(10))
