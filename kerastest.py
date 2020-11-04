import keras
from keras.layers import Dense
import pickle
from keras.models import Sequential
import numpy as np


str1="The Dentist did a fantastic job putting a crown on the enamel of my teeth"

str2="His majesty the monarch wore his crown on his head with gold and silver"


aword="crown"
with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xtr.txt", "rb") as fp:   #Pickling     
        Xtrain = pickle.load(fp)
with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xte.txt", "rb") as fp:   #Pickling       
        Xtest = pickle.load(fp)
with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Ytr.txt", "rb") as fp:   #Pickling      
        Ytrain = pickle.load(fp)
with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Yte.txt", "rb") as fp:   #Pickling     
        Ytest = pickle.load(fp)
        
        
print ("Xtrain's shape: " + str(Xtrain.shape))
print ("Ytrain's shape: " + str(Ytrain.shape))
print ("Xtest's shape: " + str(Xtest.shape))
print ("Ytest's shape: " + str(Ytest.shape))
print("Number of non zeros=",np.count_nonzero(Xtrain))  
print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
print("Number of non zeros=",np.count_nonzero(Xtest))  
print("Number of non zeros=",np.count_nonzero(Ytest,axis=1)) 
print("Data loaded from file...")
print("--------------------------------------------------")
    

model = Sequential()
model.add(Dense(150, activation='relu', input_dim=103))
model.add(Dense(16, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data

Xtrain=Xtrain.transpose()
Xtest=Xtest.transpose()
Ytrain=Ytrain.transpose()
Ytest=Ytest.transpose()


# Train the model, iterating on the data in batches of 32 samples

model.fit(Xtrain, Ytrain, epochs=10, batch_size=32)


score = model.evaluate(Xtest, Ytest, batch_size=128)



print("X=",score)
#result=model.predict(x)
#print("y=",result)































