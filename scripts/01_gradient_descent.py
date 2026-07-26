"""
Gradient Descent Optimizer from Scratch
----------------------------------------
Demonstrates 1D Gradient Descent optimization on a quadratic function f(x) = x^2 - 4x + 4.
"""

import numpy as np

def objective_function(x):
    """f(x) = x^2 - 4x + 4"""
    return x**2 - 4*x + 4

def gradient(x):
    """f'(x) = 2x - 4"""
    return 2*x - 4

def gradient_descent(initial_x, learning_rate=0.1, iterations=30):
    x = initial_x
    history = [x]

    print(f"Starting Gradient Descent at x = {initial_x:.2f}")
    for i in range(iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        history.append(x)
        if (i + 1) % 5 == 0 or i == 0:
            print(f"Iteration {i+1:02d}: x = {x:.4f}, f(x) = {objective_function(x):.4f}")

    return x, history

if __name__ == "__main__":
    optimal_x, history = gradient_descent(initial_x=10.0, learning_rate=0.1, iterations=25)
    print(f"\nOptimal x found: {optimal_x:.4f} (True Minimum at x = 2.0000)")
