# OBJECTIF DU SCRIPT: utiliser l'algorithme mapper pour projeter en 2D des coordonnées d'atomes 3D de .pdb, clusteriser les points et visualiser en tant que graphe 2D
import kmapper as km
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import sklearn.cluster
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
import extract_main_chain_pdb
import projections_data_pdb

# faire une CLASS pour faire du polymorphisme

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Creation of the lens (projected data using t-SNE with projections_data_pdb.py)
projected_data = projections_data_pdb.proj_t_sne

# Create a cover with 10 elements 
cover = km.Cover(n_cubes=10)
ids = np.array([x for x in range(projected_data.shape[0])])
projected_data2 = np.c_[ids, projected_data]
print(cover.fit(projected_data2))


# Calculate the optimal number of clusters required for each PDB file
opti_n_cluster = 0
score_cluster = -1 # Lowest and worst possible score returned with the silhouette score function

for n_clusters in range(2,10):
    # Initialize the clusterer with n_clusters value and a random generator, seed of 0 for reproducibility.
    clusterer = sklearn.cluster.KMeans(n_clusters=n_clusters, random_state=0)
    cluster_labels = clusterer.fit_predict(projected_data)

    # The silhouette_score gives the average value for all the samples.This gives a perspective into the density and separation of the formed clusters
    silhouette_avg = silhouette_score(projected_data, cluster_labels)
    
    if score_cluster < silhouette_avg :
        score_cluster = silhouette_avg
        opti_n_cluster = n_clusters
    print('avec', n_clusters,'le score est de ', silhouette_avg)

print('nombre optimal de clusters = ', opti_n_cluster)

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(lens=projected_data, 
                   X=extract_main_chain_pdb.df, 
                   clusterer= sklearn.cluster.KMeans(opti_n_cluster),
                   cover=cover)

# Visualize the graph
mapper.visualize(graph,
                 path_html="/home/thebault/stage/results/img/test_data_pdb.html",
                 title="Graph mapper")

km.draw_matplotlib(graph, layout='kk')

# Plot the networkx structure in a simple way
G = nx.complete_graph(164)
nx.draw(G)