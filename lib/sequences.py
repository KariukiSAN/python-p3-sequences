#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    if length > 0:
        a, b = 0, 1
        fib_sequence.append(a)
        for _ in range(1, length):
            a, b = b, a + b
            fib_sequence.append(a)

    print(fib_sequence)

if __name__ == "__main__":

    print_fibonacci(10)
