import unittest

# Importamos el codigo a testear.
from dataset import DataSetCampanasVerdes
from campana_verde import CampanaVerde
d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')

####################################################################

class TestDataSetCampanasVerdes(unittest.TestCase):

    def test_tamano(self):
        self.assertEqual(d.tamano(),6)
        self.assertNotEqual(d.tamano(),-1)
        self.assertNotEqual(d.tamano(),50)

    def test_barrios(self):
        self.assertEqual(d.barrios(),{'VILLA DEVOTO', 'VILLA CRESPO', 'NUEVA POMPEYA', 'MONTE CASTRO', 'CHACARITA'})

    def test_cantidad_por_barrio(self):
        self.assertEqual(d.cantidad_por_barrio('Carton'),{'VILLA DEVOTO':1,
                                                          'VILLA CRESPO':2, 
                                                          'NUEVA POMPEYA':1, 
                                                          'MONTE CASTRO':1, 
                                                          'CHACARITA':1})
        
        self.assertNotEqual(d.cantidad_por_barrio('Carton'),{'VILLA DEVOTO':6,
                                                         'VILLA CRESPO':42, 
                                                         'NUEVA POMPEYA':1, 
                                                         'MONTE CASTRO':-7, 
                                                         'CHACARITA':1})

        
    #def test_tres_campanas_cercanas(self):
        


    def test_exportar_por_materiales(self):
        

        

"""
## y así con el resto de los métodos a testear.
    
print(d.barrios())
print(d.campanas_del_barrio("VILLA DEVOTO"))

#ARREGLAR:
    def test_campanas_del_barrio(self):
        respuesta_bot:CampanaVerde=[<CERVANTES 3896@Carton/Papel@VILLA DEVOTO>]
        self.assertEqual(d.campanas_del_barrio('VILLA DEVOTO'),respuesta_bot)
        self.assertEqual(d.campanas_del_barrio('VILLA CRESPO'),['<CASTILLO 77@Carton/Papel@VILLA CRESPO>, <CASTILLO 77@Carton/Papel@VILLA CRESPO>'])
        self.assertEqual(d.campanas_del_barrio('NUEVA POMPEYA'),[])
        self.assertNotEqual(d.campanas_del_barrio('CHACARITA')["abc"])
    
"""

print(d.tamano())
print(d.barrios())
print(d.campanas_del_barrio("VILLA DEVOTO"))
print(d.cantidad_por_barrio("Carton"))     
   
####################################################################

unittest.main()
