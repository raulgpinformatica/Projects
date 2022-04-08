<?php


namespace clasespanel;


class condbusu
{
    private $dbconn;

    public function __construct($dbconn)
    {
        $this->dbconn = $dbconn;
    }

// Consulta de los usuarios creados en la base de datos
    function listausuarios(){

        $listausu = $this->dbconn->query("select usuario from desmicusuarios");
        $usuarios = array();
        while ($row = $listausu->fetch_array()[0]) {
            array_push($usuarios, $row);
        }

        return $usuarios;
    }

// Consulta de los perfiles creados en la base de datos
    function listaperfiles(){

        $listaper = $this->dbconn->query("select perfil from desmicperfiles");
        $perfiles = array();
        while ($row = $listaper->fetch_array()[0]) {
            array_push($perfiles, $row);
        }

        return $perfiles;
    }

// Consulta de las acciones creadas en la base de datos
    function listaacciones(){

        $listaacc = $this->dbconn->query("select accion from desmicacciones");
        $acciones = array();
        while ($row = $listaacc->fetch_array()[0]) {
            array_push($acciones, $row);
        }

        return $acciones;
    }
}