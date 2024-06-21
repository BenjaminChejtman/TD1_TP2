mport unittest

# Importamos el codigo a testear.
from dataset import DataSetCampanasVerdes
d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')

####################################################################

class TestDataSetCampanasVerdes(unittest.TestCase):

    def test_tamano(self):
        self.assertEqual(d.tamano,6)
        self.assertNotEqual(d.tamano,-1)
        self.assertNotEqual(d.tamano,50)
    
    def test_barrios(self):
        self.assertEqual(d.barrios,{"CHACARITA","MONTE CASTRO","NUEVA POMPEYA","VILLA DEVOTO","VILLA CRESPO"})

## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
