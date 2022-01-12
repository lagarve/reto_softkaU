from tkinter.messagebox import NO
from DBControl import *
import random

class Jugador():
    def __init__(self):
        self._ID = None
        self._name = None
        self._passWd = None
        self._cont = None
    


    def getID(self): return self._ID
    def setID(self, id): self._ID = id

    
    def getName(self): return self._name
    def setName(self, name): self._name = name


    def getPassWd(self): return self._passWd
    def setPassWd(self, passWd): self._passWd = passWd

    def getCont(self): return self._cont
    def setCont(self, cont): self._cont = cont

    def loadUser(self, name):
        query = DBControl()
        listUser = query.getUser(name)
        if len(listUser) !=0:
            self.setID(listUser[0][0])
            self.setName(listUser[0][1])
            self.setPassWd(listUser[0][2])
            self.setCont(listUser[0][3] )
            return True
        else:
            return False
    
    def registUser(self, newUser):
        nombre = newUser[0]
        newUser = [newUser]
        query = DBControl()
        query.inserUser(newUser)
        self.loadUser(nombre)
    
    def updateCont(self, cont):
        query = DBControl()
        query.updateAcumulado(self._name, cont)



class Categoria():
    def __init__(self):
        self._ID = None
        self._categoria = None

    
    def getID(self): return self._ID
    def setID(self, id): self._ID = id
    

    def getCategoria(self): return self._categoria
    def setCategoria(self, categorie): self._= categorie

    def loadCategoria(self, categoria): 
        query = DBControl()
        result = query.getCategoria(categoria)
        self.getID(result[0][0])
        self.getCategoria(result[0][1])

        
class Premio(Categoria):
    def __init__(self):
        super().__init__()
        self._premio =None
    
    def getPremio(self): return self._premio
    def setPremio(self, reward):  self._premio = reward

    def getUnPremio(self, id):
        query = DBControl()
        premio = query.getReward(id)
        return premio[1]

    def loadPremio(self, ronda):
        query = DBControl()
        premio = query.getReward(ronda)

        self.setID(premio[0])
        self.setPremio(premio[1])
        self.setCategoria(premio[2])


class Pregunta(Categoria):
    def __init__(self):
        super().__init__()
        self._pregunta = None
    def getIDPregunta(self): return self.getID()
    def getPregunta(self): return self._pregunta
    def setPregunta(self, question):  self._pregunta = question

    def loadPregunta(self, ronda):
        query = DBControl()
        result = query.getPregunta(ronda)
        pregunta = result[random.randint(0, 4)]

        self.setID(pregunta[0])
        self.setPregunta(pregunta[1])
        self.setCategoria(pregunta[2])

class Opciones():
    def __init__(self):
        self._opciones = []
        self._Id_Pregunta = None

    def getOpciones(self): return self._opciones
    def setOptiones(self, options): self._opciones = options

    def getId_Pregunta(self): return self._Id_Pregunta
    def setId_Pregunta(self, id): self._Id_Pregunta = id

    def loadOptions(self, idPregunta):
        query = DBControl()
        self.setOptiones(query.getOptions(idPregunta))
        self.setId_Pregunta(idPregunta)

class Respuesta():
    def __init__(self):
        self._respuesta = None
        self._IdPregunta = None
    
    def getRespuesta(self): return self._respuesta
    def setRespuesta(self, id): self._respuesta = id
    
    def getIdPregunta(self): return self._IdPregunta
    def setIdPregunta(self, id): self._IdPregunta = id

    def loadRespuesta(self, idPregunta):
        query = DBControl()
        self.setRespuesta(query.getRespuesta(idPregunta))
        self.setIdPregunta(idPregunta)


class Rondas(Jugador, Pregunta, Opciones, Respuesta, Premio):
    def __init__(self, namePlayer):
        super().__init__()
        self.namePlayer = namePlayer
        self._acumulado = 0
        self.contador = 0
        self.loadRonda()

    def getContador(self): return self.contador

    def getAcumulado(self): return self._acumulado
    def setAcumulado(self, cont): self._acumulado = cont

    def acumulado(self):
        if self.contador > 1:
            self._acumulado = self._acumulado + self.getUnPremio(self.contador-1)

    def incRonda(self):
        self.contador +=1
        if self.contador >5:
            return False
        else:
            return True

    def loadRonda(self):
        if self.incRonda():
            self.loadUser(self.namePlayer)
            self.loadPremio(self.contador)
            self.loadPregunta(self.contador)
            self.loadOptions(self.getIDPregunta())
            self.loadRespuesta(self.getIDPregunta())
            self.acumulado()
        else:
            self.acumulado()

    def update(self):
        self.loadRonda()
    
    def reset(self):
        self._acumulado = 0
        self.contador = 0
        self.loadRonda()
    
    def gameOver(self):
        self._acumulado = 0
        self.contador = 0
        self.updateCont([(0,)])
        self.setPregunta("Perdiste!!!")
        self.setOptiones(["perdiste", "perdiste", "perdiste", "perdiste"])
    
    def win(self):
        self.updateCont([(500,)])
        self.setAcumulado(500)

    def giveUp(self):
        self.updateCont([(self.getAcumulado(),)])
        self.reset()



    

if __name__=="__main__":
    obj = Rondas("lala")
    obj.incRonda()
    print(obj.getOpciones())

