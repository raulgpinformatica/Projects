<?php

namespace clasesapli;

class consultadbapli {

    private $dbconn;
    private $perfil;

    public function __construct($dbconn, $perfil)
    {
        $this->dbconn = $dbconn;
        $this->perfil = $perfil;
    }

// Consulta de las acciones de un perfil en la base de datos
    function listaaccper(){
        $acciones = $this->dbconn->query("select accion from desmicaccper where perfil = '$this->perfil';");
        $listaacc = array();
        while ($row = $acciones->fetch_array()[0]) {
            array_push($listaacc, $row);
        }

        return $listaacc;
    }
}

?>