import unittest
from dataset import DataSetCampanasVerdes, leer_archivo_v1 #Importamos para testear.
from campana_verde import CampanaVerde
d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')
dVacio:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-vacio.csv')

####################################################################

class TestDataSetCampanasVerdes(unittest.TestCase):
    def test_csv_vacio(self):
        self.assertEqual(dVacio.tamano(), 0)
        self.assertEqual(dVacio.barrios(), set())
    
    def test_tamano(self):
        self.assertEqual(d.tamano(),6)
        self.assertNotEqual(d.tamano(),-1)
        self.assertNotEqual(d.tamano(),50)

    def test_barrios(self):
        self.assertEqual(d.barrios(),{'VILLA DEVOTO', 'VILLA CRESPO', 'NUEVA POMPEYA', 'MONTE CASTRO', 'CHACARITA'})

    def test_campanas_del_barrio(self):
        #self.assertEqual(d.campanas_del_barrio('VILLA DEVOTO'),[<CERVANTES 3896@Carton/Papel@VILLA DEVOTO>])    
        pass

    def test_cantidad_por_barrio(self):
        self.assertEqual(d.cantidad_por_barrio('Carton'),{'VILLA DEVOTO':1, 'VILLA CRESPO':2, 'NUEVA POMPEYA':1, 'MONTE CASTRO':1, 'CHACARITA':1})   
        self.assertNotEqual(d.cantidad_por_barrio('Carton'),{'VILLA DEVOTO':6, 'VILLA CRESPO':42, 'NUEVA POMPEYA':1, 'MONTE CASTRO':-7, 'CHACARITA':1})


    def test_tres_campanas_cercanas(self):
        pass    

    def test_exportar_por_materiales(self):
        d.exportar_por_materiales({'Papel', 'Carton'})
        resultado:str = leer_archivo_v1('archivo_csv')
        valor = 'DIRECCION,BARRIO\nAGUIRRE 1447,CHACARITA\nBERMUDEZ 1697,MONTE CASTRO\nCERVANTES 3896,VILLA DEVOTO\nCASTILLO 77,VILLA CRESPO\nCASTILLO 77,VILLA CRESPO\n'
        self.assertEqual(resultado, valor)


#d.exportar_por_materiales({'Papel', 'Carton'})
#resultado:str = leer_archivo_v1('archivo_csv')
#valor = 'DIRECCION,BARRIO\nAGUIRRE 1447,CHACARITA\nBERMUDEZ 1697,MONTE CASTRO\nCERVANTES 3896,VILLA DEVOTO\nCASTILLO 77,VILLA CRESPO\nCASTILLO 77,VILLA CRESPO'
#print(resultado)
#print(valor)
#ARREGLAR:
    

#print(dVacio.tamano())
#print(d.barrios())
#print(d.campanas_del_barrio("VILLA DEVOTO"))

#print(d.cantidad_por_barrio("Carton"))     


# self.assertEqual(d.campanas_del_barrio('VILLA DEVOTO'),[<CERVANTES 3896@Carton/Papel@VILLA DEVOTO>])
 #self.assertEqual(d.campanas_del_barrio('VILLA CRESPO'),['<CASTILLO 77@Carton/Papel@VILLA CRESPO>, <CASTILLO 77@Carton/Papel@VILLA CRESPO>'])
 #self.assertEqual(d.campanas_del_barrio('NUEVA POMPEYA'),[])
 #self.assertNotEqual(d.campanas_del_barrio('CHACARITA')["abc"])
   
####################################################################

unittest.main()
