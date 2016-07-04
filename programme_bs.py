#!/usr/local/bin/python3.3

### surnom : Fox
### date : 12 Janvier 2016
### programme : programme_bs.py
### Objectif : Programme principal
###


from fonction_bs import Page
from report_excl import remplissage_cellules
###########################################
###########################################


def main():

  # Entree du site par l'utilisateur
  site = input("Bonjour, quel site souhaitez-vous étudier aujourd'hui ? ")
  
  url = Page(site)  # site analyse par la classe
  
  if url.get_title():
    # Analyse de la balise title
    titre_excel = url.get_title()
  else:
    titre_excel = "Pas d'information sur le titre "

  if url.get_meta_desc():
    # Analyse de la meta description
    meta_desc_excel = url.get_meta_desc()
  else:
    meta_desc_excel = "Pas d'information sur la meta description"

  if url.get_keywords():
    # Analyse des meta keywords
    keywords_excel = url.get_keywords()
  else:
    keywords_excel = "Pas de mots-cles"

  if url.get_h1():
    # Analyse du titre h1
    h1_excel = url.get_h1()
  else:
    h1_excel = "Pas d'information sur le h1"

  if url.get_h2:
    # Analyse du (ou des) titre(s) h2
    if len(url.get_h2()) > 1:
      h2_excel = " ".join(url.get_h2())
    else:
      h2_excel = url.get_h2()
  else:
    print('Pas d\'informations sur le h2')


  #### Remplissage du fichier xlsx 'site.xlsx'
  remplissage_cellules(site, titre_excel, meta_desc_excel, keywords_excel, h1_excel, h2_excel)




if __name__ == "__main__":
  main()
  ### demarrage du programme
