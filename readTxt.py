# -*- coding: utf-8 -*-
import pandas as pd
import jieba

inputfile='scoreNeg.txt'

data=pd.read_csv(inputfile,encoding='utf-8',header=None)
'''
l1=len(data)
data=pd.DataFrame(data[0])
l2=len(data)
print(l1,l2)
data.to_csv(inputfile,index=False,encoding='utf-8',header=False)
'''
mycut=lambda s:' '.join(jieba.cut(s))
data=data[0].apply(mycut)
print(data)
data.to_csv(inputfile,index=False,header=False,encoding='utf-8')