from haversine import haversine , Unit

class CampanaVerde:
    def __init__(self, d:str, b:str, c:int, m:set[str], latylon:tuple[float, float]): #creamos los atributos de nuestra Campana Verde
        '''
        Inicializa: una campana verde con dirección d, barrio b, comuna c, materiales m, latitud y longitud "latylon"
        
        '''
        self.direccion:str = d
        self.barrio:str = b
        self.comuna:int = c
        self.materiales:set[str] = m
        self.latitudylongitud:tuple[float, float] = latylon

    def distancia(self, punto:tuple[float, float]) -> float:       
        ''' 
        Requiere: una direccion valida con el eje X (o latitud) en el primer float de la tupla y con el eje Y (o longitud) en el segundo float de la tupla
        Devuelve: La distancia entre el punto 1, siendo la campana verde, y el punto 2, el punto ingresado
        '''
        return haversine(self.latitudylongitud, punto, unit=Unit.METERS) # devolvemos la distancia entre la ubicación de la campana verde y un punto, el cual es una tupla del tipo (latitud, longitud), utilizando la función haversine

    def __repr__(self) -> str:
        '''
        Requiere: nada
        Devuelve: Un mensaje de tipo STR que contiene la dirección, materiales y barrio de la campana verde C separados por @, con < y > al principio y al final respectivamente. Cabe mencionar que los materiales que se pueden depositar van a estar seprados por /.
        '''
        return ('<' + self.direccion + '@' + str('/'.join(self.materiales)) + '@' + self.barrio + '>')



    
        
