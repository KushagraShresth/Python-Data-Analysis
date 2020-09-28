#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[32]:


df=pd.DataFrame({'Time(years)':[0.0,0.5,1,1.5,2.0], 'Reservoir Pressure(psia)':[1798,1680,1540,1428,1335],
                 'Z':[0.869,0.870,0.880,0.890,.900],'Cumulative Gas Produced Gp(MMSCF)':[0.00,0.96,2.12,3.21,3.92]})
df


# In[6]:


df['P/Z']=df['Reservoir Pressure(psia)']/df['Z']
df


# In[26]:


x=df['Cumulative Gas Produced Gp(MMSCF)']
y=df['P/Z']
plt.scatter(x,y,marker='o', color='green')
plt.xlabel('Cumulative Gas Produced Gp(MMSCF)')
plt.ylabel('P/Z')
plt.title('Gas Material Balance')


# In[8]:


model= np.polyfit(x,y, 1)
model


# In[9]:


PZZ = np.arange(2070.38439919,0,-1)
GPP = (PZZ-2070.38439919)/-148.2874553


# In[10]:


Df=pd.DataFrame({'Cumulative Gas Produced Gp(MMMSCF)':GPP, "P/Z": PZZ})
Df


# In[11]:


Df['P/Z']


# In[21]:


Initial_gas_in_place=(0-2070.38439919)/-148.2874553
Initial_gas_in_place
G=Initial_gas_in_place
G


# In[31]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10,7))
plt.plot(Df['Cumulative Gas Produced Gp(MMMSCF)'][1:700], Df['P/Z'][1:700])
plt.plot(Df['Cumulative Gas Produced Gp(MMMSCF)'][700:2071], Df['P/Z'][700:2071], ls='-.')
plt.scatter(x,y,marker = 'o',color = 'green',label = "Gas Produced Gp")
plt.scatter(G,5, label = "Initial Gas in Place G")
plt.xlim(0,18)
plt.ylim(1,2200)
plt.axvspan(0,4,alpha=0.5,label='Production History', color='aquamarine')
plt.xlabel("Cumulative Gas Production 'Gp' (MMMSCF)")
plt.ylabel("P/Z")
plt.title("Gas Material Balance")
plt.legend(loc='upper right')
plt.show()
print("The Gas Initially in place is",G,"MMMSCF")

