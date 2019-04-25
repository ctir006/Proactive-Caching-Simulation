from User import User

class RRH:
	def __init__(self,id,UserIds):
		self.RRHID=id
		self.associatedUsers=[User(i) for i in UserIds]
		self.edgeCacheSize=1000		#Mb
		self.cacheCapacity=50
		self.edgeCacheStatus=0
		self.edgeCache=[]
		
	def requestHandler(self):
		pass
	
	def getInfo(self):
		return [self.RRHID,[user.userID for user in self.associatedUsers]]
		
	def updateCache(self,data):
		self.edgeCache=data
		self.edgeCacheStatus+=len(data)
		
	