from sklearn.preprocessing import OneHotEncoder
import numpy as np


words = np.array(["cat", "dog", "bird"]).reshape(-1,1)


encoder = OneHotEncoder(sparse_output=False)

one_hot_vectors = encoder.fit_transform(words)

print("词汇表 : ", ["cat", "dog", "bird"])
print("独热编码 : ")
for i, word in enumerate(["cat", "dog", "bird"]):
    print(f"{word} -> {one_hot_vectors[i]}")



