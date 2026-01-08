import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from .models import Observation

def predict(to_predict):
    array = np.array(Observation.objects.values_list('feature0', 'feature1', 'category',))
    features = array[:, :-1]
    categories = array[:, -1]

    scaler = StandardScaler()
    scaler.fit_transform(features)

    classifier = KNeighborsClassifier()
    classifier.fit(features, categories)

    to_predict = scaler.transform([to_predict])

    return classifier.predict(to_predict)[0]
