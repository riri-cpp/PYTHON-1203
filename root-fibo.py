import math

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n] # return yung fibonacci until n

def rootfib(n):
    fibonacci_elements = fibonacci(n)
    sqrt_elements = [math.sqrt(element) for element in fibonacci_elements]
    return fibonacci_elements, sqrt_elements


nth = int(input("Enter the number of elements: "))
fibonacci_elements, sqrt_elements = rootfib(nth)
print(f"Fibonacci elements at {nth} terms:")
for element in fibonacci_elements:
    print(element, end=" ")
print()
print(f"Square root of elements: ")
for root in sqrt_elements:
    print(f"{root:.2f}", end=" ")