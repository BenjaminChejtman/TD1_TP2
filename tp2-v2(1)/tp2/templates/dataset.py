#from haversine import haversine , Unit
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
            materiales:set[str]=set(linea['materiales'].split(' / '))
            latylng:tuple[str, str] = tuple(linea['WKT'][7:-1].split(' '))
            latitudylongitud:tuple[float, float] = (float(latylng[0]), float(latylng[1])) #ESTO NO ES CORRECTO PORQUE NO SON SIEMPRE IGUAL DE LARGOS!
            #longitud:float = float(linea['WKT'][25:41])          
            campana:CampanaVerde=CampanaVerde(direccion,barrio,comuna,materiales,latitudylongitud)
            self.campanas.append(campana)
        f.close()    


    def tamano(self) -> int:
        '''
        Requiere: un DataSet D de Campanas Verdes #deberiamos poner nada?
        Devuelve: la cantidad de Campanas Verdes en el DataSet D
        '''
        return len(self.campanas) #retornamos la len self.campanas

    def barrios(self) -> set[str]: 
        '''
        Requiere: un DataSet D de Campanas Verdes #deberiamos poner nada?
        Devuelve: un Set que contiene todos los barrios existentes en el DataSet D
            
        '''
        vrBarrios:set[str] = set()
        for campana in self.campanas:   #campana es cada campana verde en el CSV representada por lo que devuelve su REPR
            vrBarrios.add(campana.barrio)   #agregamos a vrBarrios el barrio correspondiente a cada campana, y como en un set no se repite no es necesario checkear si ya estaba o no dicho barrio
        return vrBarrios #retornamos el set de los barrios
    
    def campanas_del_barrio(self, barrio:str) -> list[CampanaVerde]:
        '''
        Requiere: un DataSet D de Campanas Verdes y un barrio en especifico
        Devuelve: una List de CampanaVerde que contiene las campanas verdes del DataSet D que estan en el barrio seleccionado
        '''
        campanasEnBarrio:list[CampanaVerde] = [] #creamos nuestra lista donde guardaremos las campanas verdes del barrio
        for campana in self.campanas:  # Recorremos las campanas verdes
            if campana.barrio == barrio: # Si el barrio de la campana coincide con el barrio seleccionado por parametro...
                campanasEnBarrio.append(campana) # ... agrgamos esa campana a nuestra lista
        return campanasEnBarrio # devolvemos la lista campanasEnBarrio
        
    def cantidad_por_barrio(self, material:str) -> dict[str, int]:
        '''
        Requiere: un DataSet D de Campanas Verdes y un material en especifico
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
        Requiere: un DataSet D de Campanas Verdes y un material en especifico
        Devuelve: un Dict que indica la cantidad de campanas verdes que hay en cada barrio en el que se puede depositar el material indicado
        '''
        campanasPorBarrio:dict[str, int] = dict()
        for campana in self.campanas:   # Recorremos las campanas verdes
            if material in campana.materiales and campana.barrio in campanasPorBarrio: # Nos fijamos si la campana verde permite el material indicado y si el barrio donde esta ya se encuentra en el Dict camapanasPorBarrio
                campanasPorBarrio[campana.barrio] = campanasPorBarrio[campana.barrio] + 1 # En caso de ser asi le agregamos uno al numero que ya habia
            elif material in campana.materiales and campana.barrio not in campanasPorBarrio: # En caso de que el material este permitido en esa campana verde pero aun no se encuentre en el Dict...
                campanasPorBarrio[campana.barrio] = 1  # ... Agregamos el barrio al Dict con un valor inicial de 1
        return campanasPorBarrio

    def tres_campanas_cercanas(self, punto:tuple[float, float]) -> tuple[CampanaVerde, CampanaVerde, CampanaVerde]: #la consigna pide lat y lng como parametros por separado, preguntar si ak hacerlo como una tupla como nosotros lo hicimos esteria bien o mal
        '''
        Requiere: Un punto del tipo Tuple que contenga su Latitud y su Longitud, ambas de tipo Float
        Devuelve: una tupla con sus tres objetos del tipo CampanaVerde, que serian las traes Campanas Verdes mas cercanas al punto ingresado
        '''
        tresMasCercanas:tuple[CampanaVerde, CampanaVerde, CampanaVerde] = (self.campanas[0], self.campanas[1], self.campanas[2]) #empezamos poniendo las tres primeras campanas que tenemos en el CSV
        for campana in self.campanas:            
            dist = campana.distancia(punto)
            primero = tresMasCercanas[0].distancia(punto)
            segundo = tresMasCercanas[1].distancia(punto)
            tercero = tresMasCercanas[2].distancia(punto)            
            if dist < primero:
                tresMasCercanas = (campana, tresMasCercanas[0], tresMasCercanas[1])
            elif dist < segundo and dist > primero:
                tresMasCercanas = tresMasCercanas[0], campana, tresMasCercanas[1]
            elif dist < tercero and dist > segundo:
                tresMasCercanas = tresMasCercanas[0], tresMasCercanas[1], campana
        return tresMasCercanas
 
    def exportar_por_materiales(self, materiales:set[str]):
        '''
        Requiere: un conjunto de materiales 'Materiales'
        Devuelve: Nada
        Modifica: EScribe un archivo CSV con nombre archivo_csv que contiene dos columnas, Direecion y Barrio, justamente incluyendo dicha informacion de las campanas en las cuales se puede tirar el/los material/es por parametro
        '''
        f2 = open('archivo_csv', 'w') # abrimos un archivo con nombre 'archivo_csv' en modo write, por eso la 'w'
        f2.write('DIRECCION,BARRIO') # le decimos que escriba como sus dos unicas columnas 'DIRECCION' y 'BARRIO'
        f2.write('\n') # Hacemos un enter para que no se escriba en los titulos de las columnas
        for campana in self.campanas: # Recorremos las campanas verdes
            if materiales == campana.materiales: # Si el material o los materiales indicados por parametro se encuentran permitidos en la campana...
                f2.write(campana.direccion + ',' + campana.barrio + '\n') # Escribimos en el archvio la direccion de la campana y el barrio de la misma, separados por una coma para asegurarnos de que esten en la columna que les corresponde, y por ultimo ponemos un enter para que la proxima vez que la proxima campana se escriba en la fila siguiente
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



#d:DataSetCampanasVerdes = DataSetCampanasVerdes('campanas-verdes-acortado.csv')
#print(leer_archivo_v1('archivo_csv'))
#print(d.tamano())
#print(d.barrios())
#print(d.cantidad_por_barrio2('Carton'))
#print(d.tres_campanas_cercanas((-58.5048544020916, -34.5746919192015)))
#print(d.exportar_por_materiales({'Papel', 'Carton'})) #los materiales vienen con el espacio que tienen en el CSV deberia eliminarse o darse por hecho que el usuario lo usara correctamente?
#print(d.campanas_del_barrio('VILLA DEVOTO'))
#print(type(d.campanas_del_barrio('VILLA DEVOTO')))
#print(d.tres_campanas_cercanas((-20.5048544020916, -34.5746919192015)))
