
import numpy as np
import matplotlib.pyplot as plt
import math

class Neuron: #you create a new class
    def __init__(self): #define it (idk why)
        self.I = 200 # the "self" in front of the variables mean that they are related to the single object of the class, they're not true for all the objects
        self.gL = 10
        self.vrest = -75
        self.v_th = -65
        self.tau_m = 5
        self.t = 0 
        self.v_process = -75
        self.v_total = np.full([1000,1], 0, float)
   
    def updatemembranepotential(self, spike_times) : #once you're done with the parameters definitions, you define also a fn that takes place in the "neuron" class 
        for t in range (1000) :
            if t in spike_times :
                
                self.I = 5500
        
            else:
                self.I = 0 
            
            if (self.v_process > -65):
               self.v_process = -75
            else: 
                self.d_vmembr_dt = (- (self.v_process - self.vrest)+ (self.I/self.gL))/self.tau_m
                self.v_process= self.v_process + self.d_vmembr_dt*0.1
            self.v_total[t] = self.v_process 
          
neuron1 = Neuron() # here you're saying that the object "neuron1" belongs to the class "Neuron" and has all the caracteristics 

spike_times = [1,400] #you define the spike times
neuron1.updatemembranepotential(spike_times) #you apply to "neuron1" the fn defined before (membrane potential function), checking the spike times

print(neuron1.v_process) #stampi il v_process di neuron1. non devi mettere self perché hai già definito che si tratta del valore di uno specifico neurone (neuron1)
plt.plot(neuron1.v_total)