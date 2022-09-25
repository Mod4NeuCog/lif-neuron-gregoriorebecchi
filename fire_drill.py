import numpy as np
import matplotlib.pyplot as plt
import math

class human: 
    def __init__(self): 
        self.thresh = 50 #highest temperature tolerated on the skin before the reflex
        self.tenvironment = 20 #temperature in the environment (default value 20°C)
        self.temp = 20 #starting temperature on the skin (default value 20°C)
        self.temptotal = np.full([100, 1], 0, float)
        self.tempincrease = 0 #temperature modification in delta t
        self.tempfire = 80 #heat source temperature 
        self.reflex = 0 # self.reflex=0 if reflex did not occur yet, =1 if it hapened
        self.time = 0
        
    def timedheatreflex(self) :
        for t in range (100) :
            if self.temp<self.thresh and self.reflex == 0: #no reflex condition, temperature increasing
                self.tempincrease = (self.tempfire-self.temp)/(self.temp) #gradient of temperature increase on the skin, assuming that it is directly connected to the sensorial neurons
                self.temp = self.tempincrease + self.temp
                self.temptotal[t] = self.temp
                self.time = self.time +1
                
            else:
                self.tempincrease = (self.temp -self.tenvironment)/self.temp #decreasing gradient temperature, depending on environment temperature 
                self.temp = self.temp - self.tempincrease
                self.temptotal[t] = self.temp
                self.time = self.time +1
                self.reflex = 1
            
human1 = human()

human1.timedheatreflex()

plt.ylim([10, 60])
plt.plot(human1.temptotal)
