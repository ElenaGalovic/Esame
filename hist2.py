import matplotlib.pyplot as plt
import numpy as np
import sys

data_hist=sys.argv[1]

data=np.loadtxt(data_hist, delimiter=' ', usecols=(0, 1, 12), unpack=True)

MsuH = data[0]        #Metalicità
m_ini = data[1]       #Massa iniziale
age_parent = data[2]  #Età della stella 

#Definiamo i limiti per tre bin diversi
boundary_1 = 1
boundary_2 = 5

#Dividiamo i nostri dati in tre bin usando i limiti sopra definiti
mass_bin1 = m_ini[age_parent < boundary_1]
MsuH_bin1 = MsuH[age_parent < boundary_1]

mass_bin2 = m_ini[(age_parent >= boundary_1) & (age_parent <= boundary_2)]
MsuH_bin2 = MsuH[(age_parent >= boundary_1) & (age_parent <= boundary_2)]

mass_bin3 = m_ini[age_parent >= boundary_2]
MsuH_bin3 = MsuH[age_parent >= boundary_2]

#Plottiamo il grafico
plt.figure(figsize=(10, 6))

#Distribuzione per bin1
plt.scatter(mass_bin1, MsuH_bin1, alpha=0.5, label='<1 Gyr')

#Distribuzione per bin2
plt.scatter(mass_bin2, MsuH_bin2, c='lightcoral', alpha=0.5, label='1-5 Gyr')

#Distribuzione per bin3
plt.scatter(mass_bin3, MsuH_bin3, c='forestgreen', alpha=0.5, label='>5 Gyr')

plt.ylabel('Metalicità')
plt.xlabel('Massa iniziale (Massa solare)')
plt.title('Distribuzione della metalicità in funzione della massa iniziale')
plt.legend()

#Ci mostra il grafico
plt.grid(True)
plt.show()
