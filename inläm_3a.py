import numpy as np
import matplotlib.pyplot as plt

def x_position(V0, alfa, tid):
    return V0 * tid * np.cos(alfa)

def y_position(V0, alfa, tid, g):
    return V0 * tid * np.sin(alfa) - (g / 2) * tid**2

def kastparabel(V0, alfa, g, dt):
    airtime = 2 * V0 * np.sin(alfa) / g
    tid = np.arange(0, airtime, dt)
    x_distans = x_position(V0, alfa, tid)
    y_distans = y_position(V0, alfa, tid, g)
    return x_distans, y_distans

def huvudprogram():
    while True:
        grader = input("Ange grader: ")
        grader = float(grader)
        V0 = input("Ange utgångshastigheten: ")

        plt.figure(figsize=(5, 4))
        plt.ion()
        plt.xlabel("Längd (m)")
        plt.ylabel("Höjd (m)")
        plt.title("Kastparabel")
        plt.grid(True)

        V0 = float(V0)
        g = 9.81
        alfa = np.radians(grader)
        x_distans, y_distans = kastparabel(V0, alfa, g, 0.005)
        
        plt.plot(x_distans, y_distans)
        plt.vlines (x=15, ymin=0, ymax=5)
        plt.draw()
        plt.show()

        bra = input("Är du nöjd med resultatet? (ja/nej): ").strip().lower()
        if bra == "ja":
            break
        else: 
            print("ange nya värden.")

huvudprogram()

#grader=40 och hastighet = 15.8