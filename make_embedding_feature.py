
from preprocessing import *
import numpy as np
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk.corpus import reuters
import pickle


def createembeddingmodel(aword):
    
    wembed=[]
    syn=wn.synsets(aword)
    for s in syn:
        sent=s.definition()
        sent1=s.examples()
        filt=preprocess(str(sent))
        filt1=preprocess(str(sent1))
        #print(filt,"\n")
        wembed=wembed+filt+filt1
    
    with open("Z:\\BE Project\\Data Storage\\Word Embeddings\\"+aword+"_embedding.txt", "wb") as fp:   #Pickling
        pickle.dump(wembed, fp)

    return wembed   




def create_feature_vectors(aword,wembed,rat=0.6):
    
    wx=wn.synsets(aword)
    inputlaynodes=len(wembed)
    print("Size of NN input: ",inputlaynodes)
    print("\nFirst 10 Entries of Word Embeddings for the word '"+aword+"' :\n")
    for i in range(10):
       print(i,wembed[i])
        
    with open("Z:\\BE Project\\Data Storage\\Sentence Data\\"+aword+"_data_x.txt", "rb") as fp:   #Pickling
        datax=pickle.load(fp)
    with open("Z:\\BE Project\\Data Storage\\Sentence Data\\"+aword+"_data_y.txt", "rb") as fp:   #Pickling
        datay=pickle.load(fp)
    
    num_sent=len(datax)
    num_senses=len(wx)
    
    featurevec=np.zeros(shape=(num_sent,inputlaynodes),dtype='int')
    opvec=np.zeros(shape=(num_sent,num_senses),dtype='int')
    k=0
    start=0
    for sent in datax[0:num_sent]:
        
        l=len(sent)
        for i in range(inputlaynodes):     #for featurevec creation
            for j in range(l):
                if wembed[i]==sent[j]:
                    featurevec[k][i-1]=1
                    
       
        s1=datay.find("Synset('",start+1)
        s2=datay.find("')",start+1)
        wordidx=datay[s1:s2+2]
        start=s2+1
        
        #print(wordidx)
        i=0
        for s in wx:                        #for opvec creation
            if wordidx == str(s):
                opvec[k][i]=1
            i=i+1
    
        #print(k)
        k=k+1
    
    
    #print(opvec)
        
    Xtrain=featurevec.transpose()
    Ytrain=opvec.transpose()
    
    #print("\nsize of X=",np.shape(Xtrain))
    
    #print(Xtrain)
    #print(Ytrain)
    
    thres=int(num_sent*rat)
    
    Xtest=Xtrain[:,thres+1:]
    Xtrain=Xtrain[:,:thres]
    
    Ytest=Ytrain[:,thres+1:]
    Ytrain=Ytrain[:,:thres]
    
    
    print("\nsize of Xtrain=",np.shape(Xtrain))
    print("size of XTest=",np.shape(Xtest))
    print("size of YTrain=",np.shape(Ytrain))
    print("size of YTest=",np.shape(Ytest))
    
    
    print("Number of non zeros=",np.count_nonzero(Xtrain))  
    print("Number of non zeros=",np.count_nonzero(Ytrain,axis=1))  
    print("Number of non zeros=",np.count_nonzero(Xtest))  
    print("Number of non zeros=",np.count_nonzero(Ytest,axis=1))  
    
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xtr.txt", "wb") as fp:   #Pickling
        pickle.dump(Xtrain, fp)
    
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Xte.txt", "wb") as fp:   #Pickling
        pickle.dump(Xtest, fp)
        
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Ytr.txt", "wb") as fp:   #Pickling
        pickle.dump(Ytrain, fp)
    
    with open("Z:\\BE Project\\Data Storage\\Feature Vectors\\"+aword+"Yte.txt", "wb") as fp:   #Pickling
        pickle.dump(Ytest, fp)

    print("\nTraining and Testing Data Successfully written to files...\n")






#aword="crown"
aword=input("Enter Ambiguous Word: ")
wembed=createembeddingmodel(aword)
  
print(wembed)
print(len(wembed))
create_feature_vectors(aword,wembed)













