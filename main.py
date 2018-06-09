from dataProcessor import dataProcessor as dp
import timeit
    
    
def main():
    
    #data = readFile()
	filePath = "D:\Prashant\Learning\Airline\Airline_Data\Airports.csv"
	
	dp.validateFile(filePath)
	
	#df = dp.readChunks(filePath, "1000","UTF-8",",")
	#print(df.shape[0])
	testcode = '''
filePath = "D:\Prashant\Learning\Airline\Airline_Data\Airports.csv"
from dataProcessor import dataProcessor as dp
dp.readChunks(filePath, "1000","UTF-8",",")
	'''
	times = timeit.timeit(testcode,number=10)
	print(times) 
if __name__ == "__main__":
    main()