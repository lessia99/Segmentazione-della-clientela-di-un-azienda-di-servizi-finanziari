# Segmentazione-della-clientela-di-un-azienda-di-servizi-finanziari

**Descrizione:**
Un'azienda di servizi finanziari sta investendo in una nuova campagna di marketing per per promuovere la propria linea di carte di credito.
Si ha a disposizione un dataset contiene le seguenti informazioni su 9000 possessori di carte di credito dell'azienda:
- CUST_ID : Identificazione del titolare della carta di credito (Categorico)
- BALANCE : importo del saldo rimasto sul conto per effettuare acquisti
- BALANCE_FREQUENCY : frequenza di aggiornamento del saldo, punteggio tra 0 e 1 (1 = aggiornato frequentemente, 0 = non aggiornato frequentemente).
- PURCHASES : Quantità di acquisti effettuati dal conto
- ONEOFF_PURCHASES : Importo massimo di acquisti effettuati in un'unica soluzione
- INSTALLMENTS_PURCHASES : Importo degli acquisti effettuati a rate
- CASH_ADVANCE : Anticipo in contanti dato dall'utente
- PURCHASES_FREQUENCY : frequenza degli acquisti, punteggio tra 0 e 1 (1 = acquisti frequenti, 0 = acquisti non frequenti).
- ONEOFFPURCHASESFREQUENCY : Quanto frequentemente gli acquisti vengono effettuati in un'unica soluzione (1 = acquisti frequenti, 0 = acquisti non frequenti).
- PURCHASESINSTALLMENTSFREQUENCY : frequenza con cui vengono effettuati gli acquisti a rate (1 = frequentemente, 0 = non frequentemente).
- CASHADVANCEFREQUENCY : frequenza con cui viene pagato l'anticipo in contanti
- CASHADVANCETRX : Numero di transazioni effettuate con "contanti in anticipo".
- PURCHASES_TRX : Numero di transazioni di acquisto effettuate
- CREDIT_LIMIT : Limite della carta di credito dell'utente
- PAYMENTS : Importo dei pagamenti effettuati dall'utente
- MINIMUM_PAYMENTS : Importo minimo dei pagamenti effettuati dall'utente
- PRCFULLPAYMENT : Percentuale del pagamento completo pagato dall'utente
- TENURE : Durata del servizio di carta di credito per l'utente

L'obiettivo è quello di segmentare la clientela attuale indentificando dei cluster verso la quale l'azienda dovrà indirizzare apposite campagne di marketing.

**Utilizzo:**
- Installazione di Python;
- software open source;
- librerie da importare e/o installare tramite pip (pip install nome_libreria): pandas, numpy, sklearn, matplotlib.pyplot, seaborn, sklearn.preprocessing;
- dataset da importare: "https://proai-datasets.s3.eu-west-3.amazonaws.com/credit_card_customers.csv"
