import math
import matplotlib.pyplot as plt
import numpy as np
import random
class LIF:
        #constants
    def __init__(self,I):
            self.I = I
    
    def doEulers(self):
        output_curr = 0 
        prev = 0
        incrementor = 1.9e-2
        tau = 10e-3
        V_reset=  -0.080
        V_rest = -0.075
        V_th = -0.040
        R_M =  10e6
        dt = 0.0002
        curr  = V_reset
        prev_curr = None
        #eulers
        while True:
            if prev_curr != None and prev_curr > V_th:
                curr = V_reset
                prev_curr = curr
                #set prev current equal to outputcurrent
       
                #increment outputcurrent by incrementor
                output_curr += incrementor
                prev = output_curr
     
  
                yield (1,output_curr)
            else:
                #eulers stuff
                curr_old = curr
                if(prev_curr != None):
                    
                    curr = prev_curr + dt *(-1*(prev_curr -V_rest) + self.I)/tau
            
                prev_curr = curr_old
                #calculate declay
                decay =math.exp(-0.01)
                old_output = output_curr
                output_curr = prev * decay
                prev = old_output
                yield (0,output_curr)
    
            





