from unittest import TestCase
from com.rafaregisp.operacoes Import Opercoes

class testOperacoes (TestCase):

   def setup(self):
       self.operacoes = operacoes()
       
       def test_soma(self):
           self.assertEqual(self.operacoes.soma([7, 2]), 9,"deveria ser 9")
