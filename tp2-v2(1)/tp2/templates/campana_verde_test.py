import unittest
from campana_verde import CampanaVerde
#from haversine import haversine, Unit

####################################################################

class TestCampanaVerde(unittest.TestCase):

    def test_atributos_CampanaVerde(self): #Acá se desea testear que la separación de la lista ingresada y la división del csv en partes funcione.         
        campana1:CampanaVerde=CampanaVerde("Laprida 1149","Recoleta",2,{"Plástico"},(-58.40803234691601, -34.59560785539046))
        self.assertEqual(campana1.direccion,"Laprida 1149")
        self.assertEqual(campana1.barrio,"Recoleta")
        self.assertEqual(campana1.comuna,2)
        self.assertEqual(campana1.materiales,{"Plástico"})
        self.assertAlmostEqual(campana1.latitudylongitud, (-58.40803234691601, -34.59560785539046))
        
        campana2:CampanaVerde=CampanaVerde("Ibarrola 7051","Liniers",9,{"Papel","Cartón"},(-58.525036515246306, -34.64016129701416))
        self.assertEqual(campana2.direccion,"Ibarrola 7051")
        self.assertEqual(campana2.barrio,"Liniers")
        self.assertEqual(campana2.comuna,9)
        self.assertEqual(campana2.materiales,{"Papel","Cartón"})
        self.assertAlmostEqual(campana2.latitudylongitud, (-58.525036515246306, -34.64016129701416))
     
        
    def test_CampanaVerde_distancia(self): #En estos casos de tests vamos a evaluar si el cálculo de distancias entre 2 puntos es correcto.

        campana1:CampanaVerde=CampanaVerde("Olazabal 4470","Villa Urquiza",12,{"Cartón"},(-58.479309232841445,-34.57265575560225))
        campana2:CampanaVerde=CampanaVerde("Alcorta 2874","Palermo",14,{"Vidrio"},(-58.435818911529196,-34.55112612847545))
        campana3:CampanaVerde=CampanaVerde("Libertador 6796","Nuñez",12,{"Papel"}, (-95.57265575560225, -90.479309232841445))

        puntoprueba1:tuple[float, float]=(-58.479309232841445,-34.57265575560225)
        puntoprueba2:tuple[float, float]=(-59.433578911529196,-32.55112612347545)
        puntoprueba3:tuple[float, float]=(-18.472841445,-20.57265573450225)
        
        self.assertAlmostEqual(campana1.distancia(puntoprueba1), 0.0) #Caso en el que son el mismo punto, por lo que su distancia corresponde que sea 0.0
        self.assertAlmostEqual(campana2.distancia(puntoprueba2), 159605.84130455766) #Caso con un resultado menor
        self.assertAlmostEqual(campana3.distancia(puntoprueba3), 8174833.288515655) #Caso con un resultado mayor

    
    def test_repr(self): #Aquí verificamos que la forma en que se represente la campana verde sea correcto.
        campana1:CampanaVerde=CampanaVerde("Laprida 1149","Recoleta",2,{"Plástico"},(-58.40803234691601,-34.59560785539046))
        campana2:CampanaVerde=CampanaVerde("Ibarrola 7051","Liniers",9,{"Papel","Cartón"},(-58.525036515246306,-34.64016129701416))
        self.assertEqual(str(campana1), '<Laprida 1149@Plástico@Recoleta>')
        self.assertEqual(str(campana2), '<Ibarrola 7051@Papel/Cartón@Liniers>')
        
####################################################################

unittest.main()
