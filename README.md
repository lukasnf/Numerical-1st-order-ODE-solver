## Numerical 1st Order ODE Solver

This project is a Python implementation for solving first-order ordinary differential equations (ODEs) numerically. The script allows users to choose between two methods: Euler's Method and Runge-Kutta 4th Order Method (RK4), providing a visual representation of the solution.

Features

Supports solving first-order ODEs of the form 
y
′
=
f
(
x
,
y
)
y 
′
 =f(x,y).
Offers two numerical methods:
Euler's Method
Runge-Kutta 4th Order Method (RK4)
Customizable parameters for initial conditions, accuracy, and range.
Visualizes the results using Matplotlib.
Requirements

Ensure the following Python libraries are installed:

matplotlib
sympy
Install missing dependencies using pip:

pip install matplotlib sympy
Usage

Clone the repository or copy the script.
Run the script in a Python environment:
python ode_solver.py
Follow the prompts to input:
The ODE to solve (e.g., x + y for 
y
′
=
x
+
y
y 
′
 =x+y).
The accuracy level (higher n yields better accuracy).
Range of the x-axis.
Initial conditions (
x
0
x 
0
​	
 , 
y
0
y 
0
​	
 ).
The method to use (euler or runge-kutta).
The script computes the solution and plots the result.
Example Input

Enter a function of x,y -> y'= x + y
How accurate should we solve the system? -> higher n results in higher accuracy 100
x-axis limitation: 10
Initial x-value: 0
Initial y-value: 1
Which method would you like to use? Type 'euler' for euler and 'runge-kutta' for rk4: runge-kutta
Example Output

The script will display a plot of the computed solution over the specified range.

How It Works

ODE Function: The user-provided ODE is parsed using sympy and converted to a numerical function using lambdify.
Numerical Methods:
Euler's Method: Iteratively computes the next value using the slope at the current point.
RK4: Provides higher accuracy by evaluating slopes at multiple points within each interval.
Visualization: The computed solution is plotted using Matplotlib.
Customization

You can modify the script to add more methods, adjust default parameters, or change visualization settings.

License

This project is open-source and free to use. Contributions and suggestions are welcome!

