'''
SOURCE: https://www.datacamp.com/community/tutorials/deep-learning-python
'''
# Import pandas 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score

# Read in white wine data
white = pd.read_csv("winequality-white.csv", sep=';')

# Read in red wine data
red = pd.read_csv("winequality-red.csv", sep=';')

# Print info on white wine
print(white.info())

# Print info on red wine
print(red.info())

# Add `type` column to `red` with value 1
red['type'] = 1

# Add `type` column to `white` with value 0
white['type'] = 0

# Append `white` to `red`
wines = red.append(white, ignore_index=True)

# Specify the data
X=wines.ix[:,0:11]

# Specify the target labels and flatten the array 
y=wines.type

# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Define the scaler -> avg and sd must be the same of the training phase!
scaler = StandardScaler().fit(X_train)

# Scale the train set
X_train = scaler.transform(X_train)

# Scale the test set
X_test = scaler.transform(X_test)

# Initialize the constructor
model = Sequential()

# Add an input layer 
model.add(Dense(12, activation='relu', input_dim=11))

# Add one hidden layer 
model.add(Dense(10))

# Add an output layer 
model.add(Dense(1, activation='sigmoid'))

# Model output shape
model.output_shape

# Model summary
model.summary()

# Model config
model.get_config()

# List all weight tensors 
model.get_weights()

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train, y_train,epochs=10, batch_size=1, verbose=1)


y_pred = model.predict(X_test)
score = model.evaluate(X_test, y_test,verbose=1)

print(score)

# Performances scores
print(confusion_matrix(y_test, y_pred.round()))

print(precision_score(y_test, y_pred.round()))

print(recall_score(y_test, y_pred.round()))

print(f1_score(y_test,y_pred.round()))

print(cohen_kappa_score(y_test, y_pred.round()))

