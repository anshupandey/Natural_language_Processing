# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:05:21 2020

@author: anshu
"""

qus_data = {}
ans_data = {}

while True:
    intent = input("Enter the intent name: ")
    if intent=='exit':
        break
    qus_data[intent]=[]
    ans_data[intent]=[]
    print("Enter Question")
    while True:
        qus = input('qus: ')
        if qus=='exit':
            break
        qus_data[intent].append(qus)
    print("Enter Answer")
    while True:
        ans = input("ans: ")
        if ans=='exit':
            break
        ans_data[intent].append(ans)
        


