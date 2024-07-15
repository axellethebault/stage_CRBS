# OBJECTIF DU SCRIPT: projeter les coordonnées selon différentes méthodes, les représenter via px.scatter en 2D et évaluer le meilleur algorithme de projection entre UMAP et t-SNE

from sklearn.manifold import TSNE, trustworthiness
from umap import UMAP
import plotly.express as px
import pandas as pd
from extract_main_chain_pdb import res_coord, df, n_atoms

n_row_df = list(range(0,n_atoms)) #liste de 0 au nombre d'atome présents dans la chaîne principale

# projection T-SNE de la dataframe df des coordonnées du fichier PDB issue du script extract_main_chain_pdb.py
tsne = TSNE(n_components=2, random_state=0)
proj_t_sne = tsne.fit_transform(df[['x','y', 'z']]) #on projette bien que les coordonnées et pas la colonne "numero atome"
df_t_sne = pd.DataFrame(proj_t_sne, columns = ['proj_x', 'proj_y']) # conversion d'un array en df de deux colonnes

'''df_t_sne.insert(2,'numero atome', n_row_df, True) # ajout d'une colonne correspondant au numéro d'atome, utile pour colorer dans le plot selon le numéro d'atome pour mieux comparer les méthodes
fig_t_sne = px.scatter(df_t_sne, x='proj_x',y='proj_y', title='Projection t-SNE', color='numero atome', color_continuous_scale=px.colors.sequential.Turbo)
fig_t_sne.show()
print('coordonnées projetées avec t-SNE',df_t_sne)'''




# La suite du script a été écrite pour choisir entre UMAP et t-SNE pour le reste du projet, pas utile sinon

'''# projection UMAP
umap_2d = UMAP(n_components=2, init='random', random_state=0)
proj_umap = umap_2d.fit_transform(df)
df_umap = pd.DataFrame(proj_umap, columns = ['proj_x', 'proj_y'])
df_umap.insert(2,'numero atome', n_row_df, True) 
#fig_umap = px.scatter(df_umap, x='proj_x',y='proj_y', title='Projection UMAP', color='numero atome', color_continuous_scale=px.colors.sequential.Turbo)
#fig_umap.show()

# plot des deux projections sur un même graphe
fig_proj = px.scatter(df_t_sne, x='proj_x',y='proj_y', title="Scatter Plot of Two DataFrames", color='numero atome', color_continuous_scale=px.colors.sequential.Turbo)
fig_proj.add_scatter(x=df_umap['proj_x'], y=df_umap['proj_y'], mode='markers', name='df_umap')
#fig_proj.show()

# évaluation des algorithmes 
eval_t_sne = trustworthiness(res_coord, proj_t_sne, n_neighbors=5, metric='euclidean') #n_neighbors<n_atoms/2 pour assurer un output dans [0;1]
#print("evaluation of t-SNE method: \n",eval_t_sne) #donne le meilleur résultat donc on utilisera la proj t-SNE pour le clustering
eval_umap = trustworthiness(res_coord, proj_umap, n_neighbors=5, metric='euclidean')
#print("evaluation of UMAP method: \n", eval_umap)
'''