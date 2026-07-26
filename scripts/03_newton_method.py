"""
18.01 Single Variable Calculus: Newton-Raphson Root Finding Algorithm
----------------------------------------------------------------------
Objective: Find the root of f(x) = x^2 - 2 (i.e., compute sqrt(2))
Formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
Features: Symbolic differentiation via SymPy & convergence visualization
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def run_newton_method(start_x=5.0, iterations=6):
    # 1. Define symbolic variable and function
    x_sym = sp.Symbol('x')
    f_sym = x_sym**2 - 2
    df_sym = sp.diff(f_sym, x_sym)

    # Convert symbolic expressions to numerical Python functions
    f = sp.lambdify(x_sym, f_sym, 'numpy')
    df = sp.lambdify(x_sym, df_sym, 'numpy')

    x_val = start_x
    history_x = [x_val]
    history_error = [abs(x_val - np.sqrt(2))]

    print(f"--- Newton-Raphson Root Finding for f(x) = x^2 - 2 ---")
    print(f"Goal: Find sqrt(2) ≈ {np.sqrt(2):.10f}\n")
    print(f"Iter 00 | x = {x_val:12.8f} | Error = {history_error[0]:12.8f}")

    for i in range(1, iterations + 1):
        # Newton update step: x_{n+1} = x_n - f(x_n) / f'(x_n)
        x_val = x_val - f(x_val) / df(x_val)
        err = abs(x_val - np.sqrt(2))

        history_x.append(x_val)
        history_error.append(err)

        print(f"Iter {i:02d} | x = {x_val:12.8f} | Error = {err:12.8f}")

    return history_x, history_error

def plot_newton_convergence(history_x, history_error):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Plot 1: Function f(x) and root approximations
    x_range = np.linspace(0.5, 5.5, 300)
    y_range = x_range**2 - 2

    ax1.plot(x_range, y_range, 'b-', label='f(x) = x^2 - 2', linewidth=2)
    ax1.axhline(0, color='black', linestyle='--', alpha=0.7)
    ax1.plot(history_x, [x**2 - 2 for x in history_x], 'ro-', markersize=6, label='Newton Iterations')
    ax1.axvline(np.sqrt(2), color='green', linestyle=':', label='True sqrt(2)')

    ax1.set_title('Newton-Raphson Trajectory on f(x)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend()

    # Plot 2: Quadratic Error Reduction (Log Scale)
    ax2.plot(history_error, 'm-s', linewidth=2, markersize=6)
    ax2.set_yscale('log')
    ax2.set_title('Quadratic Convergence (Error vs Iteration)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Absolute Error |x_n - sqrt(2)| (Log Scale)')
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plot_path = "assets/03_newton_method_convergence.png"
    plt.savefig(plot_path, dpi=300)
    plt.close()
    print(f"\n✅ Newton-Raphson plot successfully saved to: {plot_path}")

if __name__ == "__main__":
    hx, herr = run_newton_method(start_x=5.0, iterations=6)
    plot_newton_convergence(hx, herr)
