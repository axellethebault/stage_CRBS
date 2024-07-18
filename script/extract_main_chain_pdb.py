# OBJECTIF DU SCRIPT: lire les fichiers PDB dans /gstock/mapper/CEP3 et en extraire les chaînes principales
# se placer dans l'environnement conda "condathebault" sur vscode avant de lancer ce script
import os 
import pandas as pd 
from Bio.PDB import PDBParser

# récupère dans une liste les noms des fichiers du dossier /gstock/mapper/CEP3
directory_path_os = '/gstock/mapper/CEP3'
list_pdb = os.listdir(directory_path_os)

points_atom = []

# lire et extraire les coordonnées x, y et z des atomes de la chaîne principale "A" pour un fichier PDB 'name_pdb' à définir
def coord_atom (name_pdb):
    A = ["N", "CA", "C", "O"] # liste des atomes de la chaîne principale
    file_path = os.path.join(directory_path_os, name_pdb) #indique le chemin lié à chaque fichier 
    p = PDBParser()
    structure = p.get_structure('X', file_path)
    for atom in structure.get_atoms():
        S = atom.get_name() 
        if S in A: #on prend les atomes N, CA, C et O pour représenter la chaîne principale (liaison peptidique sans les radicaux)
            res = atom.get_coord()
            points_atom.append(res.tolist()) #stocker les résultats des coordonées sous forme de variable
    return points_atom

# test pour 1 fichier PDB (le premier) 
pdb_test = list_pdb[0]
print(pdb_test)
res_coord = coord_atom(pdb_test)
n_atoms = len(res_coord)

#print(res_coord)
#print(n_atoms)


n_row_df = list(range(0,n_atoms))

# afficher les points en 3D avec plotly

# convertir res_coord en dataframe
df = pd.DataFrame(res_coord, columns = ['x', 'y', 'z']) 
'''df.insert(3,'numero atome', n_row_df, True) # ajout d'une colonne correspondant au numéro d'atome, utile pour colorer dans le plot

# plot en 3D
fig = px.scatter_3d(df, x='x', y='y', z='z', color='numero atome', color_continuous_scale=px.colors.sequential.Turbo)
fig.update_traces(marker_size = 3)
#fig.show()'''
