from math import sqrt
import numpy as np
from collections import Counter
import warnings
import pandas as pd
import random



def k_nearest_neighbor(data,predict, k=3):
    if len(data) >= k:
        warning.warn('K is set lower than expected')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])
    for i in sorted(distances)[:k]:
        votes = [i[1]]
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

df = pd.read_csv("breast-cancer-wisconsin.data")
df.drop(['id'], 1, inplace = True)
df.replace('?', -99999, inplace = True)

full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[],4:[]}
test_set = {2:[],4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbor(train_set, data, k=5)
        if group == vote:
            correct+=1
        total+=1

print('Accuracy: ',correct/total)
        




