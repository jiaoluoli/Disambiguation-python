#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import math
import csv
import re
import os 

# junjieLi 
# 2019.05.16


stopwords1 = ["[","]",""]

def nIsNotNan(arg):
    try:
        if math.isnan(arg):
            return False
        else:
            return True
    except:
        return True

def splitFu(dealFile):
	f = open(dealFile)
	data = pd.read_csv(f,header=None)
	dataTable = pd.DataFrame(data)
	dataTable = dataTable.dropna(axis=0, how='all')
	
	rows = dataTable.shape[0]
	sheetrow = 0
	
	funds = []
	for i in range(0,rows):
		ut = dataTable.iloc[i,1]
		if nIsNotNan(ut):
			fud = dataTable.iloc[i,0]
			fud = fud.replace("|||"," ")
			fus = fud.split(";")

			fundOrder = 1
			
			for j in range(0,len(fus)):
				fu = fus[j].strip()
				if fu in stopwords1:
					continue
				ful = fu.split("[")
				fundName = ful[0].strip()
				if fundName == "":
					continue
				if len(ful) > 1 :
					fundCodes = fu[fu.index("[")+1:].split(",")	
					newf = 	dfundCode(ut,fundName,fundCodes,fundOrder)
					if len(newf) != 0 : 
						funds.extend(newf)
						fundOrder = funds[-1][-1]+1
				else :
					try:
						#当基金和基金编码备用分好隔开时
						nextfu = fus[j+1].strip()
						if nextfu[0] == "[":							
							fundCodes = nextfu[nextfu.index("[")+1:].split(",")
							newf = dfundCode(ut,fundName,fundCodes,fundOrder)
							if len(newf) != 0 : 	
								funds.extend(newf)
								fundOrder = funds[-1][-1]+1
						else:
							funds.append([ut,fundName,"NAN",fundOrder])
							fundOrder += 1
					except IndexError:
						funds.append([ut,fundName,"NAN",fundOrder])
						fundOrder += 1
						
	# with open(storeFile,'a',encoding='utf-8-sig',newline='') as csvf:
	# 	csvw = csv.writer(csvf)
	# 	csvw.writerows(funds)
	return funds


def dfundCode(ut,fundName,fundCodes,fundOrder):
	funds = []
	for fundCode in fundCodes:
		fundCode = fundCode.strip()

		if fundCode in stopwords1:
			continue
		# 最后一个编码
		if(fundCode[-1] == "]"):
			fundCode = fundCode[:-1]
		# 基金名后附带中括号
		if("] [" in fundCode):
			fundName = fundName + "[" + fundCode[:fundCode.index("] [")+1].strip()
			fundCode = fundCode[fundCode.index("] [")+3:]
		# 中括号内为时间或其他表意字符而非编码
		if not checkCodeForm(fundCode):
			fundName = fundName + "["+ fundCode + "]"
			fundCode = "NAN"

		funds.append([ut,fundName,protectCode(fundCode),fundOrder])
		fundOrder += 1
	return funds

#检查是否是code还是基金名的一部分
def checkCodeForm(code):
	code = code.replace(".","")
	dataForm = ['[1,2]\d{3}-\d{1,2}$','[1,2]?\d{1,3}$']
	isCode = True
	for form in dataForm:
		matchObj = re.match(form, code)
		if matchObj:
			isCode = False
	return isCode

#将excel会泽东转换为时间和求值的数据加单引号保留初始格式
def protectCode(code):
	dataForm = ['\d{1,2}-\d{1,2}(-\d{1,2})?$','(-\d+)+$','0+(\d)*$']
	for form in dataForm:
		matchObj = re.match(form, code)
		if matchObj:
			code = "'"+code
			break
	return code  	




# if __name__ == "__main__":
# 	# dealFile = 'correctFiles.csv'
# 	# storeFile = 'FuDealtc.csv'
# 	# splitFu(dealFile, storeFile)
# 	filenames = os.listdir('./Fu')
# 	fucsvList = [ filename for filename in filenames if filename.endswith(".csv") ]
# 	faultFile = []
# 	for fucsv in fucsvList:
# 		dealFile = './Fu/' + fucsv
# 		storeFile = './FuDealt/' + fucsv
		
# 		if not os.path.exists('./FuDealt'):
# 			os.makedirs('./FuDealt')

# 		try:
# 			splitFu(dealFile, storeFile)
# 		except:
# 			faultFile.append(fucsv)		
# 	with open('./fauleFile.csv','a',encoding='utf-8-sig',newline='') as csvf:
# 		print(faultFile)
# 		csvw = csv.writer(csvf)
# 		csvw.writerow(faultFile)			

 

