

import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("scripts", exist_ok=True)
os.makedirs("assets", exist_ok=True)

def f(x):
    return x**2

def trapezoid_rule(a, b, N):
    x = np.linspace(a, b, N + 1)
    y = f(x)
    dx = (b - a) / N
    return (dx / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpsons_rule(a, b, N):
    if N % 2 != 0:
        N += 1  # Simpson's rule requires an even number of intervals
    x = np.linspace(a, b, N + 1)
    y = f(x)
    dx = (b - a) / N
    return (dx / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

# Parameters
a, b, N = 0.0, 3.0, 10
exact = 9.0

trap_val = trapezoid_rule(a, b, N)
simp_val = simpsons_rule(a, b, N)

print(f"--- Advanced Numerical Integration (N={N}) ---")
print(f"Exact Analytical Integral : {exact:.8f}")
print(f"Trapezoidal Rule Approximation : {trap_val:.8f} | Absolute Error: {abs(exact - trap_val):.8f}")
print(f"Simpson's 1/3 Rule Approximation: {simp_val:.8f} | Absolute Error: {abs(exact - simp_val):.8f}")

# Visualization Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Trapezoids under the curve
x_curve = np.linspace(a, b, 200)
x_trap = np.linspace(a, b, N + 1)

ax1.plot(x_curve, f(x_curve), 'b-', linewidth=2, label='f(x) = x^2')
ax1.fill_between(x_trap, f(x_trap), color='purple', alpha=0.2, label='Trapezoids')
ax1.plot(x_trap, f(x_trap), 'ro--', label='Linear Slopes')
ax1.set_title(f'Trapezoidal Rule Area (N={N})', fontsize=12, fontweight='bold')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend()

# Plot 2: Error Convergence Comparison
n_values = np.arange(2, 22, 2)
trap_errors = [abs(exact - trapezoid_rule(a, b, n)) for n in n_values]
simp_errors = [abs(exact - simpsons_rule(a, b, n)) for n in n_values]

ax2.plot(n_values, trap_errors, 's-', color='purple', label='Trapezoidal Error')
ax2.plot(n_values, simp_errors, 'o-', color='green', label="Simpson's Error (Exact)")
ax2.set_yscale('log')
ax2.set_title('Error Convergence Comparison (Log Scale)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Number of Intervals (N)')
ax2.set_ylabel('Absolute Error')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend()

plt.tight_layout()
plot_path = "assets/05_trapezoid_and_simpson.png"
plt.savefig(plot_path, dpi=300)
plt.close()
print(f"\n✅ Plot successfully saved to: {plot_path}")
