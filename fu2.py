#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
import xlsxwriter
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
from nltk.stem import WordNetLemmatizer


# 文本预处理  作为fu.py的参考
# workbook = xlsxwriter.Workbook("./2（3）FU(2).xlsx")
# sheet = workbook.add_worksheet('文本预处理')
# sheet.write(0,0,0)
# workbook.close()
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/文本聚类方法/2（3）FU(1).xlsx")
# table = data.sheet_by_index(0)
# num = table.nrows
# fu1 = {"name1" : [], "names" : [], "fucodes" : []}
# sheetrow = 0
# for i in range(num):
# 	a = table.row_values(i)
# 	# 小写化
# 	name = a[0].strip().lower()
# 	nameli = []
# 	stemmer = PorterStemmer() 
# 	for na in name.split():
# 		# 去停用词
# 		if na not in stopwords.words('english'):
# 			# 词干提取
# 			nameli.append(stemmer.stem(na))
# 	name1 = " ".join(nameli)
# 	if name1 not in fu1["name1"]:
# 		fu1["name1"].append(name1)
# 		fu1["names"].append(a[0].strip())
# 		fu1["fucodes"].append(a[1])
# 	else:
# 		index = fu1["name1"].index(name1)
# 		fu1["names"][index] += ";" + a[0].strip()
# 		fu1["fucodes"][index] += ";" + a[1]
# for i in range(len(fu1["name1"])):
# 	sheet.write(i, 0, fu1["name1"][i])
# 	sheet.write(i, 1, fu1["names"][i])
# 	sheet.write(i, 2, fu1["fucodes"][i])
# workbook.close()

# 测试编辑距离算法
# def edit_distance(word1, word2):
#     len1 = len(word1);
#     len2 = len(word2);
#     dp = np.zeros((len1 + 1,len2 + 1))
#     for i in range(len1 + 1):
#         dp[i][0] = i;     
#     for j in range(len2 + 1):
#         dp[0][j] = j;
     
#     for i in range(1, len1 + 1):
#         for j in range(1, len2 + 1):
#             delta = 0 if word1[i-1] == word2[j-1] else 1
#             dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
#     return dp[len1][len2]/max(len1,len2)
# print(edit_distance( 'ZhejiangProvincialScienceFoundationforDistinguishedYoungScholars',"ZhejiangProvincialScienceFundforDistinguishedYoungScholars"))

# 统计词频
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(1).xlsx")
# table = data.sheet_by_index(0)
# stemmer = PorterStemmer() 
# string = ""
# for i in range(table.nrows):
# 	a = table.row_values(i)[0]
# 	string += " " + a
# strl_ist = string.lower().split(' ')
# count_dict = {}
# # 如果字典里有该单词则加1，否则添加入字典
# for str1 in strl_ist:
# 	str1 = stemmer.stem(str1)
# 	if str1 in count_dict.keys():
# 		count_dict[str1] = count_dict[str1] + 1
# 	else:
# 		count_dict[str1] = 1
# #按照词频从高到低排列
# count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
# print(count_list[:50])

#"Anhui","Beijing","Chongqing","Fujian","Gansu","Guangdong","Guangxi","Guizhou","Hainan","Hebei","Heilongjiang","Henan","Hong Kong","Hubei","Hunan","Jiangsu","Jiangxi","Jilin","Liaoning","Macau","Inner Mongol","Ningxia","Qinghai","Shandong","Shanxi","Shanxi","Shanghai","Sichuan","Taiwan","Tianjin","Tibet","Sinkiang","Yunnan","Zhejiang"
# 提取停用词词干
stemmer = PorterStemmer() 
print(stemmer.stem("application"))
# b = ["haerbing", "lanzhou", "kunming", "chengdu", "changchun", "shengyang", "xining", "xian", "zhengzhou", "jinan", "taiyuan", "hefei", "wuhan", "changsha", "nanjing", "guiyang", "nanning", "hangzhou", "nanchang", "guangzhou", "fuzhou", "taibei", "haikou", "yinchuan", "lasa", "chongqing"]
# for a in b:
# 	print('"' + stemmer.stem(a)+'"',end=',' )
# stopwords = ["Anhui","Beijing","Chongqing","Fujian","Gansu","Guangdong","Guangxi","Guizhou","Hainan","Hebei","Heilongjiang","Henan","Hong Kong","Hubei","Hunan","Jiangsu","Jiangxi","Jilin","Liaoning","Macau","Inner Mongol","Ningxia","Qinghai","Shandong","Shanxi","Shanxi","Shanghai","Sichuan","Taiwan","Tianjin","Tibet","Sinkiang","Yunnan","Zhejiang"]
# for a in stopwords:
# 	print(stemmer.stem(a), end=' ')

# 词形还原
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('Environmental', pos = "n"))
# a = ["sdf","sdfs"]
# a.remove("sdf")
# a.remove("sdfs")
# print(len(set(a)))
# while len(a)>0:
# 	if a[0] == "ss":
# 		del a[0]
# 		continue
# 	print(a[0])
# 	del a[0]
