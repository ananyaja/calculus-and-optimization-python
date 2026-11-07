
# Module 1: Univariate Gradient Descent Basics

> *"Optimization is the art of finding the best possible outcome under given constraints—navigating loss landscapes step by step."*

---

## 🎯 Mathematical Core

In machine learning and numerical optimization, we frequently want to minimize a cost or loss function $f(x)$. **Gradient Descent** is an iterative optimization algorithm that uses the derivative (gradient) to guide our search toward the function's local minimum.

For this module, we examine a classic quadratic convex function:

$$f(x) = x^2 - 4x + 4$$

Notice that this can be factored perfectly into a squared binomial:

$$f(x) = (x - 2)^2$$

### The Derivative (Gradient)
To know which direction to step, we compute the first derivative with respect to $x$:

$$f'(x) = \frac{d}{dx}(x^2 - 4x + 4) = 2x - 4$$

* **When $f'(x) > 0$:** The function is sloping upward to the right; we must step **left** (decrease $x$).
* **When $f'(x) < 0$:** The function is sloping downward to the right; we must step **right** (increase $x$).
* **When $f'(x) = 0$:** We have reached the critical point (the global minimum at $x = 2$, where $f(2) = 0$).

### The Update Rule
The core iterative step of gradient descent is defined as:

$$x_{new} = x_{old} - \alpha \cdot f'(x_{old})$$

Where $\alpha$ represents the **learning rate** (step size). 
* If $\alpha$ is too large, the algorithm overshoots and diverges.
* If $\alpha$ is too small, convergence takes an impractically long time.

---

## 💻 Python Implementation

Here is the clean, modular Python script located in `scripts/01_gradient_descent.py`:

```python
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
