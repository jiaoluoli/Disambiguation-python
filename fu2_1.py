import xlrd
import xlsxwriter
import numpy as np
import heapq

# def clearn2():
# 	data = xlrd.open_workbook(r"./2（3）FU(2)111.xlsx")
# 	table = data.sheet_by_index(0)
# 	workbook = xlsxwriter.Workbook("./2（3）FU(2)113.xlsx")
# 	sheet = workbook.add_worksheet('2（3）')
# 	fu1 = []
# 	for a in range(table.nrows):
# 		fu1.append(table.row_values(a))
# 	fu1.sort(key = key1, reverse = True)
# 	# fu2 = np.transpose(fu1).tolist()
# 	# fu3 = [len(f2[0].split()) for f2 in fu2]
# 	le = len(fu1[0][0].split())
# 	fu3 = [[fu1[0]]]
# 	del fu1[0]
# 	fu3l = 0
# 	for f1 in fu1:
# 		if len(f1[0].split()) == le:
# 			fu3[fu3l].append(f1)
# 		else:
# 			le = len(f1[0].split())
# 			fu3.extend([[f1]])
# 			fu3l += 1
# 	# fu = [["基金词干"],["基金代表"],["基金名称"],["基金编码"],["长度"]]
# 	fu4 = []
# 	leng = len(fu3[0][0][0].split())
# 	province = set(["xinjiang","lanzhou","kunm","chengdu","changchun","shengyang","xian","zhengzhou","jinan","taiyuan","hefei","wuhan","changsha","nanj","guiyang","hangzhou","nanchang","guangzhou","fuzhou","taibei","haikou","yinchuan","lasa","chongq","suzhou","guilin","changchun","shenyang","shanghai","qingdao","shenzhen","anhui","beij","fujian","gansu","guangdong","guangxi","guizhou","hainan","hebei","heilongjiang","henan","hong","kong","hubei","hunan","jiangsu","jiangxi","jilin","liaon","macau","inner","mongol","ningxia","qinghai","shandong","shanxi","shanxi","sichuan","taiwan","tianjin","tibet","sinkiang","yunnan","zhejiang"])

# 	while len(fu3[0])>0:
# 		furow = fu3[0][0]
# 		fu4.extend([furow[:]])	
# 		deng_fun(fu4,fu3[0],leng,province,0.2)
# 		del fu3[0][0]
# 	del fu3[0]
# 	leng = len(fu3[0][0][0].split())	
# 	while leng > 4:
# 		while len(fu3[0])>0:
# 			furow = fu3[0][0]
# 			fu4.extend([furow[:]])						
# 			budeng_fun(fu4,province)
# 			del fu3[0][0]
# 		del fu3[0]
# 		if len(fu3)==0:
# 			break
# 		leng = len(fu3[0][0][0].split())
# 	for i in range(len(fu4)):
# 		sheet.write(i,0,fu4[i][0])
# 		sheet.write(i,1,fu4[i][1])
# 		sheet.write(i,2,fu4[i][2])
# 		sheet.write(i,3,fu4[i][3])
# 	workbook.close()
# # 按基金词干长度排列
# def key1(x):
# 	return len(x[0].split())
# # 两个等长字符串合并
# def deng_fun(fu4,furows,leng,province,p):
# 	set1 = set(furows[0][0].split())
# 	for o in range(len(furows)-1,0,-1):
# 		furow2 = furows[o]
# 		stem = furow2[0]
# 		set2 = set(stem.split())
# 		# 等长基金名的差异字符小于长度的0.2并且两者中包含相同城市名
# 		if (len(set1-set2)/leng < p) and (set1&province == province&set2):
# 			fu4[fu4.index(furows[0])][0] += ";;" + stem
# 			fu4[fu4.index(furows[0])][1] += ";;" + furow2[1]
# 			fu4[fu4.index(furows[0])][2] += ";;" + furow2[2]
# 			fu4[fu4.index(furows[0])][3] += ";;" + furow2[3]
# 			del furows[o]
# 		else:
# 			break
# def budeng_fun(furows,province):
# 	set1 = set(furows[-1][0].split(";;")[0].split())
# 	for o in range(len(furows)-2,-1,-1):		
# 		furow2 = furows[o]	
# 		stem = furow2[0]
# 		# 使每次只跟前一个比，减小误差
# 		set2 = set(stem.split(";;")[0].split())
# 		if (len(set1-set2) == 0) and (set1&province == province&set2):
# 			furows[-1][0] += ";;" + stem
# 			furows[-1][1] += ";;" + furow2[1]
# 			furows[-1][2] += ";;" + furow2[2]
# 			furows[-1][3] += ";;" + furow2[3]
# 			del furows[o]

# clearn2()

a = [1,3,4,5,10,3,4,5,6]
b = sorted(list(enumerate(a)),key=lambda x:x[1],reverse=True)
c = [x[1] for x in b][:5]
print(c)

# def cont_funames(funames, funames2):
# 	funames2list = list(set(eval(str([fun.split() for fun in funames2.split(";")]).replace("[","").replace("]",""))))
# 	funameslist = funames.split(";")
# 	mlengths = []
# 	province = ["anhui","beij","chongq","fujian","gansu","guangdong","guangxi","guizhou","hainan","hebei","heilongjiang","henan","hong","kong","hubei","hunan","jiangsu","jiangxi","jilin","liaon","macau","inner","mongol","ningxia","qinghai","shandong","shanxi","shanxi","shanghai","sichuan","taiwan","tianjin","tibet","sinkiang","yunnan","zhejiang"]

# 	for fun in funameslist:
# 		funamesslist = fun.split()
# 		length = 0
# 		fun1set = set(funamesslist)
# 		provinceset = set(province)
# 		fun2set = set(funames2list)
# 		#如果funames里有省份，并且funames2中也有，但funames2中没有funames中有的，则funames不在funames2中
# 		if len(fun1set&provinceset)>0 and len(provinceset&fun2set)>0 and len(fun1set-fun2set)>0:
# 			length = -1
# 			break
# 		for funa in funamesslist:
# 			if funa in funames2list:
# 				length += 1
# 		mlength = length/len(funamesslist)
# 		mlengths.append(mlength)
# 	if length == -1:
# 		mlengths.append(-1)
# 	return max(mlengths)
# print(cont_funames("shanghai scienc technolog commiss shanghai municip", "guangzhou scientif technolog"))
