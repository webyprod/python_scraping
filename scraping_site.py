#!/usr/local/bin/python3.3

### surnom : Fox
### date : 9 Janvier 2016
### programme : scraping_site.py
### objectif : retirer toutes les balises nécessaires pour le référenceur
###            pour identifier un site


from urllib.request import urlopen
from bs4 import BeautifulSoup


class Page:
  def __init__(self,page):
    self.page = page
    self.url = urlopen(self.page)
    self.objet = BeautifulSoup(self.url.read(), 'html5lib')
    self.titre = self.objet.title
    self.description = self.objet.find("meta", {"name":"description"})
    self.mots_cles = self.objet.find("meta", {"name":"keywords"})
    self.h1 = self.objet.h1
    self.h2 = self.objet.findAll("h2")

  def get_title(self):
    return self.titre.get_text()

  def get_meta_desc(self):
    return self.description['content']

  def get_keywords(self):
    return self.mots_cles['content']

  def get_h1(self):
    return self.h1.get_text()

  def get_h2(self):
    h = []
    for h2 in self.h2:
      h.append(h2.get_text())
    return h
