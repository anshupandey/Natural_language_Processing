# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:02:40 2020

@author: anshu
"""

##########################################################################
# Data Preparation

import os
import json
data = open("data\qus_data.txt","r").read()
data = data.replace("'", "\"")
data = json.loads(data)

x = []
y = []
intents = list(data.keys())
for intent_name in intents:
    for sample in data[intent_name]:
        x.append(sample)
        y.append(intents.index(intent_name))
        
##########################################################################
### Text Cleaning and Preprocessing
### intall the relevant packages
### pip install -U spacy
### python -m spacy download en_core_web_sm
import numpy as np
import spacy
nlp = spacy.load('en_core_web_sm')

# stop words and lemmatization
corpus = []
doc_size = []
N = len(x)
for i in range(0,N):
    doc = nlp(x[i])
    review = [word.lemma_ for word in doc if not word.is_stop]
    doc_size.append(len(review))
    corpus.append(" ".join(review))
    
print("Average size of all docs =  ",sum(doc_size)/len(doc_size))

y = np.array(y)
##########################################################################
### Training intent recognition model
        
MAX_SEQUENCE_LENGTH = 20
MAX_WORDS = 1000
EMBEDDING_DIM = 30

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Tokenization
tok = Tokenizer(num_words=MAX_WORDS)
tok.fit_on_texts(corpus)
sequences = tok.texts_to_sequences(corpus)

# padding - making sure ever document has same lenth
xdata = pad_sequences(sequences,maxlen=MAX_SEQUENCE_LENGTH)

#onehot encoding the label
from tensorflow.keras.utils import to_categorical
y = to_categorical(y)


# Training an LSTM Layer for intent recognition
from tensorflow.keras import models,layers

model = models.Sequential()
model.add(layers.Embedding(MAX_WORDS,EMBEDDING_DIM,input_length=MAX_SEQUENCE_LENGTH))
#add the LSTM layer
model.add(layers.LSTM(100,activation='sigmoid',dropout=0.2,recurrent_dropout=0.2))
#add a hidden layer
model.add(layers.Dense(40,activation='relu'))

#add a hidden layer
model.add(layers.Dense(20,activation='relu'))

# add the output layer
model.add(layers.Dense(len(intents),activation='sigmoid'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(xdata,y,verbose=True,batch_size=100,epochs=10,shuffle=True)

print(model.evaluate(xdata,y))
############################################################################
### Save the trained model
model.save("intent_recognizer.h5")


