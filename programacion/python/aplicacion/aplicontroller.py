#!/usr/bin/python

import __init__
import os, sys, json, mysql.connector, hashlib

print("Content-Type: text/html;charset=utf-8")
print("")

datos = sys.stdin.read()
descodificardatos = json.loads(datos)

dbconn = mysql.connector.connect(host="localhost", user="raulgp", password="A123a.", database="desmic")

# Comprobación de las credenciales en el inicio de sesión
if descodificardatos["cont"] == "validarcred":
    
    contrasenaenc = hashlib.sha3_512(descodificardatos["contrasena"].encode()).hexdigest()
    dbconncursor = dbconn.cursor()
    dbconncursor.execute("select contrasena from desmicusuarios where usuario = '%s'" % (descodificardatos["usuario"]))
    contrasena = dbconncursor.fetchall()[0][0]

    if contrasena == contrasenaenc:
        descodificardatos["mensaje"] = "Usuario validado"

        usuariocon = open("usuariocon", "w")
        usuariocon.write("%s" % (descodificardatos["usuario"]))
        usuariocon.close()
    
    resultado = json.dumps(descodificardatos)
    print(resultado)

# Comprobación de la sesión creada del usuario validado
if descodificardatos["cont"] == "sesionusu":

    try:
        usuariocon = open("usuariocon", "r")
        descodificardatos["usuariosesion"] = usuariocon.read()
    except:
        descodificardatos["mensaje"] = "Sesion cerrada"
    
    resultado = json.dumps(descodificardatos)
    print(resultado)

# Cierre de la sesión del usuario
if descodificardatos["cont"] == "cerrarsesion":
    os.remove("usuariocon")

# Comprobación de los permisos del usuario en el envío de parámetros del despliegue del microservicio
if descodificardatos["cont"] == "enviarparametros":

    dbconncursor = dbconn.cursor()
    dbconncursor.execute("select perfil from desmicusuarios where usuario = '%s'" % (descodificardatos["usuarioses"]))
    perfil = dbconncursor.fetchall()[0][0]

    # Comrobación del perfil del usuario
    if perfil is None:

        descodificardatos["mensaje"] = "No tienes perfil de usuario"

    else:
        
        consulta = __init__.classarchmod.consultadbapli.consultadbapli(dbconn,perfil)

        listaacc = consulta.listaaccper()
        
        # Comprobación de las acciones del perfil del usuario
        if len(listaacc) == 0:
            descodificardatos["mensaje"] = "No tienes accion en tu perfil de usuario"
        else:
            Docker = "No valido"
            Servicios = "No valido"
            HA = "No valido"
            accionprim = "Accion no validada"
            accionsec = "Accion no validada"
            accionter = "Accion no validada"

            # Comprobación de las acciones en el despliegue de microservicios
            for i in range(len(listaacc)):

                if descodificardatos["Dockerdir"] == "":
                    Docker = "Valido"
                else:
                    if listaacc[i] == "Establecer parametros del contenedor de Docker" and accionprim == "Accion no validada":
                        Docker = "Valido"
                        accionprim = "Accion validada"
                
                if listaacc[i] == "Desplegar microservicios en infraestructura de Docker" and accionsec == "Accion no validada":
                    Servicios = "Valido"
                    accionsec = "Accion validada"
                
                if descodificardatos["HAorquestador"] == "" and descodificardatos["HAreplicas"] == "":
                    HA = "Valido"
                else:
                    if listaacc[i] == "Abastecer de Alta Disponibilidad" and accionter == "Accion no validada":
                        HA = "Valido"
                        accionter = "Accion validada"
            
            # Asignación de parámetros y ejecución del despliegue del microservicio
            if Docker == "Valido" and Servicios == "Valido" and HA == "Valido":

                if descodificardatos["Dockerdir"] == "":
                    descodificardatos["Dockerdir"] = "Por_defecto"
                
                if descodificardatos["HAorquestador"] == "" and descodificardatos["HAreplicas"] == "":
                    descodificardatos["HAorquestador"] = "Sin_HA"
                    descodificardatos["HAreplicas"] = "Sin_HA"
                
                os.system("ssh -i /var/www/.ssh/rootllaveadmin root@192.168.20.15 '/root/scriptdesmicser %s %s %s %s'" % (descodificardatos["Servicios"],descodificardatos["Dockerdir"],descodificardatos["HAorquestador"],descodificardatos["HAreplicas"]))

                descodificardatos["mensaje"] = "El servicio se ha desplegado correctamente"
            else:
                descodificardatos["mensaje"] = "No tienes permiso para llevar a cabo la accion"
    
    resultado = json.dumps(descodificardatos)
    print(resultado)