 #!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import xlsxwriter
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np


# 2.1
# workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/处理后数据.xlsx")
# sheet = workbook.add_worksheet('处理后数据2（1）')
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（1）FU.xlsx")
# table = data.sheet_by_index(0)
# num = table.nrows
# sheetrow = 0
# print(num)
# for i in range(1, num):
# 	title = table.cell_value(i,0)
# 	print(title)
# 	fus = table.cell_value(i,1).split(";")
# 	fundOrder = 1
# 	for fu in fus:
# 		ful = fu.split("[")
# 		fundName = ful[0]
# 		if(fundName[0] == " "):
# 			fundName = fundName[1:]
# 		if(len(ful) > 1):
# 			fundCodes = fu[fu.index("[")+1:].split(", ")
# 			for fundCode in fundCodes:
# 				if(fundCode[-1] == "]"):
# 					fundCode = fundCode[:-1]
# 				print(fundCode)
# 				sheet.write(sheetrow,0,title)
# 				sheet.write(sheetrow,1,fundName)
# 				sheet.write(sheetrow,2,fundCode)
# 				sheet.write(sheetrow,3,fundOrder)
# 				fundOrder += 1
# 				sheetrow += 1
# 		else:
# 			sheet.write(sheetrow,0,title)
# 			sheet.write(sheetrow,1,fundName)
# 			sheet.write(sheetrow,3,fundOrder)
# 			fundOrder += 1
# 			sheetrow += 1
# workbook.close()

# 2.3
# 第一层清洗 去重
# workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(1).xlsx")
# sheet = workbook.add_worksheet('2（1）')
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（1）数据.xlsx")
# table = data.sheet_by_index(0)
# num = table.nrows
# fu1 = {}
# sheetrow = 0
# for i in range(num):
# 	a = table.row_values(i)
# 	name = a[0].strip()
# 	if name not in fu1.keys():
# 		fu1.update({name : a[1]})
# 		sheet.write(sheetrow,0,name)
# 		sheet.write(sheetrow,1,a[1])
# 		sheetrow += 1
# workbook.close()






# 第二层清洗 初步消去停用词后聚类
# data = xlrd.open_workbook(r"C:/Users/ljj/Desktop/2（3）FU(1).xlsx")
# table = data.sheet_by_index(0)
# workbook = xlsxwriter.Workbook("C:/Users/ljj/Desktop/2（3）FU(2)1.xlsx")
# sheet = workbook.add_worksheet('2（1）')
# lower = []
# fuName = []
# fuCode = []
# maintitle = []
# stemmer = PorterStemmer() 
# # 英语停用词
# # stopwords = stopwords.words('english')
# # 根据词频及实际情况构造停用词表
# # ,'heilongjiang','jilin','liaon','hebei','henan','shandong','jiangsu','shanxi','shaanxi','gansu','sichuan','qinghai','hunan','hubei','jiangxi','anhui','zhejiang','fujian','guangdong','guangxi','guizhou','yunnan','hainan','beij','tianjin','shanghai','chongq','hong kong','research','develop'
# stopwords = ['and','from','the','by','of','in','on','at','for','foundat','fund','grant','plan','a','an','project','program','programm','provinc','provinci','nation','key','special','specialis']
# sheetrow = 0
# for i in range(table.nrows):
# 	a = table.row_values(i)
# 	fucode1 = a[1]	
# 	if fucode1.strip() == "":
# 		fucode1 = "NAN"
# 	# 去除括号及小写化
# 	b = re.sub("\\(.*\\)", "", a[0].lower())
# 	# 去特殊符号
# 	b = b.replace("'s",'').replace("'"," ").replace('"',' ').replace('&',' ').replace('.',' ').replace(':',' ').replace('-',' ').replace('/',' ').replace(',',' ').replace('*',' ')
# 	nnb = []
# 	for nb in b.split():
# 		# 词干提取
# 		nb = stemmer.stem(nb)
# 		# 去停用词
# 		if nb not in stopwords:
# 			nnb.append(nb)
# 	c = " ".join(nnb)
# 	b = c.replace(' ', '')
# 	if b not in lower:
# 		maintitle.append(c)
# 		lower.append(b)
# 		fuName.append(a[0])
# 		fuCode.append(fucode1)	
# 	else:
# 		fuName[lower.index(b)] += ";" + a[0] 
# 		fuCode[lower.index(b)] += ";" + fucode1			
# for i in range(len(lower)):
# 	# 删除字符串小于2的数据
# 	len_list = [len(name.split()) for name in fuName[i].split(";")]
# 	print(fuName[i]+ ":" + str(max(len_list)))
# 	if max(len_list) > 1:
# 		sheet.write(sheetrow, 0,  maintitle[i])
# 		sheet.write(sheetrow, 1, fuName[i])
# 		sheet.write(sheetrow, 2, fuCode[i])
# 		sheetrow += 1
# workbook.close()

# 第二层清洗2 基金名称包含距离大于0.75 字编辑距离小于0.2 聚类
# def clearn2():
# 	data = xlrd.open_workbook(r"./2（3）FU(2)1.xlsx")
# 	table = data.sheet_by_index(0)
# 	workbook = xlsxwriter.Workbook("./2（3）FU(2)21.xlsx")
# 	sheet = workbook.add_worksheet('2（3）')
# 	fu1 = []
# 	for a in range(table.nrows):
# 		fu1.append(table.row_values(a))
# 	fu1.sort(key = key1, reverse = True)
# 	fu2 = np.transpose(fu1).tolist()
# 	stemNames = fu2[0]
# 	fuNames = fu2[1]
# 	fuCodes = fu2[2]
# 	fu = [["基金词干"],["基金名称"],["基金编码"]]
# 	row = 0
# 	while len(stemNames) > 0:
# 		fu[0].append(stemNames[0])
# 		fu[1].append(fuNames[0])
# 		fu[2].append(fuCodes[0])
# 		del stemNames[0]
# 		del fuNames[0]
# 		del fuCodes[0]		
# 		for o in range(len(stemNames)-1, -1, -1):
# 			fu0 = stemNames[o]
# 			stemsum = cont_funames(fu0, fu[0][row])
# 			# print(stemNames[0] +"  ： " + fu0 + "  ： " + str(stemsum))
# 			if stemsum > 0.75:
# 				fu[0][row] += ";" + fu0
# 				fu[1][row] += ";" + fuNames[o]
# 				fu[2][row] += ";" + fuCodes[o]			
# 				del stemNames[o]
# 				del fuNames[o]
# 				del fuCodes[o]			
# 		row += 1
# 	for i in range(len(fu[0])):
# 		sheet.write(i,0,fu[0][i])
# 		sheet.write(i,1,fu[1][i])
# 		sheet.write(i,2,fu[2][i])
# 	workbook.close()
# # 按基金词干长度倒序排列
# def key1(x):
# 	return len(x[0].split())
# # 求一个基金名称funames与另一组基金名称funames2的最大包含距离
# def cont_funames(funames, funames2):
# 	funames2list = list(set(eval(str([fun.split() for fun in funames2.split(";")]).replace("[","").replace("]",""))))
# 	# funameslist = funames.split(";")
# 	# mlengths = []
# 	province = ["anhui","beij","chongq","fujian","gansu","guangdong","guangxi","guizhou","hainan","hebei","heilongjiang","henan","hong","kong","hubei","hunan","jiangsu","jiangxi","jilin","liaon","macau","inner","mongol","ningxia","qinghai","shandong","shanxi","shanxi","shanghai","sichuan","taiwan","tianjin","tibet","sinkiang","yunnan","zhejiang"]
# 	# for fun in funameslist:
# 	funamesslist = funames.split()
# 	length = 0
# 	for funa in funamesslist:
# 		for n in range(len(funames2list)-1, -1, -1) :
# 			# 不同省份包含距离为0
# 			if (funa in province) and (funames2list[n] in province) and (funa != funames2list[n]):
# 				length = -1
# 				break
# 			if edit_distance(funa, funames2list[n]) < 0.2:
# 				length += 1
# 				del funames2list[n]
# 				break
# 		if length == -1:
# 			break
# 	mlength = length/len(funamesslist)
# 		# mlengths.append(mlength)
# 	return mlength
# # 求出两个单词的编辑距离相对较长单词的相对值
# def edit_distance(word1, word2):
#     len1 = len(word1)
#     len2 = len(word2)
#     if len1 > 2 and len2 > 2 and ((word1 in word2) or (word2 in word1)):
#     	dis = 0   	
#     else:
# 	    dp = np.zeros((len1 + 1,len2 + 1))
# 	    for i in range(len1 + 1):
# 	        dp[i][0] = i     
# 	    for j in range(len2 + 1):
# 	        dp[0][j] = j  
# 	    for i in range(1, len1 + 1):
# 	        for j in range(1, len2 + 1):
# 	            delta = 0 if word1[i-1] == word2[j-1] else 1
# 	            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
# 	    dis = dp[len1][len2]/max(len1,len2)
#     return dis
# clearn2()

# 测试
# fu1 = "100 talent academi scienc"
# fu2 = "100 talent academi scienc natur scienc"
# print(cont_funames(fu1, fu2))
# fu1 = {"lower" : ["sdfsgd"], "基金名称" : ["serwer"], "基金编码" : ["gretre"]}
# df = pd.DataFrame(data=fu1)
# fu1_insert = pd.DataFrame({"lower" : ["sdf"], "基金名称" :["sdfsg"], "基金编码" : ["wserfew"]}, index = [0])
# df = df.append(fu1_insert, ignore_index = True)
# print(df.loc[0])
# df.loc[df["lower"] == "sd", "基金名称"] = df.loc[df["lower"] == "sd", "基金名称"].values[0]+",sdfgd"
# print(df.loc[df["lower"] == "sd", "基金名称"])
# ra = re.findall('sf',"SFsfZG",re.IGNORECASE)
# print(ra)
# a = 'ADFWRD sd and AD sdf & . , sd ) , ge SDF ("AND andgegrthe the  and '
# b = a.lower().replace('and','').replace('"','').replace('&','').replace(' ','').replace('(','').replace(')','').replace(',','').replace('.','')
# c = a.replace(' and ','').replace('And','').replace('AND','').replace(' the ','').replace('The','').replace('THE','').replace('"','').replace('&','').replace(' ','').replace('(','').replace(')','').replace(',','').replace('.','').replace('-','').replace("'","").replace('/','').lower()
# print(b)
# print(c)
# a = ["12 4s d","3 d43","3 45","4s67 8","5s d67 8"]
# e = [" e", "e ", "e ", "a ", "a ","a "]
# b = ["45","5s 8"]
# for ba in b:
# 	c = ba.split()
# 	lowe = ""
# 	m = 1
# 	for low in a:
# 		lowe = low
# 		lowl = low.split()
# 		if set(c) <= set(lowl):
# 			m = 0
# 			break
# 	l = a.index(lowe)
# 	e[l] += ba
# print(e)
# 删除无用数据
# workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(2.2)2.xlsx")
# sheet1 = workbook.add_worksheet('valid')
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(2).xlsx")
# table = data.sheet_by_index(0)
# num = table.nrows
# sheetrow1 = 0
# for i in range(num):
# 	a = table.row_values(i)
# 	name = a[3]
# 	nuname = len(name.split())
# 	if nuname > 1:
# 		sheet1.write(sheetrow1,3,name)
# 		sheet1.write(sheetrow1,1,a[1])
# 		sheet1.write(sheetrow1,0,a[0])
# 		sheet1.write(sheetrow1,2,a[2])
# 		sheet1.write(sheetrow1,4,a[4])
# 		sheetrow1 += 1
# workbook.close()

#  第三层清洗1，对编码列表中第一个编码操作
# workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(3)1.xlsx")
# sheet = workbook.add_worksheet('2（3）')
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(2.2).xlsx")
# table = data.sheet_by_index(0)
# fuCodes = table.col_values(2)
# fuName = table.col_values(1)
# fu = []
# sheetrow = 0
# for i in range(table.nrows):
# 	fuCodei = fuCodes[i].replace(" ","")
# 	fu.append([fuCodei, fuName[i]])
# while len(fu) > 0:
# 	code = ''
# 	fusub = fu[0][0].split(";",1)
# 	for character in fusub[0]:
# 		if character.isdigit():
# 			code = code + '\\d'
# 		elif '\u4e00' <= character <= '\u9fff':
# 			code = code + character
# 		elif character in ["[","(",")","-"] :
# 			code = code + "[" + character + "]"
# 		elif character == "\\":
# 			code = code + "\\\\"
# 		elif character in ["*","+","?"] :
# 			code = code + "\\" + character
# 		# elif character.isalpha():
# 		# 	code = code + '\\D'	
# 		else:
# 			code = code + character
# 	print(fusub[0])
# 	print(code)
# 	sheet.write(sheetrow, 0, fu[0][0])
# 	sheet.write(sheetrow, 2, code)
# 	fundCodes = ""
# 	fundNames = ""
# 	pattern = re.compile(code, re.I)
# 	for h in range(len(fu)-1, -1, -1) :
# 		m = re.match(pattern, fu[h][0])
# 		if m:
# 			fundCodes += ";" + fu[h][0]
# 			fundNames += ";" + fu[h][1]
# 			del fu[h]
# 	sheet.write(sheetrow, 3, fundCodes[1:])
# 	sheet.write(sheetrow, 1, fundNames[1:])
# 	sheetrow += 1
# workbook.close()


#  第三层清洗 2修正1，对编码列表操作
# def clearn3():
# 	workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(3)1.xlsx")
# 	sheet = workbook.add_worksheet('2（3）')
# 	data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(2).xlsx")
# 	table = data.sheet_by_index(0)
# 	fuCodes = table.col_values(2)
# 	fuNames = table.col_values(1)
# 	stemNames = table.col_values(0)
# 	fu = [[],[],[]]
# 	fui = 0
# 	while len(fuNames) > 0:
# 		fu[0].append(stemNames[0])
# 		fu[1].append(fuCodes[0])
# 		fu[2].append(fuNames[0])
# 		# 去除基金编码中的空格，并考虑基金编码组合用分号分开
# 		fusubs = list(set(fuCodes[0].replace(" ", "").split(";")))
# 		if "NAN" in fusubs:
# 			fusubs.remove("NAN")
# 		for fusub in fusubs:
# 			code = ''
# 			print(fusubs)
# 			# 构造正则表达式
# 			for character in fusub:
# 				if character.isdigit():
# 					code = code + '\\d'
# 				elif '\u4e00' <= character <= '\u9fff':
# 					code = code + character
# 				elif character in ["[","(",")","-"] :
# 					code = code + "[" + character + "]"
# 				elif character == "\\":
# 					code = code + "\\\\"
# 				elif character in ["*","+","?"] :
# 					code = code + "\\" + character
# 				# elif character.isalpha():
# 				# 	code = code + '\\D'	
# 				else:
# 					code = code + character
# 			pattern = re.compile(code, re.I)
# 			for h in range(len(fuCodes)-1, 0, -1) :
# 				fuCodea = fuCodes[h]
# 				m = re.match(pattern, fuCodea.replace(" ", ""))

# 				if m:
# 					if cont_funames(fuNames[h], fuNames[0]) > 0.5:
# 						fu[0][fui] += ";" + stemNames[h]
# 						fu[1][fui] += ";" + fuCodea
# 						fu[2][fui] += ";" + fuNames[h]
# 						apsubs = fuCodea.replace(" ", "").split(";")
# 						fusubs.extend(apsubs)
# 						fusubs = list(set(fusubs))
# 						del fuNames[h]
# 						del fuCodes[h]
# 						del stemNames[h]
# 			del fuNames[0]
# 		del fuCodes[0]
# 		del stemNames[0]
# 		fui += 1
# 	lengfu = len(fu[0])
# 	for sheetrow in range(lengfu):
# 		sheet.write(sheetrow, 0, fu[0][sheetrow])
# 		sheet.write(sheetrow, 1, fu[1][sheetrow])
# 		sheet.write(sheetrow, 2, fu[2][sheetrow])	
# 	workbook.close()
# # 求一个基金名称与一组基金名称的最小包含距离
# def cont_funames(funames, funames2):
# 	funames2list = list(set(eval(str([fun.split() for fun in funames2.split(";")]).replace("[","").replace("]",""))))
# 	funameslist = funames.split(";")
# 	mlengths = []
# 	for fun in funameslist:
# 		funamesslist = fun.split()
# 		length = 0
# 		for funa in funamesslist:
# 			if funa in funames2list:
# 				length += 1
# 		mlength = length/len(funamesslist)
# 		mlengths.append(mlength)
# 	return max(mlengths)
# clearn3()


# 第三层清洗 3 找出聚类中心
# 求出两个基金名的编辑距离
# def edit_distance(funame1, funame2):
#     len1 = len(funame1);
#     len2 = len(funame2);
#     dp = np.zeros((len1 + 1,len2 + 1))
#     for i in range(len1 + 1):
#         dp[i][0] = i;     
#     for j in range(len2 + 1):
#         dp[0][j] = j;
     
#     for i in range(1, len1 + 1):
#         for j in range(1, len2 + 1):
#             delta = 0 if funame1[i-1] == funame2[j-1] else 1
#             dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
#     return dp[len1][len2]
# # 求一个基金名相对于本组基金名的编辑距离之和
# def min_dis_funame(funames):
# 	sum_distance = []
# 	for funame in funames:
# 		funamedis = 0
# 		for funame2 in funames:
# 			funamedis += edit_distance(funame,funame2)
# 		sum_distance.append(funamedis)
# 	return funames[sum_distance.index(min(sum_distance))]
# def writef():
# 	workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(3).xlsx")
# 	sheet = workbook.add_worksheet('2（3）')
# 	data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(2).xlsx")
# 	table = data.sheet_by_index(0)
	







# 测试
# a = ["sd_f=123sd23", "[2015]2218", "sv_d=125sh3434","UK-CIAPP\\73", "sv_d=(123)sh35", "sv_d=(125)sh35","[2015]2118", "324534tg", "324534th"]
# while len(a) > 0:
# 	c = ''
# 	for i in a[0]:
# 		if i.isdigit():
# 			c = c + '\\d'
# 		elif i.isalpha():
# 			c = c + '\\D'
# 		elif i in ["[","(",")","-"] :
# 			c = c + "[" + i + "]"
# 		elif i == "\\":
# 			c = c + "\\\\"
# 		else:
# 			c = c + i
# 	print("c:" + c)
# 	pattern = re.compile(c)
# 	for h in range(len(a)-1, -1, -1) :
# 		m = re.match(pattern, a[h])
# 		if m:
# 			print(a[h])
# 			del a[h]
# print(a)
# a = "sdfwef(34dffgv)dgv"
# b = re.sub("\\(.*\\)","",a)
# print(b)
# a = "s(dfdgs ),f(sdfs ),wesdg"
# b = re.sub("s ", "", a)
# print(b)
# a = "s(dfdgss1213 ),f(sd45fs ),w3esdg"
# b = re.sub("\\d*", "", a)
# print(b)
# funames2 = "adf sdfg sd ; asdf sdf sd"
# funames2list = list(set(eval(str([fun.split() for fun in funames2.split(";")]).replace("[","").replace("]",""))))
# print(funames2list)

# 分区辅件
# workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(3.1).xlsx")
# sheet1 = workbook.add_worksheet('multiple')
# sheet2 = workbook.add_worksheet('single')
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(3).xlsx")
# table = data.sheet_by_index(0)
# fuCodes = table.col_values(1)
# fuName = table.col_values(0)
# sheetrow1 = 0
# sheetrow2 = 0
# for i in range(table.nrows):
# 	fuCode = fuCodes[i]
# 	if ";" in fuCode:
# 		sheet1.write(sheetrow1, 0, fuName[i])
# 		sheet1.write(sheetrow1, 1, fuCode)
# 		sheetrow1 += 1
# 	else:
# 		sheet2.write(sheetrow2, 0, fuName[i])
# 		sheet2.write(sheetrow2, 1, fuCode)
# 		sheetrow2 += 1
# workbook.close()

# 第二层清洗  dangerous已丢弃
# data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(1).xlsx")
# table = data.sheet_by_index(0)
# workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(2)1.xlsx")
# sheet = workbook.add_worksheet('2（1）')
# lower = []
# fuName = []
# fuCode = []
# sheetrow = 0
# for i in range(table.nrows):
# 	a = table.row_values(i)
# 	fucode1 = a[1]	
# 	if fucode1.strip() == "":
# 		fucode1 = "NAN"
# 	b = re.sub("\\(.*\\)", "", a[0].lower())
# 	b = b.replace('and ','').replace('from ','').replace('the ','').replace('by ','').replace('of ','').replace('for ','').replace('in ','').replace('china','').replace('chinese','').replace('fundation','').replace('funds','').replace('fund','').replace('grants','').replace('grant','').replace('projects','').replace('project','').replace('programs','').replace('program','').replace('provinces','').replace('province','').replace("'s",'').replace('"','').replace('&','').replace('.','').replace('-','').replace('  ',' ').replace("'","").replace('/','').strip()
# 	c = b.split()
# 	m = 1
# 	lowe = ""
# 	for low in lower:
# 		lowe = low
# 		lowl = low.split()
# 		if set(c) <= set(lowl):
# 			m = 0
# 			break
# 	if m == 0:
# 		fuName[lower.index(lowe)] += ";" + a[0] 
# 		fuCode[lower.index(lowe)] += ";" + fucode1	 
# 	else:	
# 		lower.append(b)
# 		fuName.append(a[0])
# 		fuCode.append(fucode1)	
# for i in range(len(lower)):
# 	sheet.write(sheetrow, 0, lower[i])
# 	sheet.write(sheetrow, 1, fuName[i])
# 	sheet.write(sheetrow, 2, fuCode[i])
# 	sheetrow += 1
# workbook.close()

