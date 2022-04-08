<?php

require ("vendor/autoload.php");

    $datos = file_get_contents('php://input');
    $descodificardatos = json_decode($datos, true);

    $dbconn = new mysqli("localhost", "raulgp", "A123a.", "desmic");


// Comprobación de las credenciales en el inicio de sesión
    if ($descodificardatos["cont"] == "validarcred") {

        $contrasenaenc = hash("sha3-512", $descodificardatos["contrasena"]);
        $contrasena = $dbconn->query("select contrasena from desmicusuarios where usuario = '{$descodificardatos["usuario"]}'");

        $perfil = $dbconn->query("select perfil from desmicusuarios where usuario = '{$descodificardatos["usuario"]}'");

        if (($contrasena->fetch_array()[0] == $contrasenaenc) && ($perfil->fetch_array()[0] == "Admin")) {
            $descodificardatos["mensaje"] = "Usuario validado";

            session_start();
            $_SESSION['usuariocon'] = $descodificardatos["usuario"];
        }

        $resultado = json_encode($descodificardatos);
        echo $resultado;
    }

// Consulta de los usuarios, perfiles y acciones en la base de datos 
    if ($descodificardatos["cont"] == "act") {

        session_start();

        if (isset($_SESSION['usuariocon'])) {
            $descodificardatos["usuariosesion"] = $_SESSION['usuariocon'];
        }
        else {
            $descodificardatos["mensaje"] = "Sesion cerrada";
        }

        $consultausuarios = new \clasespanel\condbusu($dbconn);

        $descodificardatos["resultadousu"] = $consultausuarios->listausuarios();


        $descodificardatos["resultadoper"] = $consultausuarios->listaperfiles();


        $descodificardatos["resultadoacc"] = $consultausuarios->listaacciones();

        $resultado = json_encode($descodificardatos);
        echo $resultado;
    }

// Cierre de la sesión del usuario
    if ($descodificardatos["cont"] == "cerrarsesion") {

        session_start();
        session_destroy();
    }

// Insercción de un nuevo usuario en la base de datos y consulta de los creados
    if ($descodificardatos["cont"] == "crearusuario") {

        $contrasenaenc = hash("sha3-512",$descodificardatos["contrasenausuario"]);

        $dbconn->query("insert into desmicusuarios (usuario,contrasena) values ('{$descodificardatos["nombreusuario"]}','{$contrasenaenc}');");

        $descodificardatos["mensaje"] = "El usuario se ha creado correctamente";

        $consultausuarios = new \clasespanel\condbusu($dbconn);

        $descodificardatos["resultadousu"] = $consultausuarios->listausuarios();

        $resultado = json_encode($descodificardatos);
        echo $resultado;
    }

// Eliminación de un usuario en la base de datos y consulta de los creados
    if ($descodificardatos["cont"] == "eliminarusu") {

        $perfil = $dbconn->query("select perfil from desmicusuarios where usuario = '{$descodificardatos["usuarioelim"]}';");

        if ($perfil->fetch_array()[0] == "Admin") {
            $descodificardatos["mensaje"] = "El usuario seleccionado tiene perfil Admin";
        }
        else {
            $dbconn->query("delete desmicusuarios.* from desmicusuarios where usuario = '{$descodificardatos["usuarioelim"]}';");
            $descodificardatos["mensaje"] = "El usuario se ha eliminado correctamente";
        }

        $consultausuarios = new \clasespanel\condbusu($dbconn);

        $descodificardatos["resultadousu"] = $consultausuarios->listausuarios();

        $resultado = json_encode($descodificardatos);
        echo $resultado;
    }

// Actualización del perfil de un usuario en la base de datos
    if ($descodificardatos["cont"] == "asignarper") {

        $dbconn->query("update desmicusuarios set perfil = '{$descodificardatos["perfilusu"]}' where usuario = '{$descodificardatos["perfilnomusu"]}';");
        $descodificardatos["mensaje"] = "El perfil se ha asignado correctamente";

        $resultado = json_encode($descodificardatos);
        echo $resultado;

    }

// Insercción de acciones en los perfiles de usuario en la base de datos
    if ($descodificardatos["cont"] == "asignaracc") {

        $dbconn->query("insert into desmicaccper values ('{$descodificardatos["accionnom"]}','{$descodificardatos["perfilesacc"]}');");
        $descodificardatos["mensaje"] = "La accion se ha asignado correctamente";

        $resultado = json_encode($descodificardatos);
        echo $resultado;

    }
