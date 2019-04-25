from RRH import RRH

class BBU:
	def __init__(self,id,rrhs,userCounts,sizeOfContentObject):
		self.BBUID=id
		userIds=[i for i in range(1,sum(userCounts)+1)]
		s=0
		UserIds=[]
		for i in userCounts:
			UserIds.append(userIds[s:s+i])
			s=s+i
		self.associatedRRHs=[RRH(v,UserIds[i]) for i,v in enumerate(rrhs)]
		self.sizeOfContentObject=sizeOfContentObject
		self.cloudChacheSize=4000		#Mb
		self.cloudCacheCapacity=200
		self.cloudCacheStatus=0
		self.cloudCache=[]
		
	def getDetails(self):
		d={}
		d["BBU id"]=self.BBUID
		d["Associated RRH IDs"]=[rrh.RRHID for rrh in self.associatedRRHs]
		dc,t={},[rrh.getInfo() for rrh in self.associatedRRHs]
		for i in t:
			dc[i[0]]=i[1]
		d["Associated userIDs"]=dc
		return d
	
	def updateCache(self,data):
		self.cloudCache=data
		self.cloudCacheStatus=len(data)
	
	def cloudCacheManager(self):
		pass
	
	def PerformProactiveCaching(self):
		pass
	
	