#OBJECTIF: global function to go from a pdb file to a graph representing the 3D structure of the protein
import extract_main_chain_pdb
from kmapper_graph_pdb import KMapper
import os

class pdb_to_graph():
    def __init__(self, file_path):
        self.list_pdb = os.listdir(file_path)
        self.file_path = file_path
        
    def mapper_algo(self, n_cubes):  #Follow the Keppler Mapper algorithm
        i = 0
        for i in range (len(self.list_pdb)):
            file_name = self.list_pdb[i]
            self.res_coord = extract_main_chain_pdb.coord_atom(self.file_path, file_name)
            KMapper(file_name, self.res_coord, n_cubes)
        
results = pdb_to_graph('/gstock/mapper/CEP3')
print(results.mapper_algo(n_cubes=2))



    

        