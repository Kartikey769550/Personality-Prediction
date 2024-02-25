import pandas as pd
from numpy import *
import numpy as np
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import neighbors

data =pd.read_csv('train.csv')
array = data.values

for i in range(len(array)):
	if array[i][0]=="Male":
		array[i][0]=1
	else:
		array[i][0]=0


df=pd.DataFrame(array)

maindf =df[[0,1,2,3,4,5,6]]
mainarray=maindf.values
print (mainarray)


temp=df[7]
train_y =temp.values
# print(train_y)
# print(mainarray)
train_y=temp.values

for i in range(len(train_y)):
	train_y[i] =str(train_y[i])



mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
mul_lr.fit(mainarray, train_y)

testdata =pd.read_csv('test.csv')
test = testdata.values

for i in range(len(test)):
	if test[i][0]=="Male":
		test[i][0]=1
	else:
		test[i][0]=0


df1=pd.DataFrame(test)

testdf =df1[[0,1,2,3,4,5,6]]
maintestarray=testdf.values
print(maintestarray)

y_pred = mul_lr.predict(maintestarray)
for i in range(len(y_pred)) :
	y_pred[i]=str((y_pred[i]))
DF = pd.DataFrame(y_pred,columns=['Predicted Personality'])
DF.index=DF.index+1
DF.index.names = ['Person No']
DF.to_csv("output.csv")

outputdata =pd.read_csv('output.csv')
output = outputdata.values
print(outputdata['Predicted Personality'])
outputdata.drop(outputdata.columns[:1], axis=1, inplace=True)
#print(type(outputdata))
testdata.drop(testdata.columns[:7], axis=1, inplace=True)
#print(type(testdata))

print('Prediction accuracy of test data : ')
print('{:.2%}\n'.format(metrics.accuracy_score(testdata, outputdata)))

from sklearn.metrics import cohen_kappa_score
cohen_score = cohen_kappa_score(testdata, outputdata)
print('Cohen-Score of test data:')
print(cohen_score)

import pickle
#pd.to_pickle(mul_lr, r'C:\Users\MANISH\PycharmProjects\personalityTY\new\model1.pickle')
mul_lr = pd.read_pickle(r'C:\Users\MANISH\PycharmProjects\personalityTY\new\model1.pickle')

gender1 = int(input("Enter your gender(Male:1,Female:0):"))
age = int(input("Enter your age(17-28) : "))
EXT1 = int(input("I am the life of the party: "))
EXT2 = int(input("I don't talk a lot:  "))
EXT3 = int(input("I feel comfortable around people:  "))
EXT4 = int(input("I am quiet around strangers:  "))

EST1 = int(input("I get stressed out easily:  "))
EST2 = int(input("I get irritated easily:  "))
EST3 = int(input("I worry about things:  "))
EST4 = int(input("I change my mood a lot:  "))

AGR1 = int(input("I have a soft heart:  "))
AGR2 = int(input("I am interested in people:  "))
AGR3 = int(input("I insult people:  "))
AGR4 = int(input("I am not really interested in others:  "))

CSN1 = int(input("I am always prepared:  "))
CSN2 = int(input("I leave my belongings around:  "))
CSN3 = int(input("I follow a schedule:  "))
CSN4 = int(input("I make a mess of things:  "))

OPN1 = int(input("I have a rich vocabulary:  "))
OPN2 = int(input("I have difficulty understanding abstract ideas:  "))
OPN3 = int(input("I do not have a good imagination:  "))
OPN4 = int(input("I use difficult words:  "))

extraversion = 0
neuroticism = 0
agreeableness = 0
conscientiousness = 0
openness = 0
extraversion = (EXT1 + EXT2 + EXT3 + EXT4)/2.50
neuroticism = (EST1 + EST2 + EST3 + EST4)/2.50
agreeableness = (AGR1 + AGR2 + AGR3 + AGR4)/2.50
conscientiousness = (CSN1 + CSN2 + CSN3 + CSN4)/2.50
openness = (OPN1 + OPN2 + OPN3 + OPN4)/2.50
def roundfigure(a):
    x = int(a)
    y = x+1
    z = float((x+y)/2)
    print(x,y,z)
    import math
    if(a<z):
        n = math.floor(a)
    else:
        n = math.ceil(a)
    return n

ext = roundfigure(extraversion)
est = roundfigure(neuroticism)
agre = roundfigure(agreeableness)
csn = roundfigure(conscientiousness)
opn = roundfigure(openness)
print(extraversion,neuroticism,agreeableness,conscientiousness,openness)
print(ext,est,agre,csn,opn)

import numpy as np
xyze = np.array([gender1,age,opn,est,csn,agre,ext])
result = mul_lr.predict([xyze])
print(result)