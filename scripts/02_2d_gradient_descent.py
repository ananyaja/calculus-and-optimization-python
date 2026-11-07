"""
2D Gradient Descent Optimization with Contour Plot Visualization
---------------------------------------------------------------
Objective: Minimize the 2D Rosenbrock/Quadratic Loss Surface
Function: f(x, y) = x^2 + 2*y^2
Gradients: df/dx = 2x, df/dy = 4y
Saves: Contour plot trajectory and loss curve to assets/
"""

import numpy as np
import matplotlib.pyplot as plt

def loss_function(x, y):
    """2D Elliptic Paraboloid Loss Surface: f(x, y) = x^2 + 2*y^2"""
    return x**2 + 2 * (y**2)

def compute_gradients(x, y):
    """Partial derivatives: [df/dx, df/dy]"""
    df_dx = 2 * x
    df_dy = 4 * y
    return df_dx, df_dy

def run_2d_gradient_descent(start_x=4.0, start_y=3.0, lr=0.1, epochs=30):
    x, y = start_x, start_y
    history_x, history_y, history_loss = [x], [y], [loss_function(x, y)]

    print(f"--- Starting 2D Gradient Descent at (x={x:.2f}, y={y:.2f}) ---")

    for i in range(1, epochs + 1):
        grad_x, grad_y = compute_gradients(x, y)
        x = x - lr * grad_x
        y = y - lr * grad_y
        loss = loss_function(x, y)

        history_x.append(x)
        history_y.append(y)
        history_loss.append(loss)

        if i % 5 == 0 or i == 1:
            print(f"Epoch {i:02d} | x: {x:8.4f} | y: {y:8.4f} | Loss: {loss:8.4f}")

    return np.array(history_x), np.array(history_y), np.array(history_loss)

def plot_optimization_results(hx, hy, hloss):
    """Generates and saves a 2D contour plot and loss convergence curve."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # 1. 2D Contour Plot
    x_range = np.linspace(-5, 5, 200)
    y_range = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x_range, y_range)
    Z = loss_function(X, Y)

    contours = ax1.contour(X, Y, Z, levels=30, cmap='viridis', alpha=0.8)
    ax1.clabel(contours, inline=True, fontsize=8)

    # Plot gradient descent path
    ax1.plot(hx, hy, 'ro-', linewidth=2, markersize=5, label='Gradient Path')
    ax1.plot(hx[0], hy[0], 'go', markersize=9, label=f'Start ({hx[0]:.1f}, {hy[0]:.1f})')
    ax1.plot(0, 0, 'b*', markersize=12, label='Global Minimum (0,0)')

    ax1.set_title('2D Loss Surface Contour & Gradient Steps', fontsize=12, fontweight='bold')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend()

    # 2. Loss Convergence Curve
    ax2.plot(hloss, 'b-o', linewidth=2, markersize=4, color='darkblue')
    ax2.set_title('Loss vs. Iterations (Convergence)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss f(x,y)')
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plot_path = "assets/02_2d_gradient_descent_contour.png"
    plt.savefig(plot_path, dpi=300)
    plt.close()
    print(f"\n✅ Contour plot successfully saved to: {plot_path}")

if __name__ == "__main__":
    hx, hy, hloss = run_2d_gradient_descent(start_x=4.0, start_y=3.0, lr=0.1, epochs=30)
    plot_optimization_results(hx, hy, hloss)
