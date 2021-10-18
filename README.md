# TDLOG-D-BG
Notre projet porte sur l'ajout d'un add-on sur le logiciel de conception 3D open-source free-CAD : https://www.freecadweb.org/.
Cet add-on est une implémentation d'une méthode d'optimisation topologique récente : https://github.com/yuanming-hu/spgrid_topo_opt.
L'add-on devra donc :
-télécharger automatiquement tous les packages nécessaires au fonctionnement de l'add-on
-présenter une petite interface liée au logiciel CAD permettant d'indiquer les conditions limites (déplacement et force), les caractéristiques du matériaux, la proportion de matière gardée et les parties du solide non affectée. On s'inspirera pour cela d'un add-on d'optimisation déjà existant. (https://forum.freecadweb.org/viewtopic.php?t=15460)
-faire le lien entre le mailleur et le code d'optimisation puis importer le résultat pour l'afficher dans freeCAD
