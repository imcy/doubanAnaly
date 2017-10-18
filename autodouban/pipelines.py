# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class AutodoubanPipeline(object):
    def __init__(self):
        self.file1 = codecs.open('./1.txt', 'a', encoding='utf-8')
        self.file2 = codecs.open('./2.txt', 'a', encoding='utf-8')
        self.file3 = codecs.open('./3.txt', 'a', encoding='utf-8')
        self.file4 = codecs.open('./4.txt', 'a', encoding='utf-8')
        self.file5 = codecs.open('./5.txt', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        for j in range(len(item["name"])):
            name = item["name"][j]
            score = item["score"][j]
            comment = item["comment"][j]
            #data = {"comment": comment,"score": score,"name":name}
            #i = json.dumps(dict(item), ensure_ascii=False)
            #line = name+" "+score+" " +comment+'\n'
            #line=i+'\n'
            if score=="力荐":
                self.file5.write(comment+'\n')
            elif score=="推荐":
                self.file4.write(comment+'\n')
            elif score=="还行":
                self.file3.write(comment+'\n')
            elif score=="较差":
                self.file2.write(comment+'\n')
            elif score=="很差":
                self.file1.write(comment+'\n')
            #print(line)
            #self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file1.close()
        self.file2.close()
        self.file3.close()
        self.file4.close()
        self.file5.close()
