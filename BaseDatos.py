from pymongo import MongoClient

class BaseDatos:
    
    def __init__(self):
        
        MONGO_URI='mongodb://localhost'

        self.cliente=MongoClient(MONGO_URI)

        self.baseDatos=self.cliente['empresa']

        self.coleccion=self.baseDatos['usuarios']

    def getUsuarios(self):
        resultados=self.coleccion.find({})
        usuarios=[]
        for r in resultados:
           usuarios.append(r['user'])
        return str(usuarios).replace(',','\n').replace('[','').replace(']','')

    def validarUsuario(self,usuario,contra):
        resultados=self.coleccion.find({"user":usuario,"password":contra})
        valor=None
        for r in resultados:
            valor=r['user']
        if valor!=None:
            return True
        else:
            return False 

    def validarNombreUsuario(self,usuario):
        resultados=self.coleccion.find({"user":usuario})
        valor=None
        for r in resultados:
            valor=r['user']
        if valor!=None:
            return True
        else:
            return False                                   

    def setUsuario(self,usuario,contra):
        resultados=self.coleccion.save({"user":usuario,"password":contra});       


   