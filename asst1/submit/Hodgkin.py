import matplotlib.pyplot as plt
import numpy as np
import random
def alpha_n(Vm):
    return (0.01 * (10.0 - Vm)) / (np.exp(1.0 - (Vm/10)) - 1.0)

def beta_n(Vm):
    return 0.125 * np.exp(-Vm / 80.0)


def alpha_m(Vm):
    return (0.1 * (25.0 - Vm)) / (np.exp(2.5 - (Vm/10)) - 1.0)

def beta_m(Vm):
    return 4.0 * np.exp(-Vm / 18.0)

def alpha_h(Vm):
    return 0.07 * np.exp(-Vm / 20.0)

def beta_h(Vm):
    return 1.0 / (np.exp(3.0 - (Vm/10)) + 1.0)
def doEulers():
    #constants

    V_rest = 0
    Cm = 1
    Vna = 115
    Vk = -12
    Vl = 10.613
    gna = 120
    gk = 36
    gl = .3

    T = 100
    dt = .01
    num_points = int(T/dt) + 1
    V = np.zeros([num_points])
    h = np.zeros([num_points])
    m = np.zeros([num_points])
    n = np.zeros([num_points])
    I = 50
    V[0] = V_rest
    n[0] = alpha_n(V_rest) /(alpha_n(V_rest) + beta_n(V_rest)) 
    m[0] = alpha_m(V_rest)/ (alpha_m(V_rest) +  beta_m(V_rest))
    h[0] = alpha_h(V_rest)/ ( alpha_h(V_rest) + beta_h(V_rest))
    t_values = np.linspace(0,T,num_points)
    for i in range(1,num_points):
        #spike who knows how this works
        V[i] = V[i-1] + dt*((I-gk*n[i-1]**4 *(V[i-1] - Vk) - gna * m[i-1]**3 *h[i-1]*(V[i-1] -  Vna) - gl*(V[i-1] - Vl))/Cm) 
        n[i] = n[i-1]+ dt*(alpha_n(V[i-1]) *(1-n[i-1]) - beta_n(V[i-1]) * n[i-1]);
        m[i] = m[i-1]+ dt*(alpha_m(V[i-1]) *(1-m[i-1]) - beta_m(V[i-1]) * m[i-1]);
        h[i] = h[i-1]+ dt*(alpha_h(V[i-1]) *(1-h[i-1]) - beta_h(V[i-1]) * h[i-1]);

    plt.plot(t_values,V)
    plt.xlabel("time in ms")
    plt.ylabel("mv")
    plt.show()


    #eulers
doEulers()



    
