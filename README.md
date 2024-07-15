But du stage: projeter, clusteriser et représenter sous forme de graphe des coordonnées d'atomes de fichiers PDB sur /gstock/mapper/CEP3 en utilisant l'algorithme keppler.mapper 

Objectifs des script:
extract_main_chain_pdb.py       #renvoie une df avec les coordonnées 3D des atomes d'un .pdb
projections_data_pdb.py         #renvoie la projection en 2D des coordonnées extraites précedemment, réduction dimensionnelle avec t-SNE
kmapper_graph_pdb.py            #renvoie le graphe networkx après clustering des données en prenant en compte le dataset de base 
                                et le dataset projeté


