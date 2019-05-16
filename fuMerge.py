import requests
import time
import random
import hashlib
import pandas as pd
import math
import csv
import re
import multiprocessing
import urllib.request
import urllib.parse
import json
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import fuSplit
import os

# junjieLi 
# 2019.05.16

# dFundNames = []
stopwords = ['and','from','the','by','of','in','on','at','for','foundat','fund','grant','plan','a','an','project','program','programm','public','provinc','provinci','nation','key','special','specialis','depart']
stemmer = PorterStemmer()

def onlyFu(funds,storeFile):

	# 制造无重复数列
	data = pd.DataFrame(funds) 
	data = data.dropna(axis=0, how='all')
	data = data.fillna("'NULL")
	dataList = data[1].values
	dataList = dataList.tolist()
	# 基金名去重
	fundNames = list(set(dataList))
	# 将基金名按长度由长到短排列
	fundNames.sort(key = lambda i:len(i), reverse = True)

	pubFunds = wordSet(fundNames)
	pubFunds.reverse()

	data[4] = data[1].apply(match, args = (fundNames, pubFunds))
	print(storeFile)
	with open(storeFile,'w',encoding='utf-8-sig',newline='') as csvf:
		csvw = csv.writer(csvf)
		csvw.writerows(data.values)
	

	# 后续若要对基金名进一步操作时用
	# dpubFunds = list(set(pubFunds))
	# dpubFunds.sort(key=pubFunds.index)
	# dpubFunds = np.transpose([dpubFunds]).tolist()
	# with open(storeFile2,'a',encoding='utf-8',newline='') as csvf:
	# 	csvw = csv.writer(csvf)
	# 	csvw.writerows(dpubFunds)



# 处理j单个基金名中特殊符号及字符
def reFund(fundName):


	# 删除小括号、中括号及其内部内容
	remove = ["\(.*\)","\[.*\]"]
	for remo in remove:
		fundName1 = re.sub(remo," ",fundName)
		if fundName1 != fundName:
			break
	if len(fundName1.split()) > 3:
		fundName = fundName1


	RD = ["R & D ", " RD ", " R D ","R&D "]
	for rd in RD:
		fundName = fundName.replace(rd," Research and Development ")	

	fundName = fundName.replace("&"," and ")

	fundName = re.sub("P(\.)?R(\.)? "," P.R.", fundName)

	stopwords = ["-",":",'"',"''", "<SUP>", "</SUP>","  "]
	for sto in stopwords:
		fundName = fundName.replace(sto, " ")
	# 排除's 和s' 情况，删除''
	searchObj = re.search( "'([^s (\W)].*)'", fundName)

	if searchObj:
		fundName = fundName.replace(searchObj.group(),searchObj.group().strip("'"))

	return fundName.strip()


# 将基金名切割成单词对比基金名的相近程度
def wordSet(fundNames):

	nnbT = []
	newDpubFunds = []
	for dpu in fundNames: 
		nnb1 = []
		dpu = reFund(dpu)
		for nb in dpu.split():
			# 词干提取
			nb = stemmer.stem(nb)
			# 去停用词
			if nb not in stopwords:
				nnb1.append(nb)			
		nnb2 = set(nnb1)
		lnnb2 = len(nnb2)
		# 对不同长度基金词干采取不同相似度计算标准
		if lnnb2 == 0 :
			newDpubFunds.insert(0,dpu)
			nnbT.insert(0,"NAN")
			continue
		elif lnnb2 > 0 and lnnb2 < 4:
			issub = False
			for nnb in nnbT:			
				if len(nnb)-lnnb2 > 2:
					break
				if nnb == "NAN":
					continue
				if nnb2.issubset(nnb):
					b =nnbT.index(nnb)
					newDpubFunds.insert(0, newDpubFunds[b])
					issub = True
					break
			if not issub:
				newDpubFunds.insert(0,dpu)
		elif lnnb2 > 3 and lnnb2 < 8:
			nnb = difSet(nnbT,nnb2,0.3)
			if nnb != "NAN":
				newDpubFunds.insert(0,newDpubFunds[nnbT.index(nnb)])
			else:
				newDpubFunds.insert(0,dpu)
		elif lnnb2 > 7 and lnnb2 < 11:
			nnb = difSet(nnbT,nnb2,0.26)
			if nnb != "NAN":
				newDpubFunds.insert(0,newDpubFunds[nnbT.index(nnb)])
			else:
				newDpubFunds.insert(0,dpu)
		elif lnnb2 > 10:
			nnb = difSet(nnbT,nnb2,0.2)
			if nnb != "NAN":
				newDpubFunds.insert(0,newDpubFunds[nnbT.index(nnb)])
			else:
				newDpubFunds.insert(0,dpu)
		nnbT.insert(0,nnb2)		
	return newDpubFunds

