import csv
import pandas as pd
import os

class dataProcessor:
	name = ""
	def validateFile(filepath):
		if (os.path.exists(filepath) and os.path.getsize(filepath) > 0):
			print("Valid Path" + filepath )
			return True
		else:
			print("Invalid Path" + filepath )
			return False
			
	def readChunks(file,chunks,encode,separator):
		df = pd.DataFrame()
		for i in range(0,10000,int(chunks)):
			try:
				tempDF = pd.read_csv(file, nrows=int(chunks), encoding=encode, skiprows=i,sep=separator,header=0)
				print(tempDF.shape[0])
				df = df.append(tempDF)
				#df.concat(df_chunck)
				#df2.append(df_chunked)
			except:
				print("No data to read")
				break
			
		return df
	
	def processData(data,columns,rules):
	
		return data
	
	def loadData(data,table):
	
		return 0
		
def __init__(self, name):
	self.name = name    # instance variable unique to each instance

        