import xlrd
import xlsxwriter
import numpy as np
import urllib.request
import urllib.parse
import json
# 求最小编辑标题
def title():
	workbook = xlsxwriter.Workbook("./成型表.xlsx")
	sheet = workbook.add_worksheet('2（1）')
	data = xlrd.open_workbook(r"./对照表.xlsx")
	table = data.sheet_by_index(0)
	sheetrow = 0
	for i in range(table.nrows):
		# title为fu[0]中编辑距离最小的
		funames = table.row_values(i)[2].replace(";;",";").split(";")
		titlen = min_dis(funames)
		for funame in funames:
			sheet.write(sheetrow,0,titlen)
			sheet.write(sheetrow,1,funame)
			sheetrow += 1
	workbook.close()
#求编辑距离
def edit_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    dp = np.zeros((len1 + 1,len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i     
    for j in range(len2 + 1):
        dp[0][j] = j  
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
    dis = dp[len1][len2]
    return dis
# 求编辑距离最小者
def min_dis(titl):
	titls = []
	for tit in titl:
		edi = 0
		for tite in titl:
			if tite != tit:
				edi += edit_distance(tit, tite)
		titls.append([edi,tit])
	return sorted(titls,key = lambda i:i[0],reverse=False)[0][1]	
title()

