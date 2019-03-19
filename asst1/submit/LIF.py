import math
import matplotlib.pyplot as plt
import numpy as np
import random
def doEulers():
    #constants
    tau = 10/1000000
    V_reset=  -0.080
    V_rest = -0.075
    V_th = -0.040
    R_M =  10e6
    dt = 0.0002
    I_1 = .19
    I_2 = 1.0
    I_3 = 1.0
    T = 1
    num_points = int(T/dt) + 1
    V_m = np.zeros([num_points])
    t_values = np.linspace(0,T,num_points)
    V_m[0] = V_reset
    #eulers
    for i in range(1,num_points):
            if V_m[i-1] > V_th:
                V_m[i] = V_reset
            else:
                if i<.20*num_points:
                    I = I_1
                elif i>.20*num_points and i<.60*num_points:
                    I = I_2
                else:
                    I = I_3
                V_m[i] = V_m[i-1] + dt *(-1*(V_m[i-1]-V_rest) + I)
    plt.subplot(3, 1, 1)
    plt.plot(t_values,V_m)
    plt.title("Potential Decay Over Time")
    plt.ylabel('dv/dt')
    plt.xlabel('time')
    spikeY = [1 if  x >V_th  else 0 for x in V_m]
    plt.subplot(3, 1, 2)
    plt.plot(t_values,spikeY)
    plt.subplot(3, 1, 3)
    countNumFiresFirst = 0
    countNumFiresSecond = 0
    countNumFiresThird = 0
    for i in range(num_points):
        if(i<.20*num_points):
            if V_m[i] > V_th:
                countNumFiresFirst +=1

        elif(i>.20*num_points and i < .60*num_points):
            if V_m[i] > V_th:
                countNumFiresSecond +=1
        else:
            if V_m[i] > V_th:
                countNumFiresThird +=1
    x = [I_1,I_2,I_3]
    y = [countNumFiresFirst/.2,countNumFiresSecond/.4,countNumFiresThird/.4]
    plt.plot(x,y)



        
    plt.show()

doEulers()



