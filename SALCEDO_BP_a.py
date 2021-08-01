# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:41:55 2020

@author: gtxnn
"""
# Import the libraries for:
# Mathematical computations on arrays and matrices
import numpy as np
# manipulating data via DataFrames, 2-D tabular, column-oriented data structure
import pandas as pd
# producing plots and other 2D data visualizations. Use plotly if you want interactive graphs
import matplotlib.pyplot as plt 
# statistical visualizations (a wrapper around Matplotlib)
import seaborn as sns 
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
import time

warnings.filterwarnings("ignore")
sns.set(style="white", color_codes=True)

start_time = time.time()

# Assign the csv data to a DataFrame
data = pd.read_csv("Iris.csv")

# Replace Iris-setosa with 0, Iris-versicolor:1 and Iris-virginica:2 
from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()
data["Species"] = labelencoder.fit_transform(data["Species"])
# data["Species"]
# Construct a dataframe from a dictionary
species = pd.DataFrame({'Species': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']})

def create_dummies(df,column_name):
    dummies = pd.get_dummies(df[column_name],prefix=column_name)
    df = pd.concat([df,dummies],axis=1)
    return df
data = create_dummies(data,"Species")
data.head(n=10)

#==============================================================================================================

X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']

# Sample the train data set while holding out 20% for testing (evaluating) the classifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = True)
# X_train

# Features before mean normalization
unscaled_features = X_train

# Mean Normalization (Standarize the features to follow the normal distribution, to obtain a faster & better classifier)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
X_train_array = sc.fit_transform(X_train.values) #calculate μ & σ(fit) and apply the transformation(transform)

# Assign the scaled data to a DataFrame & use the index and columns arguments to keep your original indices and column names:
X_train = pd.DataFrame(X_train_array, index=X_train.index, columns=X_train.columns)

# Center test data. Use the μ & σ computed (fitted) on training data
X_test_array = sc.transform(X_test.values)
X_test = pd.DataFrame(X_test_array, index=X_test.index, columns=X_test.columns)

#=======================================================================================================================
a = 4 * 1 * 3
b = 4 * 10 * 3
c = 4 * 2 * 2 * 3

network_type = b

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(network_type),solver='sgd',learning_rate_init=0.01,max_iter=500)

mlp.fit(X_train, y_train)

X_train_array = X_train.values
y_train_array = y_train.values

from sklearn.model_selection import cross_val_score
scores = cross_val_score(mlp, X_train_array,y_train_array,cv =3, scoring = 'accuracy')

#the samples are balanced across target classes hence the accuracy and the F1-score are almost equal.
f1_scores = cross_val_score(mlp, X_train_array,y_train_array,cv =3, scoring ='f1_macro')
#print("Mean Accuracy: %0.4f (+/- %0.4f) \n" % (scores.mean(), scores.std() * 2))

#================================================================================================================

# Learning curve (error vs number of training samples) 
from sklearn.model_selection import learning_curve
# train_sizes means you progressively add more data into your model. 
# For each of these train_sizes you have a different model trained upon
# We have 150 tr.examples where the 20% of them are the validation set, so the plot will reach 120 tr.examples


mlp = MLPClassifier(hidden_layer_sizes=(network_type),solver='sgd',learning_rate_init=0.01,max_iter=80)
from sklearn.model_selection import ShuffleSplit
# Cross validation with 100 iterations to get smoother mean test and train
# score curves, each time with 20% data randomly selected as a validation set.
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
train_sizes, train_scores, validation_scores = learning_curve(
                                                   mlp, X,  y, cv = cv, n_jobs=5)    
"""
To plot the learning curve, 
we need only a single error score per training set size, so we average row-wise for the y axis of the plot.
"""

plt.style.use('seaborn')

# Calculate mean and standard deviation for training set scores
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)

# Calculate mean and standard deviation for test set scores
validation_scores_mean = np.mean(validation_scores, axis=1)
validation_scores_std = np.std(validation_scores, axis=1)

# Plot the std deviation as a transparent range at each training set size
plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="lightgreen")
plt.fill_between(train_sizes, validation_scores_mean - validation_scores_std, validation_scores_mean + validation_scores_std, alpha=0.1, color="b")

# Plot mean accuracy scores for training and test sets score lines at each training set size

# Easy to fit a model with a small number of data points (1 to 40)
plt.plot(train_sizes, train_scores_mean, 'o-', color="lightgreen", label="Training score")
# Usually,its hard to predict for model with a small number of data points(1 to 40)
plt.plot(train_sizes, validation_scores_mean, 'o-', color="b", label="Cross-validation score")

# Create plot
plt.title("Learning Curve Backpropgation (4-10-3 Network)")
plt.xlabel("Number of training examples")
plt.ylabel("Score")
plt.tight_layout()
plt.legend()
plt.show()
print("===============================================")
print("Time and Performance Statistics: ")
print("Time to execute: %0.5f seconds" % (time.time() - start_time))
print("\nMean Accuracy: %0.4f (+/- %0.4f) \n" % (scores.mean(), scores.std() * 2))
print("Error Scores: " + str(train_scores_mean - validation_scores_mean))




   
 
