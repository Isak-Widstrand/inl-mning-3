import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=10):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        f_prime_x = f_prime(x)
        
        if f_prime_x == 0:
            return 0, False
        
        x_new = x - fx / f_prime_x
        
        if abs(x_new - x) < tol:
            return x_new, True
        
        x = x_new
        
    return 0, False

def f(x):
    return x**2 - 1 - np.exp(x)/3

def f_prime(x):
    return 2*x - np.exp(x)/3

def test_startgissningar(f, f_prime, x0, tol=1e-6):
    for i in range(10):
        root, konvergerad = newton_raphson(f, f_prime, x0, tol)
        if konvergerad:
            print(f"Lösning hittades för startgissning {x0}: {root}")
        else:
            print(f"Newton-Raphson konvergerade inte för startgissning {x0}")
        
        x0 += 1

x_vals = np.linspace(-3, 3, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title("Graf")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

startgissning = -2
test_startgissningar(f, f_prime, startgissning)