#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pymongo
from pprint import pprint
from pymongo import MongoClient

myclient = pymongo.MongoClient('localhost',27017)

mydb = myclient["Tarea"]
mydb


# In[35]:


#Verifica si la database existe
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "tarea" in dblist:
  print("La database existe.")


# In[36]:


#Crea colección
mycol = mydb["archivos"]
print(mydb.list_collection_names())


# In[37]:


#Verifica si las colecciones existen
collist = mydb.list_collection_names()
if "archivos" in collist:
  print("La colección existe.")


# In[57]:


#########
archivos1 = {
    "_id":1,
    "fecha":"20/07/2021",
    "ciudad":"Valdivia",
    "URL":"1",
    "latitud":-39.82435,
    "longitud":-73.24589,
    "duracion":"20 segundos",
    "formato":".wav",
    "exterior":"Si",
    "tipo_fuente":"animales",
    "usuario":
    {
        "RUT":"16.795.344-1",
        "nombre":"Gary",
        "apellido":"Medel",
    },
    "segmentos": [
        {
            "ID":11,
            "formato":".wav",
            "duracion":"10 segundos",
            "inicio":"0 segundos",
            "fin":"10 segundos",
            "etiquetas": [ 
                {
                    "descripcion":"descripcion de prueba numero 1",
                    "ID_analizador":1
                },
                {
                    "descripcion":"descripcion de prueba numero 2",
                    "ID_analizador":2
                }
            ]
        },
        {
            "ID": 12,
            "formato":".wav",
            "duración":"10 segundos",
            "inicio":"10 segundos",
            "fin":"20 segundos",
            "etiquetas": [ 
                {
                    "descripcion":"descripcion de prueba numero 3",
                    "ID_analizador":1
                },
                {
                    "descripcion":"descripcion de prueba numero 4",
                    "ID_analizador":2
                }
            ]
        }
    ]
}

#########
archivos2 = {
    "_id":2,
    "fecha":"25/06/2021",
    "ciudad":"Valdivia",
    "URL":"2",
    "latitud":-39.83168638,
    "longitud":-73.2370306,
    "duracion":"14 segundos",
    "formato": ".wav",
    "exterior": "Sí",
    "tipo_fuente":"mecanico",
    "usuario":
    {
        "RUT":"16.927.586-6",
        "nombre":"Alexis",
        "apellido":"Sanchez",
    },
    "segmentos":[
        {
            "ID":21,
            "formato":".wav",
            "duracion":"7 segundos",
            "inicio":"0 segundos",
            "fin":"7 segundos",
            "etiquetas": [ 
                {
                    "descripcion":"descripcion de prueba numero 5",
                    "ID_analizador":1
                },
                {
                    "descripcion":"descripcion de prueba numero 6",
                    "ID_analizador":2
                }
            ]
        },
        {
            "ID": 22,
            "formato":".wav",
            "duracion":"7 segundos",
            "inicio":"7 segundos",
            "fin":"14 segundos",
            "etiquetas": [ 
                {
                    "descripcion":"descripcion de prueba numero 7",
                    "ID_analizador":1
                },
                {
                    "descripcion":"descripcion de prueba numero 8",
                    "ID_analizador":2
                }
            ]
        }
    ]
}


# In[58]:


mycol.drop()


# In[59]:


x = mycol.insert_one(archivos1)
y = mycol.insert_one(archivos2)


# In[62]:


from pprint import pprint

for x in mycol.find():
  pprint(x)


# In[ ]:




