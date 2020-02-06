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
        


