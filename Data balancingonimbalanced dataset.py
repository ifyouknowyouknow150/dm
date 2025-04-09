from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
import numpy as np

x,y = make_classification(n_classes = 2, weights = [0.9,0.1], n_samples = 1000, random_state= 42)
print("Class distribution before balancing :", np.bincount(y))


smote= SMOTE(random_state=42)
x_resampled , y_resampled = smote.fit_resample(x,y)

print("Class distribution after balancing :", np.bincount(y_resampled))