# 第四层清洗
# def forth():
# 	workbook = xlsxwriter.Workbook("D:/数据挖掘/任务/2（3）FU/2（3）FU(4.1).xlsx")
# 	sheet = workbook.add_worksheet('2（3）')
# 	data = xlrd.open_workbook(r"D:/数据挖掘/任务/2（3）FU/2（3）FU(4).xlsx")
# 	table = data.sheet_by_index(0)
# 	fuCodes = table.col_values(1)
# 	fuNames = table.col_values(0)
# 	maintitles = table.col_values(2)
# 	fu = [[],[],[],[]]
# 	fui = 0
# 	for i in range(len(fuNames)):
# 		fuName = fuNames[i]
# 		fuCode = fuCodes[i]
# 		maintitle = maintitles[i] 
# 		fuName1 = fuName.split(";")
# 		m = -1
# 		lowe = ""
# 		for fuName2 in fuName1:
# 			lower = splitfu(fuName2)
# 			for low in fu[0]:
# 				lowe = low
# 				if set(lower) <= set(low):
# 					m = 0
# 					break
# 				if set(lower) >= set(low):
# 					m = 1
# 					break
# 			if m == 0 or m == 1:
# 				break		
# 		if m == 0:
# 			fu[1][fu[0].index(lowe)] += ";" + fuName
# 			fu[2][fu[0].index(lowe)] += ";" + fuCode
# 			if len(fu[3][fu[0].index(lowe)]) < len(maintitle):
# 				fu[3][fu[0].index(lowe)] = maintitle		  
# 		elif m == 1:
# 			fu[0][fu[0].index(lowe)] == lower
# 			fu[1][fu[0].index(lowe)] += ";" + fuName
# 			fu[2][fu[0].index(lowe)] += ";" + fuCode
# 			if len(fu[3][fu[0].index(lowe)]) < len(maintitle):
# 				fu[3][fu[0].index(lowe)] = maintitle
# 		else:	
# 			fu[0].append(splitfu(fuName))
# 			fu[1].append(fuName)
# 			fu[2].append(fuCode)
# 			fu[3].append(maintitle)
# 	for sheetrow in range(len(fu[0])):
# 		sheet.write(sheetrow, 1, fu[1][sheetrow])
# 		sheet.write(sheetrow, 2, fu[2][sheetrow])
# 		sheet.write(sheetrow, 3, fu[3][sheetrow])
# 	workbook.close()	

# def splitfu(fuName):
# 	b = re.sub("\\(.*\\)", "", fuName)
# 	b = b.replace('and ','').replace('from ','').replace('the ','').replace('by ','').replace('of ','').replace('at ','').replace('for ','').replace('in ','').replace("'","").replace("s ","").replace('china','').replace('chinese','').replace('fundation','').replace('fund','').replace('grant','').replace('project','').replace('program','').replace('province','').replace('"','').replace('&','').replace('.','').replace('-','').replace('  ',' ').replace('/','').replace(',','').replace('+','').replace(';','').strip()
# 	return list(set(b.split()))
# forth()


# 测试
# from nltk.corpus import wordnet 
# synonyms = []
# for syn in wordnet.synsets('Computer'):
#     for lemma in syn.lemmas():
#         synonyms.append(lemma.name())
# print(synonyms)

# 统计词频
workbook = xlsxwriter.Workbook("./词频.xlsx")
sheet = workbook.add_worksheet('2（3）')
data = xlrd.open_workbook(r"./对照表.xlsx")
table = data.sheet_by_index(0)
nowr = table.nrows
for a in range(nowr):
	names = table.cell_value(a,2).replace(";;",";").split(";")
	sheet.write(a,0,names[0])
	sheet.write(a,1,len(names))
workbook.close()