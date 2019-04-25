import random

class Caching:
	def __init__(self,numberOfContentObjects):
		self.Dataset=[i for i in range(1,numberOfContentObjects+1)]
		
	def getPopularContents(self,cloudCacheCapacity):
		data=self.Dataset
		random.shuffle(data)
		return data[:cloudCacheCapacity]
	
	def ProactiveCaching(self,BBU,RRHs):
		totalRequired=BBU.cloudCacheCapacity+sum([rrh.cacheCapacity for rrh in RRHs])
		popular=self.getPopularContents(totalRequired)
		random.shuffle(popular)
		BBU.updateCache(popular[:BBU.cloudCacheCapacity])
		popular=popular[BBU.cloudCacheCapacity:]
		for rrh in RRHs:
			rrh.updateCache(popular[:rrh.cacheCapacity])
			popular=popular[rrh.cacheCapacity:]
	
	
		