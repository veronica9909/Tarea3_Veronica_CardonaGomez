#!/usr/bin/env python
# coding: utf-8

# In[55]:


from sympy import Symbol
import numpy as np
import matplotlib.pyplot as plt


# In[75]:



class Oscilador:
    
    
    def __init__(self,y0,k,m,gamma):#Inicializamos.
        self.y0=float(y0)
        self.k=float(k)
        self.m=float(m)
        self.gamma=float(gamma)
        self.w=float(k/m)
    
    def y(self,t): #Definimos la función y.
        self.t=float(t)
        return (self.y0)*(np.e**(-1*(self.gamma*self.t)/2))*(np.cos(self.w*self.t))
    
    def v(self,t):#Definimos la velocidad para el caso simple y para el caso amortiguado.
        self.t=float(t)
        if self.gamma==0:
             return -1*(self.y0)*(self.w)*(np.sin(self.w*self.t))
        else:
            return (self.gamma/2)*(self.y0)*(np.e**(-1*(self.gamma*self.t)/2))*(self.w)*(np.sin(self.w*self.t)) 

           
    


# In[ ]:




