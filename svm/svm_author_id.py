#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]


t0=time()
clf=SVC(kernel="rbf",C=10000)

clf.fit(features_train,labels_train)
print(round(time()-t0,3))


t1=time()
pred=clf.predict(features_test)


print(pred[10])
print(pred[26])
print(pred[50])


count=0
print(len(pred))
for x in range(0,len(pred)-1,1):
	if(pred[x]==1):
		count=count+1


print(count)
#print(round(time()-t1,3))

#print(clf.score(features_test,labels_test))



#########################################################
### your code goes here ###

#########################################################


