from DBQuery import *
from tablas import *
import os


class DBControl(DBQuery, Tablas):
    def __init__(self, DBPath="database.db"):
        self.database = DBQuery()
        self.varTablas = Tablas()
        self.tablaJugadores = "jugadores"
        self.tablaCategorias = "categorias"
        self.tablaPremios = "premios"
        self.tablaPreguntas = "preguntas"
        self.tablaOpciones = "opciones"
        self.tablaRespuestas = "respuestas"
        self.tablaRondas = "rondas"
        self.exitDB()
        
    def exitDB(self):
        if not os.path.exists("datbase.db"):
            self.genearTablas()
            self.llenarTablas()

    def genearTablas(self):
        self.database.crearTabla(self.tablaJugadores, self.varTablas.tablaJugadores)
        self.database.crearTabla(self.tablaCategorias, self.varTablas.tablaCategorias)
        self.database.crearTabla(self.tablaPremios, self.varTablas.tablaPremios)
        self.database.crearTabla(self.tablaPreguntas, self.varTablas.tablaPreguntas)
        self.database.crearTabla(self.tablaOpciones, self.varTablas.tablaOpciones)
        self.database.crearTabla(self.tablaRespuestas, self.varTablas.tablaRespuestas)
        self.database.crearTabla(self.tablaRondas, self.varTablas.tablaRondas)

    def llenarTablas(self):
        self.database.insertar(self.tablaJugadores, self.varTablas.lengPlayer, self.varTablas.playerAdmin)
        self.database.insertar(self.tablaCategorias, self.varTablas.lengCategorie, self.varTablas.categories)
        self.database.insertar(self.tablaPremios, self.varTablas.lengReward, self.varTablas.reward)
        self.database.insertar(self.tablaPreguntas, self.varTablas.lengQuestion, self.varTablas.question)
        self.database.insertar(self.tablaOpciones, self.varTablas.lengOption, self.varTablas.Options)
        self.database.insertar(self.tablaRespuestas, self.varTablas.lengAnswer, self.varTablas.answers)        
        

    def getUser(self, nameUser):
        condicion = f"NAME = '{nameUser}'"
        result = self.database.seleccionar(self.tablaJugadores, "*", condicion)
        return result

    def inserUser(self, user):
        return self.database.insertar(self.tablaJugadores, self.varTablas.lengPlayer, user)
    
    def updateAcumulado(self, user,cont):
        query = f"UPDATE jugadores SET CONT = ? WHERE NAME = '{user}'"
        self.database.executarQuery(query, cont)

    def getCategoria(self, categoria):
        condition = f"ID = '{categoria}'"
        return self.database.seleccionar(self.tablaCategorias, "*",condition)

    def historico(self):
        query = "SELECT ID, NAME, CONT FROM jugadores ORDER BY CONT DESC"
        return self.database.executarQuery(query)
    
    def getReward(self, ronda):
        condition = f"ID = '{ronda}'"
        result = self.database.seleccionar(self.tablaPremios, "*", condition)
        return result[0]
    
    def getPregunta(self, ronda):
        condition = f"ID_CATEGORIA = '{ronda}'"
        result = self.database.seleccionar(self.tablaPreguntas, "*", condition)
        return result
    
    def getOptions(self, idPregunta):
        condition = f"ID_PREGUNTA = '{idPregunta}'"
        result = self.database.seleccionar(self.tablaOpciones, "OPCION", condition)
        return result
    
    def getRespuesta(self, idPregunta):
        condition = f"ID_PREGUNTA = '{idPregunta}'"
        result = self.database.seleccionar(self.tablaRespuestas, "RESPUESTA", condition)
        return result[0]


    

if __name__=="__main__":
    runDB = DBControl()
    runDB.updateAcumulado("lala", [(40,)])
    print(runDB.getUser("lala"))