import os
import numpy as np
import csv
import pandas as pd
# junjieLi
# 2019.05.16

def deDuplication():
	filenames = os.listdir('./FuDealt')
	fucsvList = [ filename for filename in filenames if filename.endswith(".csv") ]
	dpubFunds = set([])
	for fucsv in fucsvList:
		dealFile = './FuDealt/' + fucsv
		f = open(dealFile, encoding = "utf-8")
		data = pd.read_csv(f,header=None)
		dataTable = pd.DataFrame(data)
		dataTable = dataTable.dropna(axis=0, how='all')
		dpubFunds = dpubFunds | set(dataTable[4].values)
	dpubFunds = np.transpose([list(dpubFunds)]).tolist()
	with open("dpubFunds.csv",'w',encoding='utf-8-sig',newline='') as csvf:
		csvw = csv.writer(csvf)
		csvw.writerows(dpubFunds)

if __name__ == "__main__":
	deDuplication()