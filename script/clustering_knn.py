# OBJECTIF DU SCRIPT: clusteriser la projection issue de t-SNE
#PAS FINI, ne fonctionne pas

import sklearn
import projections_data_pdb
import plotly.express as px

# Clustering des données de projection
cluster_knn = sklearn.neighbors.NearestNeighbors(n_neighbors=5, radius=1.0)
cluster_knn.fit(projections_data_pdb.df_t_sne[['proj_x','proj_y']])
cluster_knn.kneighbors_graph(projections_data_pdb.df_t_sne[['proj_x','proj_y']], n_neighbors=None)

# Visualisation des clusters
fig_cluster = px.scatter(cluster_knn, x='proj_x',y='proj_y', title='Clustering t-SNE', color='numero atome', color_continuous_scale=px.colors.sequential.Turbo)
fig_cluster.show()


# Vérifier le clustering avec score silhouette