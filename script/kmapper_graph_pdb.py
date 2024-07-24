# OBJECTIF DU SCRIPT: utiliser l'algorithme mapper pour projeter en 2D des coordonnées d'atomes 3D de .pdb, clusteriser les points et visualiser en tant que graphe 2D
import kmapper as km
import numpy as np
from sklearn.manifold import TSNE
from extract_main_chain_pdb import res_coord
import class_KMeans

# Initialize
mapper = km.KeplerMapper(verbose=2)

# Creation of the lens (list oc 3D coordinates from extract_main_chain_pdb.py)
data = np.array(res_coord) #np array des coordonnées 3D de la chaîne principale d'1 fichier
projected_data = mapper.fit_transform(data, projection=TSNE(n_components=2, random_state=0)) 

# Create a cover with 10 elements 
Cov = km.Cover(n_cubes=10)
ids = np.array([x for x in range(projected_data.shape[0])])
projected_data2 = np.c_[ids, projected_data]
cover = Cov.fit(data = projected_data2)

# Clusterer definition
clusterer = class_KMeans.SmartKMeans()

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(lens=projected_data, 
                    X=data, 
                    clusterer= clusterer,
                    cover=Cov)

# Visualize the graph
mapper.visualize(graph,
                 path_html="/home/thebault/stage/results/img/Graph_pdb.html",
                 title="Graph mapper")

km.draw_matplotlib(graph, layout='kk')


# Plot the networkx structure in a simple way

