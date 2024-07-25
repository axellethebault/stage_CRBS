# Create a class inheriting from the scikit "KMeans" class to make a "smart" Kmeans functionality
import sklearn
import sklearn.cluster
import numpy as np
from sklearn.metrics import silhouette_score

class SmartKMeans(sklearn.cluster.KMeans): #classe fille qui hérite de la classe KMeans de scikit, mais sans le paramètre n_cluster
    def __init__(self, res_coord, init="k-means++", n_init="auto", max_iter=300, tol=1e-4, verbose=1, random_state=0, copy_x=True, algorithm="lloyd"):
        super().__init__(init=init, n_init=n_init, max_iter=max_iter, tol=tol, verbose=verbose, random_state=random_state) 
        self.res_coord = res_coord
        self.data = np.array(res_coord) #np array des coordonnées 3D de la chaîne principale d'1 fichier

    def _find_best_model(self, data): #best_model = KMeans avec n_cluster optimisé
        max_score_cluster = -1 # Lowest and worst possible score returned with the silhouette score function
       
        max_range=20
        if max_range > len(data):  # On vérifie que il y a au moins 20 data, sinon on reduit le nombre de cluster maximal  
            max_range = len(data)
        '''print('max range = ', max_range)
        print('size data =', len(data))'''
        
        # Initialize the clusterer with n_clusters value and a random generator, seed of 0 for reproducibility.
        for n_clusters in range(2,max_range-1):
            clusterer = sklearn.cluster.KMeans(n_clusters=n_clusters, random_state=0)
            cluster_labels = clusterer.fit_predict(data)

        # The silhouette_score gives the average value for all the samples.This gives a perspective into the density and separation of the formed clusters
            silhouette_avg = silhouette_score(data, cluster_labels)
            
            if max_score_cluster < silhouette_avg :
                max_score_cluster = silhouette_avg
                self.model = clusterer
            
    def fit(self, data):
        self.find_best_model(data)
        return self.model.fit(data)
    
    def fit_predict(self,data):
        self._find_best_model(data)
        return self.model.fit_predict(data)
