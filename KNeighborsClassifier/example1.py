import time
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

training = [[1, 1], [-5, 6]]
labels  =[[1], [2]]
neigh = KNeighborsClassifier(n_neighbors=1)  #initialise the classifier
neigh.fit(training, labels)                      #fit the training set = conductors
queries = [[30, -1], [-20, 3], [1, 4], [9, 100]]
d =  neigh.predict(queries)

print(d) #print the labels for the query points
