
# coding: utf-8

# In[95]:

__author__ = 'Nichlaus Jackson <nsoong@gmail.com>'
__date__ = '09.23.2014'
__version__ = 1.0
__all__ = []
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import requests
""" Please Load all data as json serialized"""
class moDel(object):
    
    def __init__(self,x):
        self.x = x
        db = pd.io.json.read_json(self.x)
        raw_data = []
        for i in range(len(db['raw_text'])):
            raw_data.append(db['raw_text'][i].encode('utf-8').strip())         
        self.Vectorizer = TfidfVectorizer(min_df=1)
        X_train = self.Vectorizer.fit_transform(raw_data)
        self.y_train = y_train = db['bull']
        self.clf = DecisionTreeClassifier().fit(X_train.toarray(),y_train)
        
        # all data going into the predict function should be fully parsed
    def predict(self,x):
        categories = ['no bias','bias']
        Vct_data = self.Vectorizer.transform([x])
        return categories[self.clf.predict(Vct_data.toarray())] ,metrics.f1_score(self.y_train,self.clf.predict(Vct_data.toarray()))
    
    def predict_other(self,x):
        categories = ['no bias','bias']
        data = []
        result=requests.post('https://api.idolondemand.com/1/api/sync/findsimilar/v1',data={'text':x,'apikey':'34fd5236-4d37-440f-99f6-16985435b18d','indexes':'news_eng','print':'all'}).json()
        for doc in result["documents"]:
            Vct_other_data = self.Vecotrizer.transform([doc['content']])
            result=self.clf.predict(Vct_other)
            score = metrics.f1_score(self.y_train,result)
            title = result['source']= doc['title']
            data.append([categories[result],score,title])
            
        return data
        

