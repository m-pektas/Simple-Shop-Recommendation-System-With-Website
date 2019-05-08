# Simple Shop Recommendation System With Website

This project is a simple recommendation system. Both the recommendation system and a simple website were prepared in the project. Since the project is a basic project, the user who visits the site should be given the system manually. In a real-life project, this information can be obtained from user input or cookies.

<br><br>
<h3>Methodology</h3> <br>
In this study, a sample dataset is used for the users and the points they give to the products.

Process steps;<br>
1- Calculate the similarity of all users according to the points given to the products<br>
2- Find users who have not rated at least one product and the product that has not been rated.<br>
3- Find a specific number of people who are most interested in these users.<br>
4- Calculate the average of the scores of the non-score-rated products.<br>
5-If the calculated average is positive, the product can be offered to the person. It is not recommended if negative.
<br> <br>

Recommendation system reference;<br>
Introduction to Data Mining Book - Nezahat Başeğmez - Assoc. Professor Deniz Kilinc (Page: 36-38)

<br><br>
<h3>Technical details</h3>
This project made with;
<ul>
  <li>Sklearn</li>
  <li>Numpy</li>
  <li>Flask</li>
  <li>Pandas</li>
  <li>Html</li>
  <li>Bootstap</li>
<ul>

<br><br>
<H3>Create Recommendation Object;</H3> <br>
recommendation_system = System(path="./data/user_product_data.csv",sep=",",sim_metric="cosine",neighCount=3)

<br>
<H3>Parameters;</H3><br>
path : dataset path <br>
sep : data seperator char <br>
sim_metric : similarity metric for calculate users smilarity <br>
neighCount : will use number of best similer user <br>

<br><br>
<h3>Secreenshots</h3> <br>

<img src="./screenshots/ss1.png" width="500px"/> <BR>

<img src="./screenshots/ss2.png" width="500px"/> <BR>

<img src="./screenshots/ss4.png" width="500px"/> <BR>
 
<img src="./screenshots/ss5.png" width="500px"/>

