#!/usr/local/bin/python3.3

### surnom : Fox
### date : 9 Janvier 2016
### programme : reporting_excl.py
### objectif : création des fonctions de stockage des donnees de sites sur excel


def verif_niveau():
  '''Cette fonction a pour but de vérifier quelle ligne est vide '''
  ligne = 0
  for i in range(2,10000):
    liste = []
    for j in range(1,7):
      valeur = classeur.cell(row=i,column=j).value
      if valeur == None:
        continue
      liste.append(valeur)
    if liste == []:
      ligne = i
      break
  return ligne
