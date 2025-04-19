*******************************************************************
** Instructions pour l'utilisation des fichiers d'initialisation **
*******************************************************************


Conseils pour importer les fichiers dans Python:
------------------------------------------------

Utiliser la commande numpy.loadtxt en précisant le type de données et l'adresse du dossier (path)
ex: my_array = numpy.loadtxt(path + '\\1-num.txt', dtype = int)

La pas de discrétisation est précisé ci-dessous.


Conventions:
------------

Pour chacune des configurations proposées, 2 ou 3 matrices sont fournies:
	1) Dans tous les cas: une matrice représentant le domaine géométrique (appelée dom)
	Elle permet d'identifier
		1) les noeuds qui ne doivent pas être calculés (valeur = 0). Une frange de 0 est placée
		autour de chaque domaine.
		2) les noeuds internes qui prennent une valeur = 1.
		3) les noeuds condition limite de Dirichlet qui sont repérés par une valeur = 2.
		
     2) Dans tous les cas: une matrice (appelée num) qui donne un numéro de noeud pour chaque noeud de calcul. Cette numérotation permet d'ordonner le système à résoudre et commence par 1. Pour plus d'infos, voir la séance introductive ou avec les étudiants-moniteurs.

	3) Pour le canal rectiligne (cas test) : une matrice reprenant les valeurs des conditions de Dirichlet (appelée cl)

	4) Pour le canal plus complexe avec obstacle : une matrice contenant l'indice des noeuds définissant le contour de l'obstacle (2-contourObj.txt).
	
Informations complémentaires:
-----------------------------

1) Canal rectiligne - pas spatial = 0,5 m

2) Canal avec obstacle - pas spatial = 0,01 cm
