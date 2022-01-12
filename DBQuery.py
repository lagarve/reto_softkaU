import sqlite3 as sql3
from tablas import *

class DBQuery():
    def __init__(self, DBPath="database.db"):
        self.__DBPath = DBPath
    
    def setPath(self, newPath):
        self.__DBPath = newPath
    
    def getPath(self):
        return self.__DBPath

    def executarQuery(self, query, param=()):
        query = query.lower()
        modif = ["insert", "update", "delete"]
        with sql3.connect(self.__DBPath) as conn:
            curs = conn.cursor()
            if (modif[0] in query) or (modif[1] in query) or (modif[2] in query): 
                curs.executemany(query, param)
            elif "select" in query:
                curs.execute(query)
                result = curs.fetchall()
                return result
            else:
                curs.execute(query, param)
            
            

    def crearTabla(self, nameTable, columns):
        query = f"CREATE TABLE IF NOT EXISTS {nameTable}({columns})"
        self.executarQuery(query)
        
    def insertar(self, nameTable, longValues,param=()):
        query = f"INSERT INTO {nameTable} VALUES({longValues})" 
        try:
            self.executarQuery(query, param)
            return True
        except: 
            return False
        
    def actualizar(self, nameTable, columns, condition, param):
        query = f"UPDATE {nameTable} SET {columns} = ? WHERE {condition}"
        self.executarQuery(query, param)

    def seleccionar(self, nameTable, columns, condition):
        query = f"select {columns} from {nameTable} where {condition}"
        result = self.executarQuery(query)
        return result
        
    def eliminar(self, nameTable, condition):
        query = f"DELETE FROM {nameTable} WHERE {condition}"
        self.executarQuery(query)
    
    









