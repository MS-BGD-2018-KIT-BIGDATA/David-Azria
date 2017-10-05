#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:24:42 2017

@author: david
"""

import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas


url=urllib.request.urlopen("https://www.cdiscount.com/search/10/acer.html#_his_")
soup = url.read()
soup = BeautifulSoup(soup,"lxml")

acer_produit=soup.find_all('div',"prdtBTit")
acer_result=soup.find_all('div',"prdtPInfoTC")
acer_prixinit=soup.find_all('span',"price")
a=len(acer_result)
u=soup.find_all('div',"prdtPrSt")
e=len(u)
d = 0
for i in range(a):
    lon=len(acer_result[i])
    if( lon > 0 ):
        print(acer_produit[i].text,"au prix de ", acer_result[i].text,"au lieu de ",acer_prixinit[i].text)


  
    

url=urllib.request.urlopen("https://www.cdiscount.com/search/10/dell.html#_his_")
soup = url.read()
soup = BeautifulSoup(soup,"lxml")



dell_produit=[]
dell_result=[]
dell_prixinit=[]

dell_produit=soup.find_all('div',"prdtBTit")
dell_result=soup.find_all('div',"prdtPInfoTC")
dell_prixinit=soup.find_all('span',"price")
print(len(dell_produit),len(dell_result),len(dell_prixinit))


u=soup.find_all('div',"prdtPrSt")
c=len(u)
b=len(dell_result)
j=0
i=0

import numpy as np
import pandas as pd

#h = pd.DataFrame({'col': dell_produit[i].text})


prixinit=[]
pridiscount=[]
nomproduit=[]
eco=[]
sumd=0
suminit=0
delleco=0

for i in range(b):
    lon=len(dell_result[i])
    if( lon > 0 ):
        
        tempinit=(float(dell_prixinit[i].text.replace('€',".")))
        prixinit.append(tempinit)
        suminit=tempinit+suminit
        
        tempdiscount=float(dell_result[i].text.replace('€',".").replace(',','.'))
        pridiscount.append(tempdiscount)
        sumd=tempdiscount+sumd
        
        nomproduit.append(dell_produit[i])
        eco.append((tempdiscount-tempinit)*100/(tempdiscount))
        
        print(dell_produit[i].text,"au prix de ", tempinit,"au lieu de ",tempdiscount)

#J'ai inversé le init et discount..
delleco=((sumd-suminit)*100/sumd)
print ("le nombre de promos sur les produits Acer est de", e,"le nombre de promos sur les produits Dell est de", c )
print("Les produits remisés Dell le sont, en moyenne, de", delleco, "%")
#eco[i]=int(float(prixinit)-float(pridiscount))


#dell1=np.array(([dell_prixinit]), dtype=float)
#dell2=np.array(([dell_produit]), dtype=float)
#dell=dell1-dell2


#print ("le nombre de promos sur les produits Dell ", b)
#print (soup_result)   