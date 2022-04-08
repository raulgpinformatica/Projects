
import mysql.connector

class consultadbapli:

    def __init__(self, dbconn, perfil):

        self.dbconn = dbconn
        self.perfil = perfil
    
# Consulta de las acciones de un perfil en la base de datos
    def listaaccper(self):
        dbconncursor = self.dbconn.cursor()
        dbconncursor.execute("select accion from desmicaccper where perfil = '%s'" % (self.perfil))
        
        acciones = dbconncursor.fetchall()
        listaacc = []
        for i in range(len(acciones)):
            listaacc.append(acciones[i][0])
        
        return listaacc
