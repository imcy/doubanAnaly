# -*- coding: utf-8 -*-
import re,requests,json
import codecs
from bs4 import BeautifulSoup

file1=codecs.open('scorePos.txt','a', encoding='utf-8')
file2=codecs.open('scoreNeg.txt','a', encoding='utf-8')

s=requests.session()
url='https://club.jd.com/comment/productPageComments.action'
data={
    'callback':'fetchJSON_comment98vv13933',
    'productId':'5001209',
    'score':0,
    'sortType':5,
    'page':0,
    'pageSize':10,
    'isShadowSku':0,
    'fold':1
}
while True:
    t=s.get(url,params=data).text
    try:
        t=re.search(r'(?<=fetchJSON_comment98vv13933\().*(?=\);)',t).group(0)
    except Exception as e:
        break
    j=json.loads(t)
    commentSummary=j['comments']
    for comment in commentSummary:
        c_content=comment['content']  # 评论
        c_time=comment['referenceTime']
        c_name=comment['nickname']
        c_client=comment['userClientShow']
        score=comment['score']
        print(score)
        print('{} {} {}\n{}\n'.format(c_name,c_time,c_client,c_content))
        if score>=4:
            file1.write(c_content+'\n')
        if score<=3:
            file2.write(c_content+'\n')
    data['page']+=1

file1.close()
file2.close()