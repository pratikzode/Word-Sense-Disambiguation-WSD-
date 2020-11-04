from lxml import etree
import os
import pickle
from nltk.corpus import wordnet as wn
import sys

def importdata(aword,corpi):

            
    datax=[]
    datay=[]
    
    print("Processing Dataset....\n")
    if corpi == 1:
        with open("Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor.data.xml","r") as f:
            file_content = f.read()
            tree = etree.XML(file_content)
    elif corpi == 2:
        with open("Z:\BE Project\Training Data\WSD_Training_Corpora\SemCor+OMSTI\\semcor+omsti.data.xml","r") as f:
            file_content = f.read()
            tree = etree.XML(file_content)
    else:
        sys.exit("Invalid Entry")
    
            
    s_ids =    tree.xpath('//sentence[instance/@lemma="'+aword+'"]/@id')
    
    
    print("S_ids found=",len(s_ids))
    #print(s_ids)
    for sid in s_ids:
        #sent = tree.xpath('//sentence[@id="'+str(sid)+'"]/instance/text()')
        sentlemma = tree.xpath('//sentence[@id="'+str(sid)+'"]//@lemma')
        #print("\n",sent)
        datax.append(sentlemma)
        
    print("-----------------------------------+++")
    print("Occurences of the word ",aword,":")
    print("---------------")
    
    
    for i in s_ids:
        wx=tree.xpath('//instance[@lemma="'+aword+'" and ../@id="'+i+'"]/@id')
        print("s:"+str(i)+" ; wnsn:"+str(wx))
        datay.append(wx)
    
    
    print("-----------------------------------+++")
    print("-----------------------------------+++")
    
    dataysensekeys=[]
        
    linno=0  
    if corpi == 1:
        fil = open('Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor.gold.key.txt', "rt")
    else:
        fil = open('Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor+OMSTI\\semcor+omsti.gold.key.txt', "rt")
    
    print("Traversing Key file...\n")
    for f in fil:
        linno=linno+1
        for i in range(len(datay)):
            if datay[i][0] in f:
                #print(linno,"---",f)
                s1=f.find(aword)
                dataysensekeys.append(f[s1:-1])
    fil.close()
    
    print("Data Sense Keys of Sentences Found:\n")
    print(dataysensekeys)
    
    
    print("Data x:",datax)
    print("\nNumber of Sentences found in Dataset containing the word '"+aword+"'=",len(datax))
    #print("len of dataysensekeys=",len(datay))
    
    with open("Z:\\BE Project\\Data Storage\\Sentence Data\\"+aword+"_data_x.txt", "wb") as fp:   #Pickling
        pickle.dump(datax, fp)
    with open("Z:\\BE Project\\Data Storage\\Sense Keys\\"+aword+"_data_sense_keys.txt", "wb") as fp:   #Pickling
        pickle.dump(dataysensekeys, fp)
        

aword=input("Enter Ambiguous Word: ")
corpi=input("Select Corpus of Data:\n1.SemCor\n2.OMSTI\n-------------\n")
 
importdata(aword,int(corpi))
    
    