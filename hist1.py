import matplotlib.pyplot as plt
import numpy as np
import sys

data_hist=sys.argv[1]

data=np.loadtxt(data_hist, delimiter=' ', usecols=(0, 12), unpack=True)

MsuH = data[0]       #Metalicità
age_parent = data[1]  #Età della stella 

#Definiamo i limiti per tre bin diversi
boundary_1 = 1
boundary_2 = 5

#Dividiamo i nostri dati in tre bin usando i limiti sopra definiti
age_bin1 = MsuH[age_parent < boundary_1]
age_bin2 = MsuH[(age_parent >= boundary_1) & (age_parent <= boundary_2)]
age_bin3 = MsuH[age_parent >= boundary_2]

#Plottiamo il grafico
plt.figure(figsize=(10, 6))

#Histogramma per bin1
plt.hist(age_bin1, bins=40, alpha=0.5, label='<1 Gyr')

#Histogramma per bin2
plt.hist(age_bin2, bins=40, alpha=0.5, label='1-5 Gyr')

#Histogramma per bin3
plt.hist(age_bin3, bins=40, alpha=0.5, label='>5 Gyr')

#Calcoliamo la media e la mediana per ogni bin
avg_bin1 = np.mean(age_bin1)
median_bin1 = np.median(age_bin1)

avg_bin2 = np.mean(age_bin2)
median_bin2 = np.median(age_bin2)

avg_bin3 = np.mean(age_bin3)
median_bin3 = np.median(age_bin3)

#Plotiamo linee verticali per la media e la mediana
plt.axvline(x=avg_bin1, color='royalblue', linestyle='--', label=f'Avg1: {avg_bin1:.2f}')
plt.axvline(x=median_bin1, color='navy', linestyle='--', label=f'Median1: {median_bin1:.2f}')

plt.axvline(x=avg_bin2, color='r', linestyle='--', label=f'Avg2: {avg_bin2:.2f}')
plt.axvline(x=median_bin2, color='darkred', linestyle='--', label=f'Median2: {median_bin2:.2f}')

plt.axvline(x=avg_bin3, color='greenyellow', linestyle='--', label=f'Avg3: {avg_bin3:.2f}')
plt.axvline(x=median_bin3, color='g', linestyle='--', label=f'Median3: {median_bin3:.2f}')

plt.xlabel('Metalicità')
plt.ylabel('Frequenza')
plt.title('Distribuzione della metalicità a secondo della età stellare')
plt.legend()

#Ci mostra il grafico
plt.grid(True)
plt.show()
