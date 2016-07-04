#!/usr/local/bin/python3.3

### surnom : Fox
### date : 9 Janvier 2016
### programme : scraping_testunit.py
### objectif : Tester la classe Page et vérifier qu'elle fonctionne bien


import unittest
from scraping_site import Page

class TestScrapingPage(unittest.TestCase):
  """ Classe de Test verification fonctionnalite classe Page """

  def setUp(self):
    """ testons sur la page https://www.leboncoin.fr """
    self.excel = Page("https://www.leboncoin.fr")

  def test_reception_titre(self):
    """ verifions que le titre de la page est bien Excel-Pratique.com"""
    self.assertIn("Site de petites annonces gratuites d'occasion - leboncoin.fr", self.excel.get_title())

  def test_reception_h1(self):
    """ verifions que le h1 est Trouvez la bonne affaire parmi 26 020 265 petites annonces sur leboncoin.  """
    self.assertIn("Trouvez la bonne affaire parmi 26 015 940 petites annonces sur leboncoin.", self.excel.get_h1())

  def test_reception_meta_desc(self):
    """ verifions que la meta description est bien 'Site de petites annonces gratuites d'occasion - leboncoin.fr' """
    self.assertIn("Site de petites annonces gratuites d'occasion - leboncoin.fr", self.excel.get_meta_desc())

  def test_reception_h2(self):
    """ verifions que le premier des h2 est bien 'L'actualité leboncoin' """
    self.assertIn("L'actualité leboncoin", self.excel.get_h2()[0])
    
    
unittest.main()
