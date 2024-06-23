#from haversine import haversine , Unit
from campana_verde import CampanaVerde
import csv

class DataSetCampanasVerdes:
    def __init__(self, archivo_csv:str):
        ''' 
        Requiere: archivos_csv es el nombre del archivo con formato CSV que contiene toda la informacion de Campanas Verdes de la Ciudad de Buenos Aires incluyendo la direccion, barrio, tipo de basura que se puede tirar entre otras cosas
        Iniciaiza: el DataSetCampanasVerdes cargando las campanas verdes contenidas en el archivo "archivo_csv"
        '''
        self.campanas:list[CampanaVerde] = []
        f = open(archivo_csv, encoding='utf-8')
        for linea in csv.DictReader(f):
            direccion:str=linea['direccion']
            barrio:str=linea['barrio']
            comuna:int=linea['comuna']
            materiales:set[str]=set(linea['materiales'].split(' / '))
            latylng:tuple[str, str] = tuple(linea['WKT'][7:-1].split(' '))
            latitudylongitud:tuple[float, float] = (float(latylng[0]), float(latylng[1])) #ESTO NO ES CORRECTO PORQUE NO SON SIEMPRE IGUAL DE LARGOS!         
            campana:CampanaVerde=CampanaVerde(direccion,barrio,comuna,materiales,latitudylongitud)
            self.campanas.append(campana)
        f.close()    


    def tamano(self) -> int:
        '''
        Requiere: nada
        Devuelve: la cantidad de Campanas Verdes en el DataSet D
        '''
        return len(self.campanas)
    
    def barrios(self) -> set[str]:
        '''
        Requiere: nada
        Devuelve: un Set que contiene los barrios existentes en el DataSet D
            
        '''
        vrBarrios:set[str] = set()
        for campana in self.campanas:
            for barrio in campana.barrio:
                vrBarrios.add(campana.barrio) #agregamos a vrBarrios el barrio correspondiente a cada campana, y como en un set no se repite no es necesario checkear si ya estaba o no dicho barrio
        return vrBarrios
    
    def campanas_del_barrio(self, barrio:str) -> list[CampanaVerde]:
        '''
        Requiere: un barrio en especifico
        Devuelve: una List de tipo CampanaVerde que contiene las campanas verdes del DataSet D que estan en el barrio seleccionado
        '''
        campanasEnBarrio:list[CampanaVerde] = [] #creamos nuestra lista donde guardaremos las campanas verdes del barrio
        for campana in self.campanas:  #Recorremos las campanas verdes
            if campana.barrio == barrio: #Si el barrio de la campana coincide con el barrio seleccionado por parametro...
                campanasEnBarrio.append(campana) #... agregamos esa campana a nuestra lista
        return campanasEnBarrio 
        
    def cantidad_por_barrio(self, material:str) -> dict[str, int]:
        '''
        Requiere: un material en especifico
        Devuelve: un Dict que indica la cantidad de campanas verdes que hay en cada barrio en el que se puede depositar el material indicado
        '''
        campanasPorBarrio:dict[str, int] = dict()
        for campana in self.campanas: # Recorremos las campanas verdes
            if material in campana.materiales:
                if campana.barrio in campanasPorBarrio: #checkeamos si el barrio ya fue creado en el Dict
                    campanasPorBarrio[campana.barrio] = campanasPorBarrio[campana.barrio] + 1
                else:
                    campanasPorBarrio[campana.barrio] = 1              
        return campanasPorBarrio
    
    def cantidad_por_barrio2(self, material:str) -> dict[str, int]:
        '''
        Requiere: un material en especifico
        Devuelve: un Dict que indica la cantidad de campanas verdes que hay en cada barrio en el que se puede depositar el material indicado
        '''
        campanasPorBarrio:dict[str, int] = dict()
        for campana in self.campanas:   # Recorremos las campanas verdes
            if material in campana.materiales and campana.barrio in campanasPorBarrio: # Nos fijamos si la campana verde permite el material indicado y si el barrio donde esta ya se encuentra en el Dict camapanasPorBarrio
                campanasPorBarrio[campana.barrio] = campanasPorBarrio[campana.barrio] + 1 # En caso de ser asi le agregamos uno al numero que ya habia
            elif material in campana.materiales and campana.barrio not in campanasPorBarrio: # En caso de que el material este permitido en esa campana verde pero aun no se encuentre en el Dict...
                campanasPorBarrio[campana.barrio] = 1  # ... Agregamos el barrio al Dict con un valor inicial de 1
        return campanasPorBarrio

    def tres_campanas_cercanas(self, punto:tuple[float, float]) -> tuple[CampanaVerde, CampanaVerde, CampanaVerde]: 
        '''
        Requiere: Un punto del tipo Tuple que contenga su Latitud y su Longitud, ambas de tipo Float
        Devuelve: una tupla con sus tres objetos del tipo CampanaVerde, que serian las traes Campanas Verdes mas cercanas al punto ingresado
        '''
        tresMasCercanas:tuple[CampanaVerde, CampanaVerde, CampanaVerde] = (self.campanas[0], self.campanas[1], self.campanas[2]) #empezamos poniendo las tres primeras posiciones de campanas que tenemos en el CSV
        for campana in self.campanas:               #Recorremos las campanas verdes.
            dist = campana.distancia(punto)              #Calculamos la distancia entre la campana y el punto ingresado.
            primero = tresMasCercanas[0].distancia(punto)
            segundo = tresMasCercanas[1].distancia(punto)                #Asignamos un valor a las primeras 3 posiciones.
            tercero = tresMasCercanas[2].distancia(punto)            
            if dist < primero:                                           #Nos fijamos si la campana que estamos evaluando está mas cerca que la que se encuentra en primera posición.
                tresMasCercanas = (campana, tresMasCercanas[0], tresMasCercanas[1])
            elif dist < segundo and dist > primero:                      #Nos fijamos si la campana que estamos evaluando está mas lejos que la que se encuentra en primera posición y mas cerca que la que se encuentra en segunda posición.
                tresMasCercanas = tresMasCercanas[0], campana, tresMasCercanas[1]        #La insertamos entre las dos posiciones anteriormente mencionadas.
            elif dist < tercero and dist > segundo:                      #Nos fijamos si la campana que estamos evaluando está mas lejos que la que se encuentra en segunda posición y mas cerca que la que se encuentra en tercera posición.
                tresMasCercanas = tresMasCercanas[0], tresMasCercanas[1], campana        #La insertamos entre las dos posiciones anteriormente mencionadas.
        return tresMasCercanas
 
    def exportar_por_materiales(self, materiales:set[str]):
        '''
        Requiere: un conjunto de materiales tipo str
        Devuelve: Nada
        Modifica: EScribe un archivo CSV con nombre "archivo_csv" que contiene dos columnas, Direecion y Barrio, de las campanas en las cuales se puede tirar el/los material/es por parámetro
        '''
        f2 = open('archivo_csv', 'w')   #Abrimos un archivo con nombre 'archivo_csv' en modo write
        f2.write('DIRECCION,BARRIO')    #Le decimos que escriba dos únicas columnas, estas siendo 'DIRECCION' y 'BARRIO'
        f2.write('\n')                  #Insertamos un "enter" para no se escriba en los títulos de las columnas
        for campana in self.campanas:   #Recorremos las campanas verdes
            if materiales == campana.materiales:             #Si el/los material/es indicado/s por parámetro se encuentran permitidos en la campana...
                f2.write(campana.direccion + ',' + campana.barrio + '\n')     #...Escribimos en el archvio la dirección de la campana y el barrio de la misma, separados por una coma para asegurarnos de que esten en la columna que les corresponda y, por ultimo ponemos un enter para que la proxima vez que una campana se escriba lo haga en la próxima fila.
        f2.close()

######################## FUNCION EXTRA PARA PODER TESTEAR ##########################################

def leer_archivo_v1(filename:str) -> str:
    ''' Requiere: filename, el cual es el nombre de un archivo de texto
        Devuelve: Todo el contenido del archivo como un único string
    '''
    f = open(filename, encoding="utf8")   # abrimos el archvio al cual llamamos filename
    todo:str = f.read() # pasamos su contenido a un string
    return todo # devolvemos ese string

####################################################################################################
