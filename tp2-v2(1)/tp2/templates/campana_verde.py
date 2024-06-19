from haversine import haversine , Unit

class CampanaVerde:
    def __init__(self, d:str, b:str, c:int, m:set[str], lat:float, lon:float):
        ''' completar docstring '''
        self.direccion:str = d
        self.barrio:str = b
        self.comuna:int = c
        self.materiales:set[str] = m
        self.latitud:float = lat
        self.longitud:str = lon

    def distancia(self, ubicacionCampana:tuple[float, float], punto:tuple[float, float]) -> tuple[float, float]:     
        ''' 
        Requiere: una direccion valida con el eje X (o latitud) en el primer float de la tupla y con el eje Y (o longitud) en el segundo float de la tupla
        Devuelve: La distancia entre el punto 1 y el punto 2, osea entre la ubicacion de la Campana Verde y el punto ingresado
        '''
        return haversine(ubicacionCampana, punto, unit=Unit.METERS)

    def __repr__(self) -> str:
        '''
        Requiere: nada
        Devuelve: Un mensaje de tipo STR que contiene la direccion, materiales y barrio de la campana verde C separados por @ y con <> al principio y al final respectivamente. Cabe mencionar que los materiales que se pueden depositar van a estar seprados por /.
        '''
        return ('<' + self.direccion + '@' + str(self.materiales) + '@' + self.barrio + '>') #checkear si esto seria STR o deberiamos hacer STR() a los self.algo

