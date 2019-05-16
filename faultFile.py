import xlrd
import re
import csv

# junjieLi 
# 2019.05.16
data = xlrd.open_workbook(r"./错误数据.xlsx")
table = data.sheet_by_index(0)
num = table.nrows
newlist = []
for i in range(0,num):
	furaw = ",".join([str(a) for a in table.row_values(i)])
	furaw = re.sub('[\r\n\t]', '', furaw)
	ut1 = re.findall("WOS:\d+",furaw)
	if ut1:
		for ut in ut1:
			fu = furaw[:furaw.index(ut)]
			fu = fu.strip()
			if fu[-1] == "," :
				fu = fu[:-1]
			newlist.append([fu,ut])
			furaw = furaw[furaw.index(ut)+len(ut):]
with open("correctFiles.csv",'a',encoding='utf-8',newline='') as csvf:
	csvw = csv.writer(csvf)
	csvw.writerows(newlist)

