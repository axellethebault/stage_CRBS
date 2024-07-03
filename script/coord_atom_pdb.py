# OBJECTIF DU SCRIPT: lire les fichiers PDB dans /gstock/mapper/CEP3 et en extraire les coordonnées des atomes
# exécuter "conda activate condathebault" dans le terminal avant de run ce script
import os 
import Bio.PDB
from Bio.PDB import PDBParser

# récupère dans une liste les noms des fichiers du dossier /gstock/mapper/CEP3
directory_path_os = '/gstock/mapper/CEP3'
list_pdb = os.listdir(directory_path_os)
points_atom = []

# lire et extraire les coordonnées x, y et z pour un fichier PDB 'name_pdb' à définir
def coord_atom (name_pdb):
    file_path = os.path.join(directory_path_os, name_pdb) #indique le chemin lié à chaque fichier 
    p = PDBParser()
    structure = p.get_structure('X', file_path)
    for atom in structure.get_atoms():
        points_atom.append(atom.get_coord()) # stocker les résultats des coordonées sous forme de variable
    return points_atom

# test pour 1 fichier PDB (le premier) 
pdb_test = list_pdb[0]
res_coord = coord_atom(pdb_test)
pass