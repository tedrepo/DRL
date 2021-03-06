import pandas as pd
import numpy as np
import sys
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.mixture import BayesianGaussianMixture

def my_GMM(x):
    n_clusters = range(1, 201)
    scores = []
    for n in n_clusters:
        my_gmm = GaussianMixture(n_components = n).fit(x)
        scores.append(my_gmm.score(x))
    scores = np.array(scores)
    return np.argmax(scores) + 1
    
def my_VGMM(x):
    n_clusters = 20
    my_vgmm = BayesianGaussianMixture(n_components = n_clusters, max_iter = 2000).fit(x)
    weights = my_vgmm.weights_
    weights.sort()
    weights = weights[::-1]
    count = 0
    k = 0
    for w in weights:
        count += w
        if count <= 0.9:
            k += 1
        else:
            break
    return k

if __name__ == '__main__':
    # Load the energy data
    folders = ['3level_energy_openai', '3level_maxenergy_openai', '3level_energy_denny', '1level_denny', '1level_openai', '1level_openai_argmaxsample', '3level_energy_openai_hinputI', '3level_energy_openai_hinputII']
    #game = 'breakout'
    game = 'spaceinvaders'
    #game = 'qbert'
    #game = 'seaquest'
    PATH = '/home/jingtao/Work/DRL_Data/' + game + '/'
    my_index = int(sys.argv[1])
    PATH += folders[my_index] + '/energy_data'
    df = pd.read_pickle(PATH)
    
    E0 = (df['energy0'].values).reshape(-1, 1)
    E1 = (df['energy1'].values).reshape(-1, 1)
    E2 = (df['energy2'].values).reshape(-1, 1)

    # Kmeans 
    kmeans0 = KMeans().fit(E0)
    kmeans1 = KMeans().fit(E1)
    kmeans2 = KMeans().fit(E2)
    
    K0 = kmeans0.cluster_centers_.size
    K1 = kmeans1.cluster_centers_.size
    K2 = kmeans2.cluster_centers_.size
    print("KMeans")
    print("K for Option 1: %d" % K0)
    print("K for Option 2: %d" % K1)
    print("K for Option 3: %d" % K2)
    print()
    
    # Gaussian Mixture
    K0 = my_VGMM(E0)
    K1 = my_VGMM(E1)
    K2 = my_VGMM(E2)
    print("Variational Gaussian Mixture Model")
    print("K for Option 1: %d" % K0)
    print("K for Option 2: %d" % K1)
    print("K for Option 3: %d" % K2)  
    
    
    
        
