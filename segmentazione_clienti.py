#!/usr/bin/env python
# coding: utf-8

# ## Segmentazione della clientela di un'azienda di servizi finanziari

# In[119]:


# importo le librerie necessarie all'analisi
import pandas as pd
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# In[2]:


RANDOM_SEED = 2


# In[3]:


df = pd.read_csv("credit_card_customers.csv")
df.head()


# In[40]:


df.info()


# In[4]:


df.shape


# In[5]:


df.count()


# In[6]:


df.isna().sum()


# In[120]:


# elimino il dato mancante
df = df.dropna(subset=['CREDIT_LIMIT'])


# In[121]:


# imputazione dei dati mancanti di MINIMUM_PAYMENTS con la media con pandas
col = "MINIMUM_PAYMENTS"


# In[9]:


replace_with = df[col].mean()
df[col] = df[col].fillna(replace_with)
na_count = df[col].isna().sum() 
print(f"La colonna {col} ha {na_count} valori mancanti")
df.head(10)


# In[10]:


df = df.drop('CUST_ID', axis=1)


# In[122]:


# imposto i paramentri dei grafici
plt.rcParams["figure.figsize"] = (16, 10)
sns.set_theme()


# In[123]:


# funzione del grafico dell'elbow method
def plot_ssd_curve(data):
    ssd = {}
    for k in range(1, 10):
        kmeans = KMeans(init="k-means++", n_clusters=k, random_state=RANDOM_SEED).fit(data)
        ssd[k] = kmeans.inertia_
    plt.figure()
    plt.plot(list(ssd.keys()), list(ssd.values()),marker='o')
    plt.xlabel("Numero di cluster", fontsize=16)
    plt.ylabel("Somma delle distanza al quadrato", fontsize=16)
    plt.show()


# In[124]:


# funzione del grafico visualizzare i cluster

def plot_clusters(model, data, axlabels=None, print_ssd=False):
    y_pred = model.predict(data)
    sns.scatterplot(x=data[:,0], y=data[:,1], hue=y_pred, s=100)
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], c='red', s=200, alpha=0.5)

    if axlabels!=None:
        plt.xlabel(axlabels[0], fontsize=16)
        plt.ylabel(axlabels[1], fontsize=16)

    if print_ssd:
        plt.text(X[:,0].max()-10, 0, f"SSD={model.inertia_:.2f}")

    plt.show()


# RATE 

# In[126]:


data = df[["INSTALLMENTS_PURCHASES", "PURCHASES"]].values


# In[127]:


X = scaler.fit_transform(data)


# In[128]:


plot_ssd_curve(X)


# In[129]:


kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = RANDOM_SEED)
kmeans.fit(X)
plot_clusters(kmeans, X, axlabels=["INSTALLMENTS_PURCHASES", "PURCHASES"], print_ssd=True)


# In[84]:


data = df[["PURCHASES_INSTALLMENTS_FREQUENCY", "PURCHASES_FREQUENCY"]].values


# In[85]:


X = scaler.fit_transform(data)


# In[86]:


plot_ssd_curve(X)


# In[87]:


kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = RANDOM_SEED)
kmeans.fit(X)
plot_clusters(kmeans, X, axlabels=["PURCHASES_INSTALLMENTS_FREQUENTY", "PURCHASES_FREQUENTY"], print_ssd=True)


# UNICA SOLUZIONE

# In[88]:


data = df[["ONEOFF_PURCHASES", "PAYMENTS"]].values


# In[89]:


X = scaler.fit_transform(data)


# In[90]:


plot_ssd_curve(X)


# In[91]:


kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = RANDOM_SEED)
kmeans.fit(X)
plot_clusters(kmeans, X, axlabels=["ONEOFF_PURCHASES", "PAYMENTS"], print_ssd=True)


# In[80]:


data = df[["ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_FREQUENCY"]].values


# In[81]:


X = scaler.fit_transform(data)


# In[82]:


plot_ssd_curve(X)


# In[83]:


kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = RANDOM_SEED)
kmeans.fit(X)
plot_clusters(kmeans, X, axlabels=["ONEOFF_PURCHASES_FREQUENTY", "PURCHASES_FREQUENTY"], print_ssd=True)


# ANTICIPO IN CONTANTI

# In[92]:


data = df[["CASH_ADVANCE", "PAYMENTS"]].values


# In[94]:


X = scaler.fit_transform(data)


# In[95]:


plot_ssd_curve(X)


# In[100]:


kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = RANDOM_SEED)
kmeans.fit(X)
plot_clusters(kmeans, X, axlabels=["CASH_ADVANCE", "PAYMENTS"], print_ssd=True)


# Dall'analisi svolta l'azienda dovrebbe creare diverse campagne di marketing; una parte dei suoi clienti infatti completa gli acquisti in una soluzione, un'altra a rate e un'ultima paga l'anticipo in contanti, e dedicare a ognuno di loro una campagna diversa in base all'utilizzo del conto. Inoltre potrebbe personalizzare la promozione delle carte di credito in base all'importo del saldo nel conto e alla frequenza degli acquisti e all'importo dei pagamenti. 

# In[ ]:




