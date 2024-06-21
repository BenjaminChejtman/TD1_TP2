import unittest
from campana_verde import CampanaVerde
#from haversine import haversine, Unit

####################################################################

class TestCampanaVerde(unittest.TestCase):

    def test_atributos_CampanaVerde(self): #Acá se desea testear que la separación de la lista que debería ingresar y cortar el csv en partes funciona. Utilizé dos ejemplos simples de campanas verdes reales sacadas de Google Maps.         
        campana1:CampanaVerde=CampanaVerde("Laprida 1149","Recoleta",2,{"Plástico"},(-34.59560785539046, -58.40803234691601))
        self.assertEqual(campana1.direccion,"Laprida 1149")
        self.assertEqual(campana1.barrio,"Recoleta")
        self.assertEqual(campana1.comuna,2)
        self.assertEqual(campana1.materiales,{"Plástico"})
        self.assertAlmostEqual(campana1.latitudylongitud, (-34.59560785539046, -58.40803234691601))
        #self.assertAlmostEqual(campana1.longitud, "-58.40803234691601")
        
        campana2:CampanaVerde=CampanaVerde("Ibarrola 7051","Liniers",9,{"Papel","Cartón"},(-34.64016129701416, -58.525036515246306))
        self.assertEqual(campana2.direccion,"Ibarrola 7051")
        self.assertEqual(campana2.barrio,"Liniers")
        self.assertEqual(campana2.comuna,9)
        self.assertEqual(campana2.materiales,{"Papel","Cartón"})
        self.assertAlmostEqual(campana2.latitudylongitud, (-34.64016129701416, -58.525036515246306))
        #self.assertEqual(campana2.longitud, "-58.525036515246306")
        
    def test_CampanaVerde_distancia(self): #En este conjunto de tests vamos a revisar si la función en sí es correcta y hace lo que le pedimos.
        #Campanas Modelo
        campana1:CampanaVerde=CampanaVerde("Olazabal 4470","Villa Urquiza",12,{"Cartón"},(-34.57265575560225, -58.479309232841445))
        campana2:CampanaVerde=CampanaVerde("Paseo de las Américas","Palermo",14,{"Basura"},(-34.55112612847545, -58.435818911529196))
        campana3:CampanaVerde=CampanaVerde("______","_______",12,{"__"}, (-95.57265575560225, -90.479309232841445))

        puntoprueba1:tuple[float, float]=(-34.57265575560225, -58.479309232841445)
        puntoprueba2:tuple[float, float]=(-32.55112612347545, -59.433578911529196)
        puntoprueba3:tuple[float, float]=(-20.57265573450225, -18.472841445)
        
        self.assertEqual(campana1.distancia(puntoprueba1), 0.0) #Caso en el que son el mismo punto, por lo que su distancia corresponde que sea 0.0
        self.assertEqual(campana2.distancia(puntoprueba2), 240841.14170973774) #Caso con un resultado menor
        self.assertEqual(campana3.distancia(puntoprueba3), 7921235.699038102) #Caso co un resultado mayor

    
    def test_repr(self):
        campana1:CampanaVerde=CampanaVerde("Laprida 1149","Recoleta",2,{"Plástico"},(-34.59560785539046, -58.40803234691601))
        campana2:CampanaVerde=CampanaVerde("Ibarrola 7051","Liniers",9,{"Papel","Cartón"},(-34.64016129701416, -58.525036515246306))
        self.assertEqual(str(campana1), '<Laprida 1149@Plástico@Recoleta>')
        self.assertEqual(str(campana2), '<Ibarrola 7051@Papel/Cartón@Liniers>')
        
####################################################################

unittest.main()
