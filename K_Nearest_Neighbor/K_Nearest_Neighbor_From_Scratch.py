from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import warnings

style.use('fivethirtyeight')

ds = {'k':[[1,2],[2,3],[3,1]],'r':[[5,6],[6,7],[7,5]]}

new_features = [3,6]


distances = []
def k_nearest_neighbor(data,predict, k=3):
    if len(data) >= k:
        warning.warn('K is set lower than expected')

    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])

    for i in sorted(distances)[:k]:
        votes = i[1]
    vote_result = Counter(votes).most_common(1)

    return vote_result

result = k_nearest_neighbor(ds,new_features,k=3)

    
print(result)


[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in ds[i]] for i in ds]
plt.scatter(new_features[0], new_features[1], s=100, color=result[0][0])
plt.show()
