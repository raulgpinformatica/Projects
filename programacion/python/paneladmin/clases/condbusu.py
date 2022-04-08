import mysql.connector


class condbusu:

    def __init__(self, dbconn):
        self.dbconn = dbconn

# Consulta de los usuarios creados en la base de datos   
    def listausuarios(self):
        dbconncursor = self.dbconn.cursor()
        dbconncursor.execute("select usuario from desmicusuarios")

        listausu = dbconncursor.fetchall()
        usuarios = []
        
        for i in range(len(listausu)):
            usuarios.append(listausu[i][0])
        
        return usuarios

# Consulta de los perfiles creados en la base de datos    
    def listaperfiles(self):
        dbconncursor = self.dbconn.cursor()
        dbconncursor.execute("select perfil from desmicperfiles")

        listaper = dbconncursor.fetchall()
        perfiles = []
        
        for i in range(len(listaper)):
            perfiles.append(listaper[i][0])
        
        return perfiles

# Consulta de las acciones creadas en la base de datos    
    def listaacciones(self):
        dbconncursor = self.dbconn.cursor()
        dbconncursor.execute("select accion from desmicacciones")

        listaacc = dbconncursor.fetchall()
        acciones = []
        
        for i in range(len(listaacc)):
            acciones.append(listaacc[i][0])
        
        return acciones