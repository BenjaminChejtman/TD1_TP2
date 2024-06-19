import unittest

# Importamos el codigo a testear.
from campana_verde import CampanaVerde
from haversine import haversine, Unit

####################################################################

class TestCampanaVerde(unittest.TestCase):

    def test_atributos_CampanaVerde(self): 
        #Acá se desea testear que la separación de la lista que debería ingresar y cortar el csv en partes funciona. Utilizé dos ejemplos simples de campanas verdes reales sacadas de Google Maps.  
        
        campana1:CampanaVerde=CampanaVerde("Laprida 1149","Recoleta",2,{"Plástico"},"-34.59560785539046", "-58.40803234691601")
        self.assertEqual(campana1.direccion,"Laprida 1149")
        self.assertEqual(campana1.barrio,"Recoleta")
        self.assertEqual(campana1.comuna,2)
        self.assertEqual(campana1.materiales,{"Plástico"})
        self.assertEqual(campana1.latitud, "-34.59560785539046")
        self.assertAlmostEqual(campana1.longitud, "-58.40803234691601")
        
        campana2:CampanaVerde=CampanaVerde("Ibarrola 7051","Liniers",9,{"Papel","Cartón"},"-34.64016129701416", "-58.525036515246306")
        self.assertEqual(campana2.direccion,"Ibarrola 7051")
        self.assertEqual(campana2.barrio,"Liniers")
        self.assertEqual(campana2.comuna,9)
        self.assertEqual(campana2.materiales,{"Papel","Cartón"})
        self.assertEqual(campana2.latitud, "-34.64016129701416")
        self.assertEqual(campana2.longitud, "-58.525036515246306")
        
    def test_CampanaVerde_distancia(self):
        #En este conjunto de tests vamos a revisar si la función en sí es correcta y hace lo que le pedimos.
        
        
        #Campanas Modelo
        campana1:CampanaVerde=CampanaVerde("Olazabal 4470","Villa Urquiza",12,{"Cartón"},-34.57265575560225, -58.479309232841445)
        campana2:CampanaVerde=CampanaVerde("______","_______",12,{"__"},-34.57265575560225, -58.479309232841445)
        campana3:CampanaVerde=CampanaVerde("______","_______",12,{"__"},-34.57265575560225, -58.479309232841445)
        campana4:CampanaVerde=CampanaVerde("Paseo de las Américas","Palermo",14,{"Basura"},-34.55112612847545, -58.435818911529196)
        campana5:CampanaVerde=CampanaVerde("______","_______",12,{"__"},-95.57265575560225, 190.479309232841445)
        
        #Puntos de prueba
        puntoprueba1:tuple[float, float]={-34.57265575560225, -58.479309232841445}
        puntoprueba2:tuple[float, float]={-34.57265575560225, -58.479309232841445}
        puntoprueba3:tuple[float, float]={-34.57265575560225, -58.479309232841445}
        puntoprueba4:tuple[float, float]={-34.55112612847545, -58.435818911529196}
        puntoprueba5:tuple[float, float]={-34.57265575560225, -58.479309232841445}
        
        
        #No pude hacer los test todavía por razón a llamar la función distancia
        respuesta_esperada_1=0.0
        #respuesta_bot_1=campana1.distancia(puntoprueba1)
        self.assertEqual((campana1,puntoprueba1).distancia,respuesta_esperada_1)
       
        #self.assertEqual(respuesta_esperada_1,respuesta_bot_1)
        
        
        
puntoprueba1:tuple[float, float]={-34.57265575560225, -58.479309232841445}        
print(haversine({-34.57265575560225, -58.479309232841445}, puntoprueba1))
        
## y asi con el resto de los metodos a testear.
        
####################################################################

unittest.main()
