import math
import matplotlib.pyplot as plt
import numpy as np
import random
def doEulers():
    #constants
    a = 0.02
    b = 0.2
    c = -65
    d = 8

    V_rest = -75
    V_th = 30
    T = 1000
    dt = .01
    num_points = int(T/dt) + 1
    V = np.zeros([num_points])
    U = np.zeros([num_points])
    I = 5
    V[0] = V_rest
    t_values = np.linspace(0,T,num_points)
    U[0] =  -18
    for i in range(1,num_points):
        if i < .10 * num_points:
            I = 3
        elif i>.10*num_points and i <.40* num_points:
            I = 6
        elif i > .40*num_points and i < .60 * num_points:
            I = 10
        else:
            I = 13
        if V[i-1] > V_th:
            V[i] = c
            U[i] += U[i-1] +  d
        else:
            V[i] = V[i-1] + dt*(.04 * V[i-1] * V[i-1] + 5*V[i-1] + 140 - U[i-1] + I)
            U[i] = U[i-1] + dt*a*(b * V[i-1] - U[i-1])

    plt.plot(t_values,V)
    plt.xlabel("ms")
    plt.ylabel("Voltage in mV")
    plt.show()


    #eulers
doEulers()



    