# 对比nnb2和nnbT中所有nnb的包换关系，nnbT为按单词数由少到多排序
def difSet(nnbT,nnb2,rate):	
	lnnb2 = len(nnb2)
	numb2 = re.findall( "\d+", " ".join(nnb2))

	for nnb in nnbT:
		lnnb = len(nnb)
		# 如果 nnb为NAN 或和 nnb2的长度相差超过两个则跳出循环
		if abs(lnnb-lnnb2) > 3:
			break		
		if nnb == "NAN":
			continue
		# 如果两个基金名内数字不一样，则区分为两个基金
		if numb2:
			numb = re.findall( "\d+", " ".join(nnb))
			if numb2 != numb:
				continue

		if max(len(nnb.difference(nnb2)),len(nnb2.difference(nnb)))/min(lnnb,lnnb2)<rate :

			return nnb
	return "NAN" 

def match(data,fundNames,pubFunds):
	return pubFunds[fundNames.index(data)]


# 翻译
# def translation(sentence):
# 	#输入单词
#     keyword = sentence
 
#     #生成salt的值
#     r = str(int(time.time()*1000))
#     salt = r + str(int(random.random()*10))
 
#     #生成sign
#     value = "fanyideskweb" + keyword + salt + "@6f#X3=cCuncYssPsuRUE"
#     md5_str = getMd5(value)
 
#     #生成header
#     headers = {
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
#         'Connection': 'keep-alive',
#         'Content-Length': str(233+len(keyword)),
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'Cookie': 'OUTFOX_SEARCH_USER_ID=-1475131016@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=6241167.578427844; _ga=GA1.2.1519057173.1535511777; JSESSIONID=aaamFTGK4qLCf4uKcrxPw; ___rl__test__cookies=1556242390777',
#         'Host': 'fanyi.youdao.com',
#         'Origin': 'http://fanyi.youdao.com',
#         'Referer': 'http://fanyi.youdao.com/',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#         'X-Requested-With': 'XMLHttpRequest'
#     }
 
#     #生成表单数据
#     data_dic = {
#         'i': keyword,
#         'from': 'en',
#         'to': 'zh',
#         'smartresult': 'dict',
#         'client': 'fanyideskweb',
#         'salt': salt,
#         'sign': md5_str,
#         'ts': r,
#         'bv': 'ae62d2e2541901f6ebf99ec18e429e3f',
#         'doctype': 'json',
#         'version': '2.1',
#         'keyfrom': 'fanyi.web',
#         'action': 'FY_BY_REALTlME'
#     }
 
#     #接口地址
#     url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#     #发起网络请求
#     response = requests.post(url=url,data=data_dic,headers=headers)
#     data = response.json()
#     return data['translateResult'][0][0]['tgt']


# def getMd5(value):   
#     md5 = hashlib.md5()
#     md5.update(bytes(value, encoding='Utf-8'))
#     md5_str = md5.hexdigest()
#     return md5_str

if __name__ == "__main__":
	# dealFile = './FuDealt/Fu_8.csv'
	# storeFile1 = './StoreFile/PubFu_8.csv'
	# storeFile2 = 'FuMtest2.csv'
	# onlyFu(dealFile,storeFile1,storeFile2)
	filenames = os.listdir('./Fu')
	fucsvList = [ filename for filename in filenames if filename.endswith(".csv") ]
	faultFile = []
	# 根据需要更改设置进程池中进程个数
	pool = multiprocessing.Pool(processes = 6)
	for fucsv in fucsvList:
		dealFile = './Fu/' + fucsv
		storeFile = './FuDealt/deal' + fucsv		
		if not os.path.exists('./FuDealt'):
			os.makedirs('./FuDealt')

		try:
			funds = fuSplit.splitFu(dealFile)
			pool.apply_async(onlyFu, [funds,storeFile])
		except:
			faultFile.append(fucsv)
	pool.close()
	pool.join()
	with open('./fauleFile.csv','w',encoding='utf-8-sig',newline='') as csvf:
		print(faultFile)
		csvw = csv.writer(csvf)
		csvw.writerow(faultFile)


	# pool = multiprocessing.Pool(processes = 7)
	# for i in range(0,42):
	# 	dealFile = './FuDealt/Fu_'+str(i)+'.csv'
	# 	storeFile1 = './StoreFile/PubFu_'+str(i)+'.csv'
	# 	storeFile2 = './StoreFile/OnlFu_'+str(i)+'.csv'
	# 	pool.apply_async(onlyFu, [dealFile,storeFile1,storeFile2])
	# pool.close()
	# pool.join()