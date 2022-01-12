from os import getlogin
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from Entidades import *

class K():
    def key(self, value):
        print(value)  


class root(Jugador):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random Dare")
        self.root.geometry("720x450")
        self.root.resizable(False, False)
        
        self._frameBase = tk.LabelFrame(self.root, bg ="ivory4")
        self._sideBar = tk.LabelFrame(self._frameBase, bg ="ivory4")
        self._mainFrame = tk.LabelFrame(self._frameBase, bg ="azure4")
        self._frameBase.pack(fill="both", expand="yes")
        
        self.sideBar()
        self.mainFrame()
    
    def mainLoop(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
    
    def lipiarCampo(self, nameEntry):
        nameEntry.delete(0, tk.END)
    
    def sideBar(self):
        self._sideBar.config(width='144', height='450')
        self._sideBar.pack(side='left')

    def mainFrame(self):
        self._mainFrame.pack(fill="both", expand="yes", side='right')

    def noVoidEntry(self, Entry):
        if Entry.get() != "":
            return True
        else:
            return False
    
    def messageBox(self, sms, title):
        messagebox.showinfo(message=sms, title= title)    

    def comparador(self, entry1, entry2):
        if entry1.get() == entry2.get():
            return True
        else:
            return False

    
    def noVoidEntrys(self, *entry):
        for i in entry:
            if not self.noVoidEntry(i):
                return False
        return True


    
  

class Game():
    def __init__(self, contenedor, namePlayer):
        self._namePlayer = namePlayer
        self.Ronda = Rondas(self._namePlayer)
        self.playerFrame = tk.Frame(contenedor, bg='azure4')
        self.playerFrame.pack(side='top', fill='x', expand=1)

        self.namePlayer = tk.Label(self.playerFrame, text="Nombre", bg='azure4')
        self.level = tk.Label(self.playerFrame, text="Nivel", bg='azure4')
        self.reward = tk.Label(self.playerFrame, text="Premio", bg='azure4')
        self.accum = tk.Label(self.playerFrame, text="acumulado", bg='azure4')

        self.namePlayer.pack(side='left')
        self.level.pack(side='right')
        self.reward.pack(side='right')
        self.accum.pack(side='right')

        #área de texto para las preguntas 
        self.questionFrame = tk.Frame(contenedor)
        self.questionFrame.pack(side='top')
        self.questionBox = tk.Text(self.questionFrame, background='azure4')
        self.questionBox.config(height=10, width=65)
        self.questionBox.pack(fill='x', expand=1)
        
    

        #radio button de las oppciones 
        self.option = tk.IntVar()
        self.radioButton = tk.Frame(contenedor)
        self.radioButton.pack(side='top', fill='x', expand=1)
        self.optionFrame = tk.Frame(self.radioButton)
        self.optionFrame.config(bg='azure4')
        self.optionFrame.pack( fill='both', expand='yes')
        self.option1 = tk.Radiobutton(self.optionFrame, text="Option1", variable=self.option, value=0, bg="azure4")
        self.option2 = tk.Radiobutton(self.optionFrame, text="Option2", variable=self.option, value=1, bg="azure4")
        self.option3 = tk.Radiobutton(self.optionFrame, text="Option3", variable=self.option, value=2, bg="azure4")
        self.option4 = tk.Radiobutton(self.optionFrame, text="Option4", variable=self.option, value=3, bg="azure4")

        self.option1.pack(side='top')
        self.option2.pack(side='top')
        self.option3.pack(side='top')
        self.option4.pack(side='top')

        #botones responder y retirarse 
        self.bottomFrame = tk.Frame(contenedor)
        self.bottomFrame.config(width=60, bg='azure4')
        self.bottomFrame.pack(side='top', fill='x', expand=1)
        self.replyButton = tk.Button(self.bottomFrame, text="Responder", relief=GROOVE, command=self.responder)
        self.giveUpButton = tk.Button(self.bottomFrame, text="Rendirse", relief=GROOVE, command= self.giveUp)
        self.replyButton.config(bg='green')
        self.giveUpButton.config(bg='red')
        self.replyButton.pack(side='right', padx=5)
        self.giveUpButton.pack(side='right', padx=5)

    
    def giveUp(self):
        jugar = messagebox.askquestion(title="GIVE UP", message="¿Desea retirarse?")
        if jugar == "yes":
            self.Ronda.giveUp()
            self.bloquearButton()
    
    def responder(self):
        opcion = self.Ronda.getOpciones()[self.option.get()][0]
        respuesta = self.Ronda.getRespuesta()[0]
        if opcion == respuesta:
            if self.Ronda.getContador() <5: #en partida
                self.Ronda.update()
                self.ronda()
            else:                           #ganar
                self.ganar()
        else:                               #perder
            self.perder()

    def ganar(self):
        jugar = messagebox.askquestion(title="WINER!!!", message="Ganaste 500 puntos.\n¿Quieres jugar una nueva?")
        if jugar == "yes":
            self.Ronda.reset()
            self.desbloquearButton()
        else:
            self.Ronda.win()
            self.bloquearButton()


    def perder(self):
        self.Ronda.gameOver()
        self.ronda()
        jugar = messagebox.askquestion(title="Game Over", message="¿Quieres volver a intentarlo?")
        if jugar == "yes":
            self.Ronda.reset()
            self.ronda()
            self.desbloquearButton()
        else:
            self.bloquearButton()

    def bloquearButton(self):
        self.replyButton['state']= DISABLED
        self.giveUpButton['state']= DISABLED
    
    def desbloquearButton(self):
        self.replyButton['state']= NORMAL
        self.giveUpButton['state']= NORMAL
       
        

    def ronda(self):
        self.namePlayer.configure(text="Jugador : "+self._namePlayer)
        self.accum.configure(text="Acumulado: "+str(self.Ronda.getAcumulado()))
        self.level.configure(text="Nivel : "+str(self.Ronda.getContador()))
        self.reward.configure(text="Premio: "+str(self.Ronda.getPremio()))
        self.questionBox.delete("1.0","end")
        self.questionBox.insert(INSERT, self.Ronda.getPregunta())
        
        self.option1.config(text=self.Ronda.getOpciones()[0])
        self.option2.config(text=self.Ronda.getOpciones()[1])
        self.option3.config(text=self.Ronda.getOpciones()[2])
        self.option4.config(text=self.Ronda.getOpciones()[3])

class Vistas(root,  Game):
    def __init__(self):
        super().__init__()
        self.crearContenedor()
        self._nameUser = None
        #botones sideBar
        self.logInButton = tk.Button(self._sideBar,text= 'Log In' , command=self.login)
        self.registButton = tk.Button(self._sideBar, text= 'Registrase', command=self.register)
        self.histButton = tk.Button(self._sideBar,text= 'Historial',  command=self.historial)
        self.auxLabel = tk.Label(self._sideBar)
        self.playButton = tk.Button(self._sideBar, text= 'Jugar',command=lambda: self.play(self._nameUser))
        


    def buttons(self):
        self.logInButton.config(bg='ivory4', relief=GROOVE)
        self.logInButton.config(width='20')
        self.logInButton.pack(side='top')
        
        self.registButton.config(bg='ivory4', relief=GROOVE)
        self.registButton.config(width='20')
        self.registButton.pack(side='top')

        self.histButton.config(bg='ivory4', relief=GROOVE)
        self.histButton.config(width='20')
        self.histButton.pack(side='top')


        self.auxLabel.config(bg='ivory4', relief=GROOVE)
        self.auxLabel.config(height='22')
        self.auxLabel.pack(fill='both', expand='yes')

        self.playButton.config(bg='ivory4', relief=GROOVE, state=DISABLED)
        self.playButton.config(width='20')
        self.playButton.pack(side='bottom')

    def vistaLogin(self, contenedor):
        self.userLabel = tk.Label(contenedor, text= "Usuario", bg="azure4")
        self.passWdLabel = tk.Label(contenedor, text="Contraseña", bg="azure4")
        self.userEntry = tk.Entry(contenedor)
        self.passWdEntry = tk.Entry(contenedor, show="*")
        self.logInButton = tk.Button(contenedor, text="Enviar", command=self.enviar)

        self.userLabel.grid(row=0, column=0, padx=10, pady=10)
        self.passWdLabel.grid(row=1, column=0, padx=10, pady=10)
        self.userEntry.grid(row=0, column=1, padx=10, pady=10)
        self.passWdEntry.grid(row=1, column=1, padx=10, pady=10)
        self.logInButton.grid(row=2, column=1)
    


    def vistaRegistro(self, contenedor):
        self.userLabel = tk.Label(contenedor, text= "Usuario", bg="azure4")
        self.passWdLabel = tk.Label(contenedor, text="Contraseña", bg="azure4")
        self.rePassWdLabel = tk.Label(contenedor, text="Repetir\nContraseña", bg="azure4")
        self.userEntry = tk.Entry(contenedor)
        self.passWdEntry = tk.Entry(contenedor, show="*")
        self.rePassWdEntry = tk.Entry(contenedor, show="*")
        self.registButton = tk.Button(contenedor, text="Registrar", command=self.registrar)

        self.userLabel.grid(row=0, column=0, padx=10, pady=10)
        self.passWdLabel.grid(row=1, column=0, padx=10, pady=10)
        self.userEntry.grid(row=0, column=1, padx=10, pady=10)
        self.passWdEntry.grid(row=1, column=1, padx=10, pady=10)
        self.rePassWdLabel.grid(row=2, column=0, padx=10, pady=10)
        self.rePassWdEntry.grid(row=2, column=1, padx=10, pady=10)
        self.registButton.grid(row=3, column=1)

    def vistaHistoricos(self, contenedor):
        self.histTable = ttk.Treeview(contenedor, columns=("nombre", "puntaje"))
        self.histTable.column("#0", width=80)
        self.histTable.column("nombre", width=80, anchor=CENTER)
        self.histTable.column("puntaje", width=80, anchor=CENTER)

        self.histTable.heading("#0", text="ID", anchor=CENTER)
        self.histTable.heading("nombre", text="NOMBRE", anchor=CENTER)
        self.histTable.heading("puntaje", text="PUNTAJE", anchor=CENTER)


        listHistorico = self.getHistorico()
        for i in listHistorico:
            self.histTable.insert("", END, text=f"{i[0]}", values=(i[1], i[2]))

        self.histTable.pack(side='top', fill='both', expand='yes')


    def registrar(self):
        if self.noVoidEntrys(self.userEntry, self.passWdEntry, self.rePassWdEntry):
            if self.comparador(self.passWdEntry, self.rePassWdEntry):
                user, passWd = self.getLogIn()
                self.jugador = Jugador()
                newUser = (user, passWd, 0)
                self.jugador.registUser(newUser)
                self.playButton['state']='normal'
                self._nameUser = user
                self.play(user)
                  
            else:
                self.messageBox("Las contraseñas no coinciden", "Error: password_register") 
                  

    def enviar(self):
        if self.noVoidEntry(self.userEntry) and self.noVoidEntry(self.passWdEntry):
            user, passWd = self.getLogIn()
            self.jugador = Jugador()
            if self.jugador.loadUser(user):
                if passWd == self.jugador.getPassWd():
                    self.playButton['state']='normal'
                    self._nameUser = user
                    self.play(user)
                    
                 
                else:
                    self.messageBox("Contraseña Incorrecta!", "Error: passWord_Error")
                    self.passWdEntry.delete(0, tk.END)
            else:
                self.messageBox("Usuario no registrado!", "Error: User_Error")
        else:
            self.messageBox("Todos los campos deben llenarse", "Error: void_Entry")

    def crearContenedor(self):
        self.contenedor = tk.Frame(self._mainFrame, bg='azure4')
        self.contenedor.pack(fill=tk.BOTH, expand=tk.YES)
    
    def getLogIn(self):
        return self.userEntry.get(), self.passWdEntry.get()

    def login(self):
        self.contenedor.destroy()
        self.crearContenedor()
        self.vistaLogin(self.contenedor)
        
    

    def register(self):
        self.contenedor.destroy()
        self.crearContenedor()
        self.vistaRegistro(self.contenedor)

    def historial(self):
        self.contenedor.destroy()
        self.crearContenedor()
        self.vistaHistoricos(self.contenedor)
        
    def play(self, namePlayer):
        self.contenedor.destroy()
        self.crearContenedor()
        self.game = Game(self.contenedor, namePlayer)
        self.game.ronda()
    
    def getHistorico(self):
        query = DBControl()
        return query.historico()
        



    
