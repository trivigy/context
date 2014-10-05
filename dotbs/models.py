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
        cond = self.clf.predict(self.X_train.toarray())
        if cond[0] == 0:
            cond = random.uniform(0.5, 1.0)
        elif cond[0] == 1:
            cond = ranndom.uniform(0.0, 0.5)
        return categories[self.clf.predict(Vct_data.toarray())], cond

    def predict_other(self,x):
        categories = ['no bias','bias']
        data = []
        result=requests.post('https://api.idolondemand.com/1/api/sync/findsimilar/v1',data={'text':x,'apikey':'34fd5236-4d37-440f-99f6-16985435b18d','indexes':'news_eng','print':'all'}).json()
        for doc in result["documents"]:
            Vct_other_data = self.Vectorizer.transform([doc['content']])
            result=self.clf.predict(Vct_other_data.toarray())
            cond = self.clf.predict(self.X_train.toarray())
            if cond[0] == 0:
                cond = random.uniform(0.5, 1.0)
            elif cond[0] == 1:
                cond = ranndom.uniform(0.0, 0.5)
            score = cond
            title = doc['title']
            data.append([categories[result],score,title])
            return data

MLearn = Model()
