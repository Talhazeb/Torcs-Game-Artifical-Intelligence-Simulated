# Torcs-Game-Artifical-Intelligence-Simulated
Artificial Intelligence project in which data is first scrapped using manual control of car. That data is later trained using decision tree classifier and trained on it. Certain best attributes of car were selected for its training purpose. Each map in game required separate data and its training.

##Introduction:
In this project, we have implemented an AI based car movement based on the decision tree method. 
We have collected data by playing game manually using keys. We have collected approximately 
50000+ rows of good data. Angle, current lap time, damage, keypress, speed, time, speedx, speed-y
etc. are some of the attributes of data saved. This data is trained on model of decision tree to predict 
the movement of the car.
##Algorithm:
❖ Decision Tree
##Explaination:
Decision Tree : Decision tree is the most powerful and popular tool for classification and 
prediction. A Decision tree is a flowchart like tree structure, where each internal node 
denotes a test on an attribute, each branch represents an outcome of the test, and each 
leaf node (terminal node) holds a class label.
First we find Entropy with the help of following formula:
- ∑ni=1 Pi log2 Pi
Then we find Information Gain with the help of following formula:
H – (HL x PL + HR x PR)
-Decision trees classify instances by sorting them down the tree from the root to some leaf 
node, which provides the classification of the instance. An instance is classified by starting at 
the root node of the tree, testing the attribute specified by this node, then moving down the 
tree branch corresponding to the value of the attribute as shown in the above figure. This 
process is then repeated for the subtree rooted at the new node. 
##Benefits of Decision Trees:
-Decision trees can generate understandable rules.
-Decision trees perform classification without requiring much computation.
-Decision trees can handle both continuous and categorical variables.
-Decision trees provide a clear indication of which fields are most important for prediction or 
classification.
