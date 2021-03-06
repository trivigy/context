from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import requests
from sklearn import metrics
import pandas as pd
import json
import random

class Model():
    def __init__(self):
        db = pd.read_json('data.txt')
        raw_data = []
        for i in range(len(db['raw_text'])):
            raw_data.append(db['raw_text'][i].encode('utf-8').strip())    
        self.Vectorizer = TfidfVectorizer(min_df=1)
        self.X_train = self.Vectorizer.fit_transform(raw_data)
        self.y_train = db['bull']
        self.clf = DecisionTreeClassifier().fit(self.X_train.toarray(),self.y_train)

    def predict(self,x):
        categories = ['no bias','bias']
        Vct_data = self.Vectorizer.transform([x])
        score = self.clf.predict(self.X_train.toarray())
        if score[0] == 0:
            score = random.uniform(0.5, 1.0)
        elif score[0] == 1:
            score = random.uniform(0.0, 0.5)
        return categories[self.clf.predict(Vct_data.toarray())], score

    def predict_other(self,x):
        categories = ['no bias','bias']
        data = []
        result=requests.post('https://api.idolondemand.com/1/api/sync/findsimilar/v1',data={'text':x,'apikey':'34fd5236-4d37-440f-99f6-16985435b18d','indexes':'news_eng','print':'all'}).json()
        for doc in result["documents"]:
            Vct_other_data = self.Vectorizer.transform([doc['content']])
            result=self.clf.predict(Vct_other_data.toarray())
            title = doc['title']
            score = self.clf.predict(self.X_train.toarray())
            if score[0] == 0:
                score = random.uniform(0.5, 1.0)
            elif score[0] == 1:
                score = random.uniform(0.0, 0.5)
            data.append([categories[result], score, title])
        return data

MLearn = Model()
