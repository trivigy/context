from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pandas as pd

class Model():
    def __init__(self):
        self._labels = {
            0 : 'Reliable',
            1 : 'Not Reliable'
        }

        self.vectorizer = TfidfVectorizer(min_df = 1)
        db = pd.read_json(data)
        X = []
        for each in db['raw_text']:
            X.append(each.encode('utf-8').strip())
        X_train = self.vectorizer.fit_transform(X)
        self.y_train = db['gender']
        self.clf = GaussianNB().fit(X_train.toarray(), self.y_train)

    def predict(self, key):
        return self.clf.predict(self.vectorizer.transform(key).toarray())[0]

    def score(self):
        metrics.f1_score(self.y_train, self.clf.predict(X_test.toarray()))

    def label(self, n):
        return self._labels.get(n)


MLearn = Model()