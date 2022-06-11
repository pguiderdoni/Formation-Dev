SELECT nom,
    prenom,
    telephone,
    ville,
    salaire 

FROM serveurs,
    employes,
    personnes,
    coordonnees 

WHERE serveurs.numpersonne= employes.numpersonne 
    and employes.numpersonne=personnes.numpersonne 
    and personnes.numpersonne=coordonnees.numpersonne 
    and salaire between 2000 and 3000;
	
	
	
	
	
	
	
	
	
	
	SELECT nom,
    prenom,
    telephone,
    ville,
    salaire 

FROM employes,
    personnes,
    coordonnees
  
WHERE  employes.numpersonne not in(
    select serveurs.numpersonne
    FROM serveurs)
    and employes.numpersonne=personnes.numpersonne 
    and personnes.numpersonne=coordonnees.numpersonne 
    and salaire between 2000 and 3000;