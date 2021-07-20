#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
from pprint import pprint
from pymongo import MongoClient

myclient = pymongo.MongoClient('localhost',27017)

mydb = myclient["Tarea"]
mydb


# In[26]:


#Verifica si la database existe
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "tarea" in dblist:
  print("La database existe.")


# In[27]:


#Crea colección
mycol = mydb["archivos"]
print(mydb.list_collection_names())


# In[28]:


#Verifica si las colecciones existen
collist = mydb.list_collection_names()
if "archivos" in collist:
  print("La colección existe.")


# In[29]:


wav1 = "sonido1.wav"
wav2 = "sonido2.wav"

myquery1 = { "URL": "1" }
newvalues1 = { "$set": { "URL": wav1 } }
mycol.update_one(myquery1, newvalues1)


myquery2 = { "URL": "2" }
newvalues2 = { "$set": { "URL": wav2 } }
mycol.update_one(myquery2, newvalues2)


# In[ ]:




