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

    dbconncursor.execute("select perfil from desmicusuarios where usuario = '%s'" % (descodificardatos["usuario"]))

    perfil = dbconncursor.fetchall()[0][0]

    if contrasena == contrasenaenc and perfil == "Admin":
        descodificardatos["mensaje"] = "Usuario validado"
        usuariocon = open("usuariocon", "w")
        usuariocon.write("%s" % (descodificardatos["usuario"]))
        usuariocon.close()

    resultado = json.dumps(descodificardatos)
    print(resultado)

# Consulta de los usuarios, perfiles y acciones en la base de datos 
if descodificardatos["cont"] == "act":
    
    try:
        usuariocon = open("usuariocon", "r")
        descodificardatos["usuariosesion"] = usuariocon.read()
    except:
        descodificardatos["mensaje"] = "Sesion cerrada"

    
    consultausuarios = __init__.classarchmod.condbusu.condbusu(dbconn)

    descodificardatos["resultadousu"] = consultausuarios.listausuarios()

    descodificardatos["resultadoper"] = consultausuarios.listaperfiles()

    descodificardatos["resultadoacc"] = consultausuarios.listaacciones()

    resultado = json.dumps(descodificardatos)
    print(resultado)

# Cierre de la sesión del usuario
if descodificardatos["cont"] == "cerrarsesion":
    os.remove("usuariocon")

# Insercción de un nuevo usuario en la base de datos y consulta de los creados
if descodificardatos["cont"] == "crearusuario":

    contrasenaenc = hashlib.sha3_512(descodificardatos["contrasenausuario"].encode()).hexdigest()

    dbconncursor = dbconn.cursor()
    dbconncursor.execute("insert into desmicusuarios (usuario,contrasena) values ('%s','%s')" % (descodificardatos["nombreusuario"],contrasenaenc))
    dbconn.commit()

    descodificardatos["mensaje"] = "El usuario se ha creado correctamente"

    consultausuarios = __init__.classarchmod.condbusu.condbusu(dbconn)

    descodificardatos["resultadousu"] = consultausuarios.listausuarios()

    resultado = json.dumps(descodificardatos)
    print(resultado)

# Eliminación de un usuario en la base de datos y consulta de los creados
if descodificardatos["cont"] == "eliminarusu":

    dbconncursor = dbconn.cursor()

    dbconncursor.execute("select perfil from desmicusuarios where usuario = '%s'" % (descodificardatos["usuarioelim"]))

    perfil = dbconncursor.fetchall()[0][0]

    if perfil == "Admin":
        descodificardatos["mensaje"] = "El usuario seleccionado tiene perfil Admin"
    else:
        dbconncursor.execute("delete desmicusuarios.* from desmicusuarios where usuario = '%s'" % (descodificardatos["usuarioelim"]))
        dbconn.commit()
        descodificardatos["mensaje"] = "El usuario se ha eliminado correctamente"
    
    consultausuarios = __init__.classarchmod.condbusu.condbusu(dbconn)

    descodificardatos["resultadousu"] = consultausuarios.listausuarios()

    resultado = json.dumps(descodificardatos)
    print(resultado)

# Actualización del perfil de un usuario en la base de datos
if descodificardatos["cont"] == "asignarper":

    dbconncursor = dbconn.cursor()
    dbconncursor.execute("update desmicusuarios set perfil = '%s' where usuario = '%s'" % (descodificardatos["perfilusu"],descodificardatos["perfilnomusu"]))
    dbconn.commit()

    descodificardatos["mensaje"] = "El perfil se ha asignado correctamente"

    resultado = json.dumps(descodificardatos)
    print(resultado)

# Insercción de acciones en los perfiles de usuario en la base de datos
if descodificardatos["cont"] == "asignaracc":

    dbconncursor = dbconn.cursor()
    dbconncursor.execute("insert into desmicaccper values ('%s','%s')" % (descodificardatos["accionnom"],descodificardatos["perfilesacc"]))
    dbconn.commit()

    descodificardatos["mensaje"] = "La accion se ha asignado correctamente"

    resultado = json.dumps(descodificardatos)
    print(resultado)