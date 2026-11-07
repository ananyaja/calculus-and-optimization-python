# Module 4: Riemann Sums and Definite Integration

> *"Integration is the art of accumulation—breaking a continuous curve into infinitely thin rectangular slices and summing them up to find the exact area under the curve."*

---

## 🎯 Mathematical Core

Before the formal development of the Fundamental Theorem of Calculus, mathematicians approximated accumulated change and areas under curves using finite partitions. **Riemann Sums** form the rigorous foundation of definite integrals.

In this module, we compute the definite integral of a convex parabolic function over the interval $[0, 3]$:

$$\int_{0}^{3} x^2 \, dx$$

### Analytical Solution
Using the power rule for integration:

$$\int_{0}^{3} x^2 \, dx = \left[ \frac{x^3}{3} \right]_{0}^{3} = \frac{3^3}{3} - \frac{0^3}{3} = \frac{27}{3} = 9.0$$

### Numerical Approximation Methods
When analytical integration is impossible or computationally expensive, we approximate the area using discrete subdivisions ($N$ rectangles of width $\Delta x = \frac{b - a}{N}$):

1. **Left Riemann Sum (Underestimate):** Evaluates the height at the left endpoint of each subinterval.
   $$\text{Left Sum} = \sum_{i=0}^{N-1} f(x_i) \cdot \Delta x$$

2. **Right Riemann Sum (Overestimate):** Evaluates the height at the right endpoint of each subinterval.
   $$\text{Right Sum} = \sum_{i=1}^{N} f(x_i) \cdot \Delta x$$

3. **Trapezoidal Rule:** Averages the left and right sums to form linear trapezoids instead of flat-topped rectangles, dramatically reducing approximation error.
   $$\text{Trapezoid Sum} = \frac{\text{Left Sum} + \text{Right Sum}}{2}$$

---

## 💻 Python Implementation

Here is the clean, modular Python script located in `scripts/04_riemann_integration.py`:

```python
"""
18.01 Single Variable Calculus: Riemann Sums & Definite Integration
--------------------------------------------------------------------
Objective: Calculate area under f(x) = x^2 from x=0 to x=3.
Exact Calculus Result: ∫[0 to 3] x^2 dx = [x^3 / 3]_0^3 = 27/3 = 9.0
Approximations: Left Riemann Sum, Right Riemann Sum, and Trapezoidal Rule.
Saves: Visual comparison plot showing area rectangles to assets/
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Function to integrate: f(x) = x^2"""
    return x**2

def calculate_riemann_sums(a=0.0, b=3.0, N=10):
    dx = (b - a) / N

    # Grid points
    x_left = np.linspace(a, b - dx, N)
    x_right = np.linspace(a + dx, b, N)

    # Sum calculations
    left_sum = np.sum(f(x_left) * dx)
    right_sum = np.sum(f(x_right) * dx)
    trapezoid_sum = (left_sum + right_sum) / 2.0
    exact_val = 9.0  # Exact analytical integral

    print(f"--- Riemann Sum Integration for f(x) = x^2 over [{a}, {b}] with N={N} ---")
    print(f"Exact Analytical Integral : {exact_val:.6f}")
    print(f"Left Riemann Sum (Under)  : {left_sum:.6f}  | Error: {abs(exact_val - left_sum):.6f}")
    print(f"Right Riemann Sum (Over)  : {right_sum:.6f}  | Error: {abs(exact_val - right_sum):.6f}")
    print(f"Trapezoidal Approximation : {trapezoid_sum:.6f}  | Error: {abs(exact_val - trapezoid_sum):.6f}")

    return left_sum, right_sum, trapezoid_sum, exact_val, dx

def plot_riemann_visualizations(a=0.0, b=3.0, N=10):
    dx = (b - a) / N
    x_curve = np.linspace(a, b, 200)
    y_curve = f(x_curve)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Plot 1: Left Riemann Sum (Under-estimate) ---
    x_left = np.linspace(a, b - dx, N)
    ax1.plot(x_curve, y_curve, 'b-', linewidth=2, label='f(x) = x^2')
    ax1.bar(x_left, f(x_left), width=dx, align='edge', alpha=0.3, color='orange', edgecolor='darkorange', label='Left Rectangles')
    ax1.set_title(f'Left Riemann Sum (N={N})', fontsize=12, fontweight='bold')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend()

    # --- Plot 2: Right Riemann Sum (Over-estimate) ---
    x_right = np.linspace(a, b, N+1)
    ax2.plot(x_curve, y_curve, 'b-', linewidth=2, label='f(x) = x^2')
    ax2.bar(x_left, f(x_left + dx), width=dx, align='edge', alpha=0.3, color='green', edgecolor='darkgreen', label='Right Rectangles')
    ax2.set_title(f'Right Riemann Sum (N={N})', fontsize=12, fontweight='bold')
    ax2.set_xlabel('x')
    ax2.set_ylabel('f(x)')
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend()

    plt.tight_layout()
    plot_path = "assets/04_riemann_integration_rectangles.png"
    plt.savefig(plot_path, dpi=300)
    plt.close()
    print(f"\n✅ Riemann Sum plot successfully saved to: {plot_path}")

if __name__ == "__main__":
    calculate_riemann_sums(a=0.0, b=3.0, N=10)
    plot_riemann_visualizations(a=0.0, b=3.0, N=10)
