# doubanAnaly
对豆瓣电视剧中的指定电视剧页面的短评进行爬取，并存储为txt文件，爬取程序采用scrapy框架进行爬虫。将爬取短评分类为1星2星差评和4星5星好评。对爬取后的短评进行关键词分析
### 依赖环境
需要安装scrapy框架进行爬虫分析，以及gensim进行LDA分析

### autodouban
该文件实现的是Scrapy框架爬虫的自动化爬虫，命令行输入scrapy autodouban即可进行短评爬虫

### annaly.py
豆瓣影评的LDA方法关键词分析

### getComment
用于获取京东商品短评

### /autodouban/spiders/douban.py
修改待爬取电视剧的影评页面需要修改url
```python
start_urls = ['https://movie.douban.com/subject/26801052/comments?start=0&limit=20&sort=new_score&status=P']
```
完成分析后结果如图
![](https://github.com/imcy/doubanAnaly/blob/master/2017-09-18%2010-39-01%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
