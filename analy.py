# -*- coding: utf-8 -*-
import pandas as pd

negfile='scoreNeg.txt'
posfile='scorePos.txt'
stoplist='stoplist.txt'
neg=pd.read_csv(negfile,encoding='utf-8',header=None)
pos=pd.read_csv(posfile,encoding='utf-8',header=None)

stop=pd.read_csv(stoplist,encoding='utf-8',header=None)
stop=[' ','']+list(stop[0]) # 手动添加空格
neg[1]=neg[0].apply(lambda s:s.split(' '))  # 定义分割
neg[2]=neg[1].apply(lambda x:[i for i in x if i not in stop])  # 去停用词

pos[1]=pos[0].apply(lambda s:s.split(' '))  # 定义分割
pos[2]=pos[1].apply(lambda x:[i for i in x if i not in stop])  # 去停用词

from gensim import corpora,models

neg_dic=corpora.Dictionary(neg[2]) # 建立词典
neg_corpus=[neg_dic.doc2bow(i) for i in neg[2]]

neg_lda=models.LdaModel(neg_corpus,num_topics=3,id2word=neg_dic)
for i in range(3):
    print(neg_lda.print_topic(i))
print('\n')
pos_dic=corpora.Dictionary(pos[2]) # 建立词典
pos_corpus=[pos_dic.doc2bow(i) for i in pos[2]]

pos_lda=models.LdaModel(pos_corpus,num_topics=3,id2word=pos_dic)
for i in range(3):
    print(pos_lda.print_topic(i))