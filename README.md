
📐 MIT 18.01: Applied Single-Variable Calculus
"Calculus is the mathematical language of a changing universe."

Welcome to MIT 18.01 Applied. This repository reimagines MIT’s single-variable calculus curriculum through a practical, historical, and computational lens.

Instead of treating calculus as a collection of algebraic tricks or abstract proofs, this repo grounds every concept in physical reality, real-world engineering failures, historical genius, and executable Python code.

💡 The Grand Unifying Idea: What Is Calculus?
Before calculus, mathematics was largely static—it measured fixed shapes, constant speeds, and settled balances. But the real world is dynamic:

Objects accelerate under gravity.
Electrical currents surge and dissipate.
Financial systems fluctuate continuously.
Planetary orbits curve under changing forces.
Calculus was invented to solve two fundamental problems that static algebra and geometry could not touch:

1. THE TANGENT PROBLEM (Differential Calculus)
   "If something is constantly changing, how fast is it changing RIGHT NOW?"
   --> Zoom in on a curve until it looks like a straight line.

2. THE AREA PROBLEM (Integral Calculus)
   "If rates of change vary at every instant, how much accumulates OVER TIME?"
   --> Break a complex shape into infinite tiny slices and add them up.
♟️ The 3 Cs Framework: Human Intuition Meets Mathematics
Standard textbooks often obscure calculus behind endless derivative tables. This repository relies on three core mental models to connect abstract operations to real-world thinking:


 ┌───────────────────────────────────────────────────────────────────────────┐
 │                            THE 3 Cs FRAMEWORK                             │
 ├──────────────────────────┬───────────────────────┬────────────────────────┤
 │    1. CHAIN-BREAKING     │       2. CHESS        │       3. COOKING       │
 │   (Unraveling Systems)   │  (Optimal Strategy)   │    (Reconstruction)    │
 ├──────────────────────────┼───────────────────────┼────────────────────────┤
 │ Linearizes products,     │ Evaluates state &     │ Unbakes the cake;      │
 │ ratios, & compositions   │ finds equilibrium     │ solves inverse systems │
 │ d(uv) = u dv + v du      │ dy/dx = 0             │ dx/dy = 1/(dy/dx)      │
 └──────────────────────────┴───────────────────────┴────────────────────────┘


1. Chain-Breaking (Mixed Signals):
The Mixed Signals Problem: Real-world systems fuse completely different mathematical species together (e.g., an exponential decay e−kt multiplying a harmonic oscillator sin(ωt)).

The Calculus Solution: Calculus acts as a delicate untangler. Through local linearity, rules like the Product Rule d(uv)=udv+vdu and Chain Rule dydx=dydu⋅dudx break these tangled chains down into simple, additive linear pieces.

2. Chess: Strategic Evaluation & Equilibrium
The Strategic Analogy: A grandmaster doesn't calculate every variation to checkmate; they evaluate positional balance to find where their advantage peaks before over-extension creates weaknesses.

The Calculus Solution: Finding critical points where dydx=0 performs the exact same positional evaluation. It locates the precise equilibrium points where marginal gain balances marginal loss—whether that is finding maximum rocket trajectory height or minimizing structural stress.

3. Cooking: Inverse Functions & Geometric Reconstruction
The Reconstruction Problem: Cooking is a forward function (Ingredients+Heat→Finished Dish). Signal processing, medical imaging, and machine learning face the inverse problem: given the output observation, how do you reconstruct the exact original inputs?

The Calculus Solution: Forward functions compute outputs from inputs. Inverse functions work like taste-testing a dish to deduce the original recipe. Geometrically, the slope of an inverse function is always the reciprocal of the forward process (dxdy=1dydx).

🏛️ Standing on the Shoulders of Giants
This repo highlights the key thinkers who shaped how we think about change:

Mastermind	Core Contribution	Practical Intuition
John Napier (1614)	Continuous Logarithms	Modeled ratio-based continuous motion before calculus existed.
Gottfried Leibniz (1684)	Differential Notation (dx,dy)	Saw curves as polygons with infinitely small sides. Gave us modern notation.
Leonhard Euler (1748)	Operational Analysis & Methods	Treated calculus as an engine for physics, differential equations, and series.
Cauchy & Weierstrass (1820s)	Limit Rigor (ϵ-δ)	Transformed 'infinitesimals' into rigorous thresholds and tolerances.
mit-1801-applied-calculus/
│
├── README.md                          # Master index & project vision
├── 01-limits-and-continuity.md         # Foundation module
├── 02-derivatives-and-rates.md         # Motion & Leibniz notation
├── 03-linear-approximation.md         # Euler's method & square root limits
├── 04-optimization-and-physics.md     # MIT Pumpkin Toss & trajectory
├── 05-integration-and-accumulation.md  # Area under curve & Napier logs
│
├── code/                              # Runnable Python scripts
│   ├── 01_limits_demo.py
│   └── 02_derivative_sim.py
└── assets/                            # Generated charts for Markdown display
    └── 01_sin_x_over_x.png

🚀 How to Run the Code
1. Clone the repository:

git clone https://github.com/your-username/mit-1801-applied-calculus.git
cd mit-1801-applied-calculus
2. Set up environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install numpy matplotlib
3. Run a module script:

python code/01_limits_demo.py
📜 Attribution & Disclaimers
Educational Inspiration: This project is inspired by the curriculum and pedagogical insights of MIT 18.01 (Single Variable Calculus), originally taught by faculty including Prof. David Jerison and Prof. Haynes Miller on MIT OpenCourseWare.

License Compliance: Content derived from or inspired by MIT OpenCourseWare is shared under the CC BY-NC-SA 4.0 license.

Disclaimer: This repository is an independent, non-commercial educational project created for self-study and open-source learning. It is not officially affiliated with, endorsed by, or sponsored by the Massachusetts Institute of Technology (MIT).

"Calculus is not about memorizing derivative rules—it is about learning to view the world through continuous change."
