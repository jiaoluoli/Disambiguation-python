import pandas as pd
import re
import csv
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import urllib.request
import urllib.parse
import json

# dataFrame格式
	# dFundNames = pd.DataFrame({'rowFunds':[],'pubFunds':[]})
	# f = open(dealFile)
	# data = pd.read_csv(f,header=None)
	# dataTable = pd.DataFrame(data)	
	# rows = dataTable.shape[0]
	# for i in range(0,rows):
	# 	fundName = dataTable.iloc[i,1]
	# 	if fundName not in dFundNames['rowFunds'].values:

	# 		dFundNames = pd.concat([pd.DataFrame({'rowFunds':[fundName],'pubFunds':[reFund(fundName)]}), dFundNames],ignore_index=True)	
	# 		# dFundNames.append(fundName)
	# print(dealFile)


# data = pd.read_csv(open("test1.csv"),header=None)

# list1 = data[1].values
# list1 = list1.tolist()
# print(list1)

# 测试正则表达式
# code = "0003"
# code = code.replace(".","")
# dataForm = ['(\d{1,2})?-\d{1,2}(-\d{1,2})?$','(-\d+)+$','0+(\d)*$']
# isCode = True
# for form in dataForm:
# 	matchObj = re.match(form, code)
# 	if matchObj:
# 		print(form)
# 		isCode = False
# print(isCode)

# fundName = "sdfg{sdfg}[sdfg](sdg)' 'wees' PR. "
# remove = ["\(.*\)","\[.*\]"]
# for remo in remove:
# 	fundName = re.sub(remo,"",fundName)
# fundName = re.sub(" P(\.)?R(\.)? "," P.R.", fundName)
# searchObj = re.search( "'([^s ].*)'", fundName)
# if searchObj:
# 	fundName = re.sub(searchObj.group(),searchObj.group(1),fundName)
# print(fundName)

# =_xlfn.FILTERXML(_xlfn.WEBSERVICE("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=xml&version=1.1&q="&F3&""),"//paragraph")

# dpubFunds = ["sdf","sdg","sdg"]
# d = ["sdgf","sgfre","srgewr"]
# dpubFunds = np.transpose([dpubFunds,d]).tolist()
# print(dpubFunds)

# 提取词干和去停用词
# a = "China's National Tenth Five Year Scientific and Technological Key Programme"
# stopwords = ['and','from','the','by','of','in','on','at','for','foundat','fund','grant','plan','a','an','project','program','programm','public','provinc','provinci','nation','key','special','specialis','depart']
# stemmer = PorterStemmer() 
# nnb = ""
# for nb in a.split():
# 	# 词干提取
# 	nb = stemmer.stem(nb)
# 	# 去停用词
# 	if nb not in stopwords:
# 		nnb += " " + nb 
# print(nnb)



#有道翻译一

# content = ". ".join(["China's National Tenth Five Year Scientific and Technological Key Programme","Western Light Projects of China"])
# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
# data = {}
# data['type'] = 'AUTO'
# data['i'] = content
# data['doctype'] = 'json'
# data['keyfrom'] = 'neverland'
# data['ue'] = 'UTF-8'
# data['action'] = 'FY_BY_CLICKBUTTON'
# data['key'] = '969918857'
# data['typoResult'] = 'true'

# data = urllib.parse.urlencode(data).encode('utf-8')
# response = urllib.request.urlopen(url, data)
# html = response.read().decode('utf-8')
# target = json.loads(html)
# print('翻译的结果：%s' % target['translateResult'][0][0]['tgt'])

# 测试按长度排序
# def test():
# 	fundNames = ["sgg","wetfewtf","we"]
# 	fundNames.sort(key = lambda i:len(i), reverse = False)
# 	print(fundNames)
# def key1(x):
# 	return len(x)
# test()

#测试数列转置
# fundNames = ["123",'123','123']
# pubFunds = ['34','34','34']
# mixFund = np.transpose([fundNames,pubFunds]).tolist()
# print(mixFund)

# 存docx
# doc = docx.Document()
# for dpu in dpubFunds:
# 	doc.add_paragraph(dpu)
# doc.save(storeFile2)

#有道翻译二

# import requests
# import time
# import random
# import hashlib
# # 生成md5字符串
# def getMd5(value):
    
#     md5 = hashlib.md5()
#     md5.update(bytes(value, encoding='Utf-8'))
#     md5_str = md5.hexdigest()
#     return md5_str
 
# if __name__ == '__main__':
#     #输入单词
#     keyword = "National Science and Technology Major Project Key New Drug Creation and Manufacturing Program, China. Chinese Ministry of Health"
 
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
#     print(data['translateResult'][0][0]['tgt'])


# 测试文件夹
# filenames = listdir('./test')
# fucsvList = [ filename for filename in filenames if filename.endswith(".csv") ]
# for fucsv in fucsvList:
# 	dealFile = './test/' + fucsv
# 	storeFile = './testDealt/' + fucsv
# 	faultFile = './fauleFile.csv'
# 	if not os.path.exists('./testDealt'):
# 		os.makedirs('./testDealt')

# 	try:
# 		splitFu(dealFile, storeFile)
# 	except:
# 		with open(faultFile,'a',encoding='utf-8',newline='') as csvf:
# 			csvw = csv.writer(csvf)
# 			csvw.writerow(fucsv)


a = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]  
df = pd.DataFrame(a) 
print(df)