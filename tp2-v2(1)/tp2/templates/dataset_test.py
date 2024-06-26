import unittest
from dataset import DataSetCampanasVerdes, leer_archivo_v1 #Importamos para testear.
from campana_verde import CampanaVerde

########################## CREAMOS NUESTROS DATASETS PARA TESTEAR ################

d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')
d2:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado2.csv')
dVacio:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-vacio.csv')

##################################################################################

class TestDataSetCampanasVerdes(unittest.TestCase):
    
    def test_csv_vacio(self): #Revisamos que el archivo ingresado no esté vacío.
        self.assertEqual(dVacio.tamano(), 0)
        self.assertEqual(dVacio.barrios(), set())
    
    
    def test_tamano(self): #Testeamos el método tamaño
        self.assertEqual(d.tamano(),6)
        self.assertNotEqual(d.tamano(),-1)
        self.assertNotEqual(d.tamano(),50)
        self.assertEqual(d2.tamano(), 81)
        self.assertNotEqual(d2.tamano(), 6)


    def test_barrios(self): #Tests para revisar si funciona el método barrios.
        self.assertEqual(d.barrios(),{'VILLA DEVOTO', 'VILLA CRESPO', 'NUEVA POMPEYA', 'MONTE CASTRO', 'CHACARITA'})    
        self.assertEqual(d2.barrios(), {'COGHLAN', 'VILLA URQUIZA', 'BELGRANO', 'CABALLITO', 'SAAVEDRA'})
    
    
    def test_campanas_del_barrio(self): #Testeamos el método campanas_del_barrio
        esperado:CampanaVerde = CampanaVerde("CERVANTES 3896","VILLA DEVOTO",11,{"Papel", "Carton"},(-58.5267564075838, -34.6083119977315))
        listEsperado = [esperado]
        self.assertEqual(str(d.campanas_del_barrio('VILLA DEVOTO')), str(listEsperado))                    
        self.assertEqual(str(d.campanas_del_barrio('VILLA CRESPO')), '[<CASTILLO 77@Papel/Carton@VILLA CRESPO>, <CASTILLO 77@Papel/Carton@VILLA CRESPO>]')  


    def test_cantidad_por_barrio(self): #Testeamos el método cantidad_por_barrio
        self.assertEqual(d.cantidad_por_barrio('Carton'),{'VILLA DEVOTO':1, 'VILLA CRESPO':2, 'NUEVA POMPEYA':1, 'MONTE CASTRO':1, 'CHACARITA':1})   
        self.assertNotEqual(d.cantidad_por_barrio('Carton'),{'VILLA DEVOTO':6, 'VILLA CRESPO':42, 'NUEVA POMPEYA':1, 'MONTE CASTRO':-7, 'CHACARITA':1})
        self.assertEqual(d2.cantidad_por_barrio('Vidrio'), {'BELGRANO': 1, 'CABALLITO': 15, 'COGHLAN': 7, 'SAAVEDRA': 26, 'VILLA URQUIZA': 30})


    def test_tres_campanas_cercanas(self): #Testeamos el método tres_campanas_cercanas.
        self.assertEqual(str(d.tres_campanas_cercanas((-58.5048544020916, -34.5746919192015))), '(<BERMUDEZ 1697@Papel/Carton@MONTE CASTRO>, <CERVANTES 3896@Papel/Carton@VILLA DEVOTO>, <AGUIRRE 1447@Papel/Carton@CHACARITA>)')    
        self.assertEqual(str(d.tres_campanas_cercanas((-20.5048544020916, -34.5746919192015))), '(<CACHI 163@Metal/Carton/Papel/Plastico/Vidrio@NUEVA POMPEYA>, <CASTILLO 77@Papel/Carton@VILLA CRESPO>, <AGUIRRE 1447@Papel/Carton@CHACARITA>)')    
        
        
    def test_exportar_por_materiales(self): #Testeamos el método exportar_por_materiales.
        d.exportar_por_materiales({'Papel', 'Carton'})
        resultado:str = leer_archivo_v1('archivo_csv')
        valor = 'DIRECCION,BARRIO\nAGUIRRE 1447,CHACARITA\nBERMUDEZ 1697,MONTE CASTRO\nCERVANTES 3896,VILLA DEVOTO\nCASTILLO 77,VILLA CRESPO\nCASTILLO 77,VILLA CRESPO\n'
        self.assertEqual(resultado, valor)
   
####################################################################

unittest.main()
