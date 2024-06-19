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
            latitud:float = float(linea['WKT'][7:23]) #ESTO NO ES CORRECTO PORQUE NO SON SIEMPRE IGUAL DE LARGOS!
            longitud:float = float(linea['WKT'][25:41])          
            campana:CampanaVerde=CampanaVerde(direccion,barrio,comuna,materiales,latitud,longitud)
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
'''
    def tres_campanas_cercanas(self, lat, lon) -> tuple[CampanaVerde, CampanaVerde, CampanaVerde]:
        
        
        pass

    def exportar_por_materiales(self, archivo_csv, materiales:set[str]) -> ...:
         completar docstring 
        pass
'''

d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')
print(d.cantidad_por_barrio(' Metal ')) #los materiales vienen con el espacio que tienen en el CSV deberia eliminarse o darse por hecho que el usuario lo usara correctamente?