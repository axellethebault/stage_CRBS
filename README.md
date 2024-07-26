But du stage: projeter, clusteriser et représenter sous forme de graphe des coordonnées d'atomes de fichiers PDB sur /gstock/mapper/CEP3 en utilisant l'algorithme keppler.mapper.

Objectifs des script:
extract_main_chain_pdb.py: renvoie une df avec les coordonnées 3D des atomes d'un .pdb.

projections_data_pdb.py: renvoie la projection en 2D des coordonnées extraites précedemment, réduction dimensionnelle avec t-SNE.

#kmapper_graph_pdb.py: renvoie le graphe networkx après clustering des données en prenant en compte le dataset de base et le dataset projeté.

#kmapper_graph_pdb.py: fonction faisant tourner l'algorithme mapper.

#class_KMeans.py: définition d'un classe similaire au KMeans de SciKit mais en version "intelligente" qui permet de calculer le nombre de cluster optimal (mesure par score.silhouette de la qualité du clustering) pour chaque cube de l'espace de clustering final.

#pdb_to_graph/py: fonction globale qui permet d'obtenir un graphe Networkx en entrant juste en paramètre le chemin du fichier .pdb qu'on veut convertir et le nombre de cubes de l'espace de clustering final.


