#import libraries and recommendation system
from Recommendation import System
from flask import Flask,render_template,request
import numpy as np

app = Flask('__name__')

#create recommendation system object
recommendation_system = System(path="./data/user_product_data.csv",sep=",",sim_metric="cosine",neighCount=3)
ids = recommendation_system.getNotKnownUserIds()#suggestible users
product_image_dict={"Product2":"../static/images/p2.jpg", #simple product images dataset
                    "Product3":"../static/images/p3.jpg",
                    "Product4":"../static/images/p4.jpg",
                    "Product5":"../static/images/p5.jpg",
                    "Product6":"../static/images/p6.jpg",
                    "Product10":"../static/images/p10.jpg",
                    }

#Home Page
@app.route("/")
@app.route("/index/")
def hello(): 
    return render_template('index.html',userIds=ids,isSuggest=False)

#Recommendation Page
@app.route('/recommend', methods=['POST'])
def recommend():

    Id = request.form['Id']
    if Id is None or str(Id) == "" or str(Id) == " ": #if id is empty
        return render_template('index.html',warning_message="Please, Enter Id.",userIds=ids,isSuggest=False)
    else:
        isIdOk = isIdInIds(Id)
        if isIdOk:  #if id in suggestible user ids
            Id = int(Id)
            product = str(getProduct(Id))
            return render_template('index.html',suggest=product,userIds=ids,product_src=product_image_dict[product],isSuggest=True)
        else:#wrong ids
            return render_template('index.html',warning_message="Please, Enter correct Id.",userIds=ids,isSuggest=False)
            
 
def getProduct(Id): #get product by id
   suggestable_products = recommendation_system.recommendAll(Id=Id)   
   rnd = np.random.randint(len(suggestable_products), size=1)
   product = None
   counter=0
   for k,v in suggestable_products.items():
     if counter == rnd:
       product = k
       break

     counter = counter + 1

   return product

def isIdInIds(Id):#if id in suggestible user ids return True
    Id = int(Id)
    for i in ids:
        if (i==Id):
            return True
    return False
    


if __name__ == "__main__":
    app.run(debug=True)
        