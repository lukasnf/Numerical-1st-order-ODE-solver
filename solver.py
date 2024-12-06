import matplotlib.pyplot as plt
import sympy as sp

func = input("Enter a function of x,y -> y'=").strip()
n = int(input("How accurate should we solve the system? -> higher n results in higher accuracy").strip())
b = float(input("x-axis limitation:").strip())
x0 = float(input("Initial x-value:").strip())
y0 = float(input("Initial y-value:").strip())
user = str(input("Which method would you like to use? Type 'euler' for euler and 'runge-kutta' for rk4:").strip())

def function(func):
    func = sp.sympify(func)
    f = sp.lambdify((x,y), func)
    return f

def runge_kutta4(f,x0,y0,n,a,b):
    y = [y0]
    x = [x0]
    h = (b-a)/n
    for i in range(n):
        k1 = h * f(x[-1],y[-1])
        k2 = h * f(x[-1]+h/2,y[-1]+k1/2)
        k3 = h * f(x[-1]+h/2,y[-1]+k2/2)
        k4 = h * f(x[-1]+h,y[-1]+k3)

        y_r = y[-1]+(k1+2*k2+2*k3+k4)/6
        x_r = x[-1]+h

        x.append(x_r)
        y.append(y_r)

    return x,y

def euler(f,x0,y0,n,a,b):
    y = [y0]
    x = [x0]
    h = (b-a)/n
    for i in range(n):
        y_e = y[-1]+h*f(x[-1],y[-1])
        x_e = x[-1]+h

        x.append(x_e)
        y.append(y_e)

    return x,y


f = function(func)

if user == "runge-kutta":
    x,y = runge_kutta4(f,x0,y0,n,0,b)

else: x,y = euler(f,x0,y0,n,0,b)


plt.plot(x,y,label = f"{user.capitalize()}")
plt.grid()
plt.title("Numerical 1st order ODE solver")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()