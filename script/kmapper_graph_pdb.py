# OBJECTIF DU SCRIPT: utiliser l'algorithme mapper pour projeter en 2D des coordonnées d'atomes 3D de .pdb, clusteriser les points et visualiser en tant que graphe 2D
import kmapper as km
import numpy as np
from sklearn.manifold import TSNE
import class_KMeans
import networkx as nx
import matplotlib.pyplot as plt

def KMapper(file_name, res_coord, n_cubes):
    # Initialize
    mapper = km.KeplerMapper(verbose=0)

    # Creation of the lens (list oc 3D coordinates from extract_main_chain_pdb.py)
    data = np.array(res_coord) #np array des coordonnées 3D de la chaîne principale d'1 fichier
    projected_data = mapper.fit_transform(data, projection=TSNE(n_components=2, random_state=0)) 

    # Create a cover with 10 elements 
    Cov = km.Cover(n_cubes)
    '''ids = np.array([x for x in range(projected_data.shape[0])])
    projected_data2 = np.c_[ids, projected_data]
    cover = Cov.fit(data = projected_data2)'''

    # Clusterer definition
    clusterer = class_KMeans.SmartKMeans(res_coord=res_coord)

    # Create dictionary called 'graph' with nodes, edges and meta-information
    graph = mapper.map(lens=projected_data, 
                        X=data, 
                        clusterer= clusterer,
                        cover=Cov)

    # Visualize the graph
    mapper.visualize(graph,
                    path_html="/home/thebault/stage/results/Networkx_graphs/Graph_pdb_{file_name}.html".format(file_name = file_name),
                    title="Graph mapper {file_name}".format(file_name = file_name))

    km.draw_matplotlib(graph, layout='spring')

    # Get the Networkx structure with a deterministic approach and fixed layout
    G = km.adapter.to_networkx(graph) #converts the mapper.map graph into a networkx.Graph() object
    pos = nx.spring_layout(G=G, seed=0) # sets the seed to 0 so it is deterministic
    nodes = nx.draw_networkx_nodes(G, node_size=8, pos=pos)  # noqa: F841
    edges = nx.draw_networkx_edges(G, pos=pos)  # noqa: F841
    plt.savefig('/home/thebault/stage/results/Networkx_graphs/spring_layout_{file_name}.png'.format(file_name = file_name))

