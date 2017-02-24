# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:10:07 2017

@author: Jialiang Yu
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba #分词包
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator #词云包
from PIL import Image
import scipy.misc
import pylab
from matplotlib import cm


file = codecs.open(u"F:\\wechat backup\\Yiwei\\Wechat messages-Leon's iphone\\201702121815-hanying\\Text format\\xiaojiang4.txt",'r')
content = file.read()
file.close()

segment = []
segs = jieba.cut(content)

for seg in segs:
    if len(seg) > 1 and seg != '\r\n':
        segment.append(seg)
print segment[0]
#停用词

words_df = pandas.DataFrame({'segment':segment})
words_df.head()
stopwords = pandas.read_csv(u"F:\\wechat backup\\Yiwei\\Wechat messages-Leon's iphone\\201702121815-hanying\\Text format\\stopwords2.txt", index_col=False,quoting=3,sep="\t",names=['stopword'],encoding="utf-8")
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]



#统计
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"count":numpy.size})
words_stat=words_stat.reset_index().sort(columns="count",ascending=False)


#词云
"""
wordcloud=WordCloud(font_path="simhei.ttf",background_color="black")
wordcloud=wordcloud.fit_words(words_stat.head(1000).itertuples(index=False))
"""
bimg = imread('F:\\Leetcode test\\heart39.png')
wordcloud = WordCloud(background_color="white", font_path="simhei.ttf", mask=bimg)

wordcloud = wordcloud.fit_words(words_stat.head(300).itertuples(index=False))
bimgColors = ImageColorGenerator(bimg)
arr = wordcloud.recolor(color_func=bimgColors)
plt.axis("off")

scipy.misc.imsave('result.jpg', arr)
#plt.imsave("result.png", arr, dpi=1000)

"""

bimg=imread('heart.jpeg')
wordcloud=WordCloud(background_color="white",mask=bimg,font_path='simhei.ttf')
wordcloud=wordcloud.fit_words(words_stat.head(39769).itertuples(index=False))
bimgColors=ImageColorGenerator(bimg)plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()

"""

















