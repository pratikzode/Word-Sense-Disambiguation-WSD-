from nltk.corpus import wordnet as wn
import numpy as np
import re
import pickle
#from OMSTIimport import *


aword=input("Enter Ambiguous Word: ")

datay=[]
sense_key_regex = r"(.*)\%(.*):(.*):(.*):(.*):(.*)"
synset_types = {1:'n', 2:'v', 3:'a', 4:'r', 5:'s'}

def synset_from_sense_key(sense_key):
    lemma, ss_type, lex_num, lex_id, head_word, head_id = re.match(sense_key_regex, sense_key).groups()
    lemma=aword
    for syn in wn.synsets(lemma):
        #print(syn.lemmas())
        for syn2 in syn.lemmas():
            #print(syn2.key())
            if syn2.key() in sense_key:
            #if syn2.key() in sense_key:
                return lemma,syn
    s=wn.synsets(lemma)[0]
    return lemma,s
            
with open("Z:\\BE Project\\Data Storage\\Sense Keys\\"+aword+"_data_sense_keys.txt", "rb") as fp:   #Pickling
    dataysensekeys=pickle.load(fp)

print(dataysensekeys, len(dataysensekeys))

jk=1
for d in dataysensekeys:
    
    word,wordidx= synset_from_sense_key(d)

    print(jk,wordidx,len(wn.synsets(word)),wordidx.definition())
    datay.append(wordidx)
    jk=jk+1
print(datay)

with open("Z:\\BE Project\\Data Storage\\Sentence Data\\"+aword+"_data_y.txt", "wb") as fp:   #Pickling
    pickle.dump(str(datay),fp)

