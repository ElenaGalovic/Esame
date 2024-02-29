import matplotlib.pyplot as plt
import numpy as np
import sys

data_HR=sys.argv[1]
#'/home/s264413@DS.UNITS.IT/Desktop/storage/s264413/Abilita Informatiche e telematiche/28.11.2023./Nemo_6670.dat'
data=np.loadtxt(data_HR, delimiter=' ', usecols=(4, 8, 12), unpack=True)


M_ass = data[0]       #Magnitudine assoluta
b_y = data[1]         #Indice di colore B-V -> Banda U (Ultravioletto), Banda B (Blu), Banda V (Visibile) 
age_parent = data[2]  #Età della stella

age_bins = [0, 0.05, 0.11, 0.18, 0.25, 0.33, 0.41, 0.51, 0.61, 0.73, 0.85, 0.99, 1.14, 1.30, 1.48, 1.68, 1.89, 2.13, 2.39, 2.67, 2.99, 3.33, 3.70, 4.12, 4.57, 5.06, 5.60, 6.20, 6.85, 7.57, 8.35, 9.21, 10.15, 11.19, 12.32, 13.56]

# Mettiamo tutti i dati della colonna age_parent nei age_bin scitti sopra
age_categories = np.digitize(age_parent, bins=age_bins)

# Scegliamo il gruppo di colori che vogliamo usare
cmap = plt.get_cmap('jet')

plt.figure(figsize=(14, 11))

# Creiamo lo scatter plot per ogni age_bin
# Enumerate ci conta quante volte entriamo nel loop
#
#(i/(len(age_bins)-1) divide il numero totale di passi fatti nel loop con gli age_bins,-1 perchè ci servono 35 bins e nel age_bins abbiamo 36 numeri
for i, age_bin in enumerate(age_bins[:-1]):
    indices = np.where((age_categories >= i + 1) & (age_categories < i + 2))[0]
    plt.scatter(np.array(b_y)[indices], np.array(M_ass)[indices], color=cmap(i / (len(age_bins) - 1)), label=f'{age_bins[i]} Gyr-{age_bins[i+1]} Gyr', marker='.')

# Ci inverte l'asse y    
plt.gca().invert_yaxis()

# Limitiamo le assi
plt.ylim(8.2, -4)
plt.xlim(-0.1, 1)

# Scriviamo la legenda con lettere piccole
plt.legend(fontsize='small')

plt.xlabel('B-V Color Index')
plt.ylabel('Mass (Solar Masses)')
plt.title('Hertzsprung-Russell Diagram with Age Bins')

# Ci mostra il plot
plt.grid(True)
plt.show()

