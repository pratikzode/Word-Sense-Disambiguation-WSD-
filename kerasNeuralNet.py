import keras
from keras.layers import Dense
import pickle
from keras.models import Sequential
import numpy as np

def train_neural_net(aword):
        
    
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xtr.txt", "rb") as fp:   #Pickling     
            Xtrain = pickle.load(fp)    
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Ytr.txt", "rb") as fp:   #Pickling      
            Ytrain = pickle.load(fp)
            
            
    Xtrain=Xtrain.transpose()
    Ytrain=Ytrain.transpose()
    
    print("--------------------------------------------------")
    print ("Xtrain's shape: " + str(Xtrain.shape))
    print ("Ytrain's shape: " + str(Ytrain.shape))
    #print("Number of non zeros=",np.count_nonzero(Xtrain))  
    #print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
    print("Data loaded from file...")
    print("--------------------------------------------------")
        
    
    model = Sequential()
    model.add(Dense(150, activation='relu', input_dim=Xtrain.shape[1]))
    model.add(Dense(Ytrain.shape[1], activation='sigmoid'))
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
  
    model.fit(Xtrain, Ytrain, epochs=100, batch_size=32)
    #score = model.predict(Xtrain, batch_size=32)
    #print(" TrX Accuracy=\n",score.transpose())
    #print(" TeX Accuracy=\n",Ytrain.transpose())
    
    print("Training Done!")
    
    with open("Z:\\BE Project\\Data Storage\\Final NN Models\\"+aword+"_model.txt", "wb") as fp:   #Pickling     
        pickle.dump(model,fp)
    return model


def test_neural_net(aword):
    
    with open("Z:\\BE Project\\Data Storage\\Final NN Models\\"+aword+"_model.txt", "rb") as fp:   #Pickling     
        model=pickle.load(fp)
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xtr.txt", "rb") as fp:   #Pickling      
        Xtest = pickle.load(fp)
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Ytr.txt", "rb") as fp:   #Pickling     
        Ytest = pickle.load(fp)
    Xtest=Xtest.transpose()
    Ytest=Ytest.transpose()
    
    print("--------------------------------------------------")
    print ("Xtest's shape: " + str(Xtest.shape))
    print ("Ytest's shape: " + str(Ytest.shape))
    #print("Number of non zeros=",np.count_nonzero(Xtest))  
    #print("Number of non zeros=",np.count_nonzero(Ytest,axis=1))
    print("Data loaded from file...")
    print("--------------------------------------------------")
    
    #score = model.predict(Xtest, batch_size=128)
    
    accu=model.evaluate(Xtest,Ytest, batch_size=128)
    acc=accu[1]*100
    print(" Testing Accuracy=\n",acc)
    #print(" Testing Accuracy=\n",Ytest.transpose())
    #print(" Testing Accuracy=",score.shape)
    return acc


aword=input("Enter Ambiguous Word: ")
model= train_neural_net(aword)
acc=test_neural_net(aword)


























