from haversine import haversine , Unit
from campana_verde import CampanaVerde
import csv

class DataSetCampanasVerdes:
    def __init__(self, archivo_csv:str):
        ''' 
        Requiere: archivos_csv es el nombre del archivo con formato CSV que contiene toda la informacion de Campanas Verdes de la Ciudad de Buenos Aires incluyendo la direccion, barrio, tipo de basura que se puede tirar entre otras cosas
        '''
        self.campanas:list[CampanaVerde] = []
        f = open(archivo_csv, encoding='utf-8')
        for linea in csv.DictReader(f): #linea es dict[str,str]
            direccion:str=linea['direccion']
            barrio:str=linea['barrio']
            comuna:int=linea['comuna']
            materiales:set[str]=set(linea['materiales'].split('/'))
            latitudylongitud:tuple[float, float] = (0.0, 0.0) #ESTO NO ES CORRECTO PORQUE NO SON SIEMPRE IGUAL DE LARGOS!
            #longitud:float = float(linea['WKT'][25:41])          
            campana:CampanaVerde=CampanaVerde(direccion,barrio,comuna,materiales,latitudylongitud)
            self.campanas.append(campana)
        f.close()    


    def tamano(self) -> int:
        '''
        Requiere: un DataSet D de Campanas Verdes #deberiamos poner nada?
        Devuelve: la cantidad de Campanas Verdes en el DataSet D
        '''
        return len(self.campanas)

    def barrios(self) -> set[str]: 
        '''
        Requiere: un DataSet D de Campanas Verdes #deberiamos poner nada?
        Devuelve: un Set que contiene todos los barrios existentes en el DataSet D
            
        '''
        vrBarrios:set[str] = set()
        for campana in self.campanas:   #campana es cada campana verde en el CSV representada por lo que devuelve su REPR
            vrBarrios.add(campana.barrio)   
        return vrBarrios
    
    def campanas_del_barrio(self, barrio:str) -> list[CampanaVerde]:
        '''
        Requiere: un DataSet D de Campanas Verdes y un barrio en especifico
        Devuelve: una List de CampanaVerde que contiene las campanas verdes del DataSet D que estan en el barrio seleccionado
        '''
        campanasEnBarrio:list[CampanaVerde] = []
        for campana in self.campanas:
            if campana.barrio == barrio:
                campanasEnBarrio.append(campana)
        return campanasEnBarrio
        
    def cantidad_por_barrio(self, material:str) -> dict[str, int]:
        '''
        Requiere: un DataSet D de Campanas Verdes y un material en especifico
        Devuelve: un Dict que indica la cantidad de campanas verdes que hay en cada barrio en el que se puede depositar el material indicado
        '''
        campanasPorBarrio:dict[str, int] = dict()
        for campana in self.campanas:
            if material in campana.materiales:
                if campana.barrio in campanasPorBarrio: #checkeamos si el barrio ya fue creado en el Dict
                    campanasPorBarrio[campana.barrio] = campanasPorBarrio[campana.barrio] + 1
                else:
                    campanasPorBarrio[campana.barrio] = 1              
        return campanasPorBarrio

    def tres_campanas_cercanas(self, punto:tuple[float, float]) -> tuple[CampanaVerde, CampanaVerde, CampanaVerde]: #la consigna pide lat y lng como parametros por separado, preguntar si ak hacerlo como una tupla como nosotros lo hicimos esteria bien o mal
        '''
        Requiere: Un punto del tipo Tuple que contenga su Latitud y su Longitud, ambas de tipo Float
        Devuelve: una tupla con sus tres objetos del tipo CampanaVerde, que serian las traes Campanas Verdes mas cercanas al punto ingresado
        '''
        distancias:dict[CampanaVerde, float] = list()
        distanciasList:list[float] =[] 
        for campana in self.campana:
            dist = haversine(campana.latylon, punto, unit=Unit.METERS)
            distancias[campana] = dist
            distanciasList.append(dist)
        distanciasList.sort()
        #distancias[0] =  
        #cerca1 = 
        #res:tuple[CampanaVerde, CampanaVerde, CampanaVerde] = {, }
        #return res
            

    def exportar_por_materiales(self, materiales:set[str]):
        f2 = open('archivo_csv', 'w')
        f2.write('DIRECCION y BARRIO')
        for campana in self.campanas:
            if materiales in campana.materiales:
                f2.write(campana.direccion + campana.barrio + '\n')
        f2.close()
        


d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')
#print(d.barrios())
print(d.cantidad_por_barrio('Papel '))
#print(d.exportar_por_materiales({' Vidrio'})) #los materiales vienen con el espacio que tienen en el CSV deberia eliminarse o darse por hecho que el usuario lo usara correctamente?
