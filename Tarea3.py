#!/usr/bin/env python
# coding: utf-8

# In[1]:


from MasaResorte import * #Importamos el archivo en el que está la clase.


# In[3]:


Oscilador1=Oscilador(0.02,12,1.4,0.0) #Definimos cinco osciladores armónicos simples con parámetros distintos.
Oscilador2=Oscilador(0.05,15,2.0,0.0)
Oscilador3=Oscilador(0.02,20,1.7,0.0)
Oscilador4=Oscilador(0.08,15,1.2,0.0)
Oscilador5=Oscilador(0.01,17,2.3,0.0)
y1=[] #Creamos listas de y vacías para añadir los elementos respectivos a un intervalo de tiempo.
y2=[]
y3=[]
y4=[]
y5=[]
v1=[]#Creamos listas de v vacías para añadir los elementos respectivos a un intervalo de tiempo.
v2=[]
v3=[]
v4=[]
v5=[]
ti=list(np.arange(0,2,0.01))
for i in ti:
    y1.append(Oscilador1.y(i)) #Añadimos los respectivos valores.
    y2.append(Oscilador2.y(i))
    y3.append(Oscilador3.y(i))
    y4.append(Oscilador4.y(i))
    y5.append(Oscilador5.y(i))
    v1.append(Oscilador1.v(i))
    v2.append(Oscilador2.v(i))
    v3.append(Oscilador3.v(i))
    v4.append(Oscilador4.v(i))
    v5.append(Oscilador5.v(i))

plt.figure(figsize=(10, 8)) #Graficamos y vs t.
plt.title("Osciladores armónicos simples.(y vs t)",fontsize=20)
plt.plot(ti,y1,c="blue",label="Oscilador 1.")
plt.plot(ti,y2,c="purple",label="Oscilador 2.")
plt.plot(ti,y3,c="magenta",label="Oscilador 3.")
plt.plot(ti,y4,c="cyan",label="Oscilador 4.")
plt.plot(ti,y5,c="palegreen",label="Oscilador 5.")
plt.ylabel("y", fontsize=20)
plt.xlabel("t", fontsize=20)
plt.axhline(0.0,c="k")
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(10, 8)) #Graficamos v vs y.
plt.title("Osciladores armónicos simples.(v vs y)",fontsize=20)
plt.plot(y1,v1,c="blue",label="Oscilador 1.")
plt.plot(y2,v2,c="purple",label="Oscilador 2.")
plt.plot(y3,v3,c="magenta",label="Oscilador 3.")
plt.plot(y4,v4,c="cyan",label="Oscilador 4.")
plt.plot(y5,v5,c="palegreen",label="Oscilador 5.")
plt.ylabel("v", fontsize=20)
plt.xlabel("y", fontsize=20)
plt.axhline(0.0,c="k")
plt.grid()
plt.legend()
plt.show()


# In[4]:


Oscilador_amort1=Oscilador(0.02,15,2.0,10) #Definimos cinco osciladores amortiguados con parámetros distintos.
Oscilador_amort2=Oscilador(0.05,19,1.4,15)
Oscilador_amort3=Oscilador(0.03,15,0.9,16)
Oscilador_amort4=Oscilador(0.1,11,1.3,6)
Oscilador_amort5=Oscilador(0.02,13,1.7,4)
y1=[] #Creamos listas de y vacías para añadir los elementos respectivos a un intervalo de tiempo.
y2=[]
y3=[]
y4=[]
y5=[]
v1=[] #Creamos listas de v vacías para añadir los elementos respectivos a un intervalo de tiempo.
v2=[]
v3=[]
v4=[]
v5=[]
ti=list(np.arange(0,2,0.01))
for i in ti:
    y1.append(Oscilador_amort1.y(i)) #Añadimos los respectivos valores.
    y2.append(Oscilador_amort2.y(i))
    y3.append(Oscilador_amort3.y(i))
    y4.append(Oscilador_amort4.y(i))
    y5.append(Oscilador_amort5.y(i))
    v1.append(Oscilador_amort1.v(i))
    v2.append(Oscilador_amort2.v(i))
    v3.append(Oscilador_amort3.v(i))
    v4.append(Oscilador_amort4.v(i))
    v5.append(Oscilador_amort5.v(i))

plt.figure(figsize=(10, 8)) #Graficamos y vs t.
plt.title("Osciladores amortiguados.(x vs t)",fontsize=20)
plt.plot(ti,y1,c="blue",label="Oscilador amortiguado 1.")
plt.plot(ti,y2,c="purple",label="Oscilador amortiguado 2.")
plt.plot(ti,y3,c="magenta",label="Oscilador amortiguado 3.")
plt.plot(ti,y4,c="cyan",label="Oscilador amortiguado 4.")
plt.plot(ti,y5,c="palegreen",label="Oscilador amortiguado 5.")
plt.ylabel("y", fontsize=20)
plt.xlabel("t", fontsize=20)
plt.axhline(0.0,c="k")
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(10, 8)) #Graficamos v vs y.
plt.title("Osciladores armónicos amortiguados.(v vs y)",fontsize=20)
plt.plot(y1,v1,c="blue",label="Oscilador amortiguado 1.")
plt.plot(y2,v2,c="purple",label="Oscilador amortiguado 2.")
plt.plot(y3,v3,c="magenta",label="Oscilador amortiguado 3.")
plt.plot(y4,v4,c="cyan",label="Oscilador amortiguado 4.")
plt.plot(y5,v5,c="palegreen",label="Oscilador amortiguado 5.")
plt.ylabel("v", fontsize=20)
plt.xlabel("y", fontsize=20)
plt.axhline(0.0,c="k")
plt.grid()
plt.legend()
plt.show()


# In[ ]:




