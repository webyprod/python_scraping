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


def remplissage_cellules(url="", titre="", description="", keywords="", h1="", h2=""):
  informations_du_site = {
    'url':url,
    'titre':titre,
    'meta description':description,
    'meta keywords': keywords,
    'h1':h1,
    'h2':h2
    }
  ligne = verif_niveau()
  colonne = 1
  for valeur in informations_du_site.values():
    classeur.cell(row=ligne,column=colonne).value = valeur
    colonne += 1
    fichier.save('site.xlsx')
