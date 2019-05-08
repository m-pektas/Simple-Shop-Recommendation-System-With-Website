import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

class System:
    def __init__(self,path,sep,sim_metric="cosine",neighCount=2):
        self.sim_metric=sim_metric
        self.neighCount=neighCount
        self.dataset = self.load_data(path=path,sep=sep)
        self.similarityMatris = self.calculateSimilarity()
        self.notKnownUsers = self.getNotKnownUsers()
        
    #import dataset
    def load_data(self,path,sep):
         return pd.read_csv(path,sep=sep)
    
    #calculate similarity users by their overiew on product
    def calculateSimilarity(self):
        print("\nSimilarity Calculating..")
        matris = np.asmatrix(self.dataset.fillna(-1))
        sim = pairwise_distances(matris,metric=self.sim_metric)
        print("Similarity Ended.\n")
        return sim
    
    #get suggestible users from dataset
    def getNotKnownUsers(self):
        print("Not Known Users Finding..\n")
        df = self.dataset.copy()
        df = df[pd.isnull(df).any(axis=1)]
        columns = df.columns.values
        users = []
        key = False
        
        for i in df["UserId"]:
            dictin = {"Id":0,"Products":[]}
            products = []
            line = df[df["UserId"]==i].iloc[0]
            nans = np.isnan(line)
            for j in range(len(nans)):
                if nans[j]==True:
                    print(i," kişisi",columns[j],"ürünü")
                    products.append(columns[j])
                    key = True
                    
            if key==True:        
                dictin["Id"]=i
                dictin["Products"]=products
                users.append(dictin)
                
            key = False
        print("\nFiniding Finished.\n")    
        return users
    
    #get suggestible user ids
    def getNotKnownUserIds(self):
        userIds = [i["Id"] for i in self.notKnownUsers] 
        return userIds
        
    #recommend spesific user and product - not used in project last version but you can want to look
    def recommend(self,Id,product):
        similarities = self.similarityMatris.copy()
        dataset = self.dataset.copy()
        print("\nRecommandation System Running..\n")
        lenght = len(similarities)
        
        sim = [similarities[Id][i] for i in range(0,lenght)]
        sim.sort()
        sim = sim[0:self.neighCount+1]
        print("En benzerler:",sim)
        
        SimUsers = []
        for i in range(0,lenght):
            for j in range(1,len(sim)):
                if similarities[Id][i]==sim[j]:
                    SimUsers.append(i+1)    
        print("Benzeyen Kullanıcı Id'leri:",SimUsers)
        
        vals = []
        for i in SimUsers:
            x = float(dataset[dataset["UserId"]==i][product])
            vals.append(x)
            
        total = 0
        counter = 0
        for i in vals:
            if not np.isnan(i):
                total = total + i
                counter = counter + 1
        
        avg = total/counter         
        print("Total:",total)
        print("Avg:",avg)
        print("\n\n\nSonuç\n")
        if(avg>4):
            print(product," ürünü ",Id," no'lu kullanıcıya gönül rahatlığıyla önerilebilir.")
        elif(avg>3):
            print(product," ürünü ",Id," no'lu kullanıcıya önerilebilir.")
        else:
            print(product," ürünü ",Id," no'lu kullanıcıya önerilemez. !!!!")
    
        print("\nRecommendation System Ended..\n") 
        
    #recommend products to user 
    def recommendAll(self,Id):

        SuggestibleList = {}
        similarities = self.similarityMatris.copy()
        dataset = self.dataset.copy()
        print("\nRecommandation System Running..\n")
        lenght = len(similarities)
        
        sim = [similarities[Id][i] for i in range(0,lenght)]
        sim.sort()
        sim = sim[0:self.neighCount+1]
        print("En benzerler:",sim)
        
        SimUsers = []
        for i in range(0,lenght):
            for j in range(1,len(sim)):
                if similarities[Id][i]==sim[j]:
                    SimUsers.append(i+1)    
        print("Benzeyen Kullanıcı Id'leri:",SimUsers)
        
        for l in self.notKnownUsers:
            if l["Id"] == Id:
                for product in l["Products"]:                
                    print(Id,"-",product)
                    vals = []
                    for i in SimUsers:
                        x = float(dataset[dataset["UserId"]==i][product])
                        vals.append(x)
                        
                    total = 0
                    counter = 0
                    for i in vals:
                        if not np.isnan(i):
                            total = total + i
                            counter = counter + 1
                    
                    avg = total/counter   
                    print("\n\n\nSonuç\n")
                    if(avg>4):
                        print(product," ürünü ",Id," no'lu kullanıcıya gönül rahatlığıyla önerilebilir.")
                    elif(avg>3):
                        print(product," ürünü ",Id," no'lu kullanıcıya önerilebilir.")
                    else:
                        print(product," ürünü ",Id," no'lu kullanıcıya önerilemez. !!!!")
                
                    print("Total:",total)
                    print("Avg:",avg)
                    
                    SuggestibleList[product]=avg
                     
        return SuggestibleList
        print("\nRecommendation System Ended..\n")
        