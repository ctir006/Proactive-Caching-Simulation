class ContentServer:
	def __init__(self,totalNoOfDataObjects,):
		self.numberOfContentObjects=totalNoOfDataObjects
		self.contentIds=[i for i in range(1,self.numberOfContentObjects+1)]
	
	def requestHandler(self,contentID):
		if contentID in self.contentIds:
			return True
		else:
			return False
	