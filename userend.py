from preprocessing import *
from os import path
import sys
import pickle
import numpy as np
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

        
def loadparams(awords):
    
    paramlist=[]
    for i in range(len(awords)):  
        params={}      
        with open("Z:\\BE Project\\Data Storage\\Final NN Models\\"+awords[i]+"_params.txt", "rb") as fp:   #Pickling     
            params=pickle.load(fp)
        paramlist.append(params)
    return paramlist;

def create_one_vector(awords,wordlist):
    
    veclist=[]    
    l=len(wordlist)
        
    for k in range(len(awords)):
        
        with open("Z:\\BE Project\\Data Storage\\Word Embeddings\\"+awords[k]+"_embedding.txt", "rb") as fp:   #Pickling
            wembed=pickle.load(fp)
        fvec=np.zeros(shape=(len(wembed),1),dtype='int')
        
        for i in range(len(wembed)):
            for j in range(l):
                if wembed[i]==wordlist[j]:
                    fvec[i][0]=1
                    #print("x==",i)
                    
        veclist.append(fvec)
        
    #i=2
    #print(veclist[i])
    #print(np.size(veclist[i],axis=0),np.size(veclist[i],axis=1))
    #print(print("Number of non zeros=",np.count_nonzero(veclist[i])))
    return veclist


def predict(awords,veclist):
    
    
    op=np.zeros(shape=(len(awords),),dtype='int')
    for k in range(len(awords)):
        
        with open("Z:\\BE Project\\Data Storage\\Final NN Models\\"+awords[k]+"_model.txt", "rb") as fp:   #Pickling     
            model=pickle.load(fp)
        fvec=veclist[k]
        
        fvec=fvec.transpose()
        
        #print("--------------------------------------------------")
        #print ("fvec's shape: " + str(fvec.shape))
        #print("Number of non zeros=",np.count_nonzero(fvec))  
        #print("Feature Vector loaded from file...")
        print("--------------------------------------------------")
        
        result1= model.predict(fvec, batch_size=128)
        
            
        #print(" Result=\n",result1)
        
        result=result1.transpose()
        
        maxv=np.zeros(shape=(len(result[0]),),dtype='float')
        xval=np.zeros(shape=(len(result[0]),),dtype='int')
        yval=np.zeros(shape=(len(result[0]),),dtype='int')
        
        p = np.zeros(shape=result.shape,dtype='int')
        
        for i in range(len(result[0])):
            maxv[i]=result[0][i]
            xval[i]=0
            yval[i]=i
            for j in range(len(result)):
                if result[j][i]>maxv[i]:
                    #print(probas[j][i])
                    maxv[i]=result[j][i]
                    #print(maxv[i])
                    xval[i]=j
                    yval[i]=i
                    
        for i in range(len(result[0])):      
            p[xval[i]][yval[i]]=1
        
        #print(p)
        #print(xval[0])
        
        op[k]=xval[0]
    return op
    
    
    
def retdefinition(aword,senseno):
    
    syn=wn.synsets(aword)
    return str(syn[senseno].definition())

def findops(awords,senselist):
    
    #print(len(awords))
    #print(len(userip_vecs))
    #print(len(params))
    result={}
    for i in range(len(awords)):
        #print("\nAmbiguous word= ",awords[i]) 
        #print("Predicted Sense Number= ",senselist[i])
        #print("Definition of Sense= ",retdefinition(awords[i],senselist[i]))
        result["Aword"+str(i)]=awords[i]
        result["Sense"+str(i)]=senselist[i]
        result["Def"+str(i)]=retdefinition(awords[i],senselist[i])
    return result
        
        
def run_user_end(wordlist,awords):
    print(awords)
    print(wordlist)
    veclist=create_one_vector(awords,wordlist)
    senselist=predict(awords,veclist)
    return findops(awords,senselist)






#str1=input("Enter String\n")
#str1="piano bass hello hello play guitar banjo"
#str1="This is a amortized english tree coin crown sample play musical instrument bass guitar, play apply showing off the stop words filtration."  
#str1="Eating in bed is easier said than done, as it is heavily dependant on the bedding clothing"
#str1="the dentist put a crown on my tooth"


#wordlist=preprocess(str1)                               #get list of words in sentence
#awords=findambiwords(wordlist)                          #find ambiguous words

#result=run_user_end(wordlist,awords)
