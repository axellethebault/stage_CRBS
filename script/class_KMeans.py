# Create a class inheriting from the scikit "KMeans" class to make a "smart" Kmeans functionality
import sklearn
import sklearn.cluster
import numpy as np
from sklearn.metrics import silhouette_score
from extract_main_chain_pdb import res_coord

data = np.array(res_coord) #np array des coordonnées 3D de la chaîne principale d'1 fichier

class SmartKMeans(sklearn.cluster.KMeans): #classe fille qui hérite de la classe KMeans de scikit, mais sans le paramètre n_cluster
    def __init__(self, init="k-means++", n_init="auto", max_iter=300, tol=1e-4, verbose=1, random_state=0, copy_x=True, algorithm="lloyd"):
        super().__init__(init=init, n_init=n_init, max_iter=max_iter, tol=tol, verbose=verbose, random_state=random_state)
    
    def find_best_model(self, data):
        opti_n_cluster = 0
        score_cluster = -1 # Lowest and worst possible score returned with the silhouette score function
        
        for n_clusters in range(2,10):
            # Initialize the clusterer with n_clusters value and a random generator, seed of 0 for reproducibility.
            clusterer = sklearn.cluster.KMeans(n_clusters=n_clusters, random_state=0)
            cluster_labels = clusterer.fit_predict(data)

            # The silhouette_score gives the average value for all the samples.This gives a perspective into the density and separation of the formed clusters
            silhouette_avg = silhouette_score(data, cluster_labels)
            
            if score_cluster < silhouette_avg :
                score_cluster = silhouette_avg
                opti_n_cluster = n_clusters

        self.opti_n_cluster = opti_n_cluster
        self.model #c quoi model
    
    def fit(self, data):
        model = self.find_best_model(data)
        return model.fit(data)


    '''def KMeans_auto(self, projected_data):
        k = sklearn.cluster.KMeans(n_clusters = self.fit(projected_data), random_state=0)
        return k'''