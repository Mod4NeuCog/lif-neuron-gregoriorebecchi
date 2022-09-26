class Neuron :
    def __init__(self): #init: you give starting values 
        self.vmembr=-70
        
    def main(self):
       self.nnexcsyn = input('How many excitatory synapsis are considered? ')
       self.nnexcsyn = int(self.nnexcsyn)
       self.nninhsyn = input('How many inhibitory synapsis are considered? ') 
       self.nninhsyn = int(self.nninhsyn)
       self.vmembr=self.vmembr+5*self.nnexcsyn-3*self.nninhsyn
       if self.vmembr>-65:
               self.outcome = 'The threshold has been passed, the neuron will fire'
               print('Final membrane value =',self.vmembr, self.outcome)
       else: 
                self.outcome = 'The threshold has not been passed, the neuron will not fire'
                print('Membrane value =',self.vmembr, self.outcome)
                
Neuron1 = Neuron()
Neuron1.main()
