<?php

$apiUrl  = "http://applis.matmut.fr/DevisMRSQInternet/devis.mcp/";
$genre   = array('Voiture'=>'5');
$resultat    = array();

foreach ($genre as $typeVehicule => $idType){
    
	$resultat[$idType] = array();
	$marques   = JSON_decode(file_get_contents($apiUrl."GetListeMarques?genreVehicule=$idType"),true);
	foreach($marques as $idMarque => $nomMarque){
		$resultat[$idType][$nomMarque['Text']] = array();
		$urlModel = "GetListeModeles?anneeDebut=&anneeFin=".date('Y')."&genreVehicule=$idType&marque=".urlencode($nomMarque['Text']);
		$modeles = JSON_decode(file_get_contents($apiUrl.$urlModel),true);
		foreach ($modeles as $k2 => $v2) array_push($resultat[$idType][$nomMarque['Text']], $v2['Text']);
        error_log(json_encode($resultat));
	}
}

echo json_encode($resultat);

