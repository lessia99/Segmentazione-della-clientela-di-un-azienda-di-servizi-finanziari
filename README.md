# Segmentazione-della-clientela-di-un-azienda-di-servizi-finanziari

Un'azienda di servizi finanziari sta investendo in una nuova campagna di marketing per per promuovere la propria linea di carte di credito.
L'obiettivo è quello di segmentare la clientela attuale indentificando dei cluster verso la quale l'azienda dovrà indirizzare apposite campagne di marketing.

## Descrizione allegati:

1.**credit_card_customers.csv**: dataset (link in fondo alla pagina) che contiene le seguenti informazioni su 9000 possessori di carte di credito dell'azienda:
- *CUST_ID*: Identificazione del titolare della carta di credito (Categorico)
- *BALANCE*: importo del saldo rimasto sul conto per effettuare acquisti
- *BALANCE_FREQUENCY*: frequenza di aggiornamento del saldo, punteggio tra 0 e 1 (1 = aggiornato frequentemente, 0 = non aggiornato frequentemente).
- *PURCHASES*: Quantità di acquisti effettuati dal conto
- *ONEOFF_PURCHASES*: Importo massimo di acquisti effettuati in un'unica soluzione
- *INSTALLMENTS_PURCHASES*: Importo degli acquisti effettuati a rate
- *CASH_ADVANCE*: Anticipo in contanti dato dall'utente
- *PURCHASES_FREQUENCY*: frequenza degli acquisti, punteggio tra 0 e 1 (1 = acquisti frequenti, 0 = acquisti non frequenti).
- *ONEOFFPURCHASESFREQUENCY*: Quanto frequentemente gli acquisti vengono effettuati in un'unica soluzione (1 = acquisti frequenti, 0 = acquisti non frequenti).
- *PURCHASESINSTALLMENTSFREQUENCY*: frequenza con cui vengono effettuati gli acquisti a rate (1 = frequentemente, 0 = non frequentemente).
- *CASHADVANCEFREQUENCY*: frequenza con cui viene pagato l'anticipo in contanti
- *CASHADVANCETRX*: Numero di transazioni effettuate con "contanti in anticipo".
- *PURCHASES_TRX*: Numero di transazioni di acquisto effettuate
- *CREDIT_LIMIT*: Limite della carta di credito dell'utente
- *PAYMENTS*: Importo dei pagamenti effettuati dall'utente
- *MINIMUM_PAYMENTS*: Importo minimo dei pagamenti effettuati dall'utente
- *PRCFULLPAYMENT*: Percentuale del pagamento completo pagato dall'utente
- *TENURE*: Durata del servizio di carta di credito per l'utente

2.**segmentazione_clienti.ipynb**: notebook contenent l'analisi svolta in python

## Dettagli analisi

### Analisi preliminari

1.**Valori mancanti**: controllo se ci sono valori mancanti

  - *crediti_limit* ha un valore mancante, che decido di eliminare
  - *minimum_payments* ne ha diversi, quindi decido imputare ai dati mancanti la media
    
Ora nessuna variabile presenta valori mancanti.

2.Tolgo la variabile *cust_id* che non mi serve per l'analisi

### Cluster

Combinando insieme gruppi di variabili, con k-means e con elbow method vedo se e quanti gruppi sono presenti nel dataset.  

## Prerequisiti e utilizzo 

- Python installato
- librerie da installare tramite pip (pip install nome_libreria):
  - pandas
  - numpy
  - matplotlib.pyplot
  - sklearn
  - seaborn

### Istruzioni

1.**Download repository**: il notebook contiene il codice python, i grafici e i relativi commenti, e il dataset 'credit_card_customers.csv', da scaricare qui:  

https://proai-datasets.s3.eu-west-3.amazonaws.com/credit_card_customers.csv 

2.**Installare le librerie richieste**:
  - assicurarsi di avere Python 3.10 installato
  - installare le librerie necessarie
  - 
3.**Runnare il file Python**: eseguire il file Python usando direttamente un interprete Python come Google Colab.

4. Settare il RANDOM_SEED, io l'ho settato a 2.

## Contatti
Per domande, suggerimenti o feedback, contattatemi pure alla mail alessiaagostini53@gmail.com.
