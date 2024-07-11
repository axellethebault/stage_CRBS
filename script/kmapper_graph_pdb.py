# OBJECTIF DU SCRIPT: utiliser l'algorithme mapper pour projeter en 2D des coordonnées d'atomes 3D de .pdb, clusteriser les points et visualiser en tant que graphe 2D

#EN COURS D'ECRITURE, SCRIPT NON FINI

# Import the class
import kmapper as km
import matplotlib as plt
import plotly.express as px
import os 
import Bio.PDB
from Bio.PDB import PDBParser
import sklearn
from sklearn.manifold import TSNE
import coord_atom_pdb

# récupère dans une liste les noms des fichiers du dossier /gstock/mapper/CEP3 et stock dans data_pdb les listes du 1er fichier PDB
directory_path_os = '/gstock/mapper/CEP3'
list_pdb = os.listdir(directory_path_os)
data_pdb = coord_atom_pdb.coord_atom(list_pdb[0])

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Fit to and transform the data
# Projection faite avec t-SNE (seed fixe) et à importer via projections_data_pdb.py
projected_data = mapper.fit_transform(data, projection=[0,1]) # X-Y axis # "data" doit être un ndarray

# Create a cover with 10 elements 
cover = km.Cover(n_cubes=10)

# Cluster the projected dataset
cluster
# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, cover=cover)

# Definition of lenses

# Create a simplicial complex
mapper.map(
    lens,
    X,
    cover=km.Cover(n_cubes=15, perc_overlap=0.4),
    clusterer=sklearn.cluster.KMeans(n_clusters=2, random_state=1618033),
)

mapper.visualize(graph, path_html="test_data_pdb.html",
                 title="data_pdb(n_samples=5000, noise=0.03, factor=0.3)")

#km.draw_matplotlib(graph, layout='kk')

