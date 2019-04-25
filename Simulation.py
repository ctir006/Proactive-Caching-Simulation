from BBU import BBU
from RRH import RRH
from Caching import Caching


def initializeSimulation():
	print("Initializing Simulation please enter details below --> ")
	#print("Enter number of videos(content Objects in the system) : ",end="")
	numberOfContentObjects=1000#int(input())
	#print("Enter size of each Video : ",end="")
	sizeOfContentObject=20#int(input())
	NumberOfRRHs=5#int(input("Enter number of RRH's : "))
	userCounts=[7,5,9,8,10]
	# for i in range(1,NumberOfRRHs+1):
		# print("Enter number of user for RRH ",i,": ",end="")
		# userCounts.append(int(input()))
	rrhIds=[i for i in range(1,NumberOfRRHs+1)]
	return BBU(1,rrhIds,userCounts,sizeOfContentObject),numberOfContentObjects,sizeOfContentObject
	
if __name__=='__main__':
	BBU,numberOfContentObjects,sizeOfContentObject=initializeSimulation()
	Cache=Caching(numberOfContentObjects)
	Cache.ProactiveCaching(BBU,BBU.associatedRRHs)
	print("Content in Cloud Cache : ",BBU.cloudCache[:15],len(BBU.cloudCache))
	print("Contents in edge caches : ")
	for rrh in BBU.associatedRRHs:
		print("RRH ",rrh.RRHID,": ",rrh.edgeCache[:15],len(rrh.edgeCache))
	print(BBU.getDetails())
	
	
	
	
	
	
# def initializeSimulation():
	# NumberOfBBUs=int(input("Enter number of BBU's : "))
	# BBUs=[]
	# numberOfRRHs=1
	# for i in range(1,NumberOfBBUs+1):
		# print("Enter number of RRHs in BBU ",i,": ")
		# n=int(input())
		# rrhIds=[i for i in range(numberOfRRHs,numberOfRRHs+n)]
		# numberOfRRHs=numberOfRRHs+n
		# BBUs.append(BBU(i,rrhIds))
	# return BBUs	