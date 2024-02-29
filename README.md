Nella repository sono stati scaricati tutti i file necesari per far partire il programma. Lo script "installazione.sh" crea la directory "dir_esame" dove lo script "esecuzione.sh" e i file Python vengono coppiati e attribuisce I permessi di esecuzione. Lo script "esecuzione.sh" scarica i dati che contengono le proprietà di un gruppo di stelle dalla repository su github dove sono stati salvati. In piu fornisce i dati ai tre file Python per creare i grafici. Nel file "HR.py" i dati vengono usati per creare il grafico di magnitudine assoluta in funzione di indice di colore B-V. I dati sono suddivisi in 35 gruppi di età e indicati in legenda con diversi colori. Il secondo file python "hist1.py" crea tre istogrammi a secondo dell'età stellare che mostrano le metalicità stellari per tre sotto-campioni. Con le linee verticali vengono riportate la media e la mediana per ogni distribuzione con i valori che si possono leggere dalla legenda. L'ultimo file "hist2.py" crea il grafico che mostra il legame tra metallicità e massa iniziale delle stelle per i tre sotto-campioni di età precedentemente studiati. Per vedere come funziona intero programma bisogna scaricare tutti i file nella stessa cartella, aprire il terminale da quella cartella e lanciare lo scrpt di installazione con il comando: ' ./installazione.sh' Il programma mostra il primo dei trei grafici, senza ulteriori passaggi, mentre per visualizzare gli altri due grafici è necessario chiudere la finestra proposta e automaticamente viene aperto il secondo grafico, poi chiudendo quello viene direttamente apperto l'ultimo grafico.
