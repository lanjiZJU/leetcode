class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nameList = {}
        self.count = 0
        self.tweetTime = {}
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.count += 1
        self.tweetTime[tweetId] = self.count
        if userId not in self.nameList:
        	self.nameList[userId] = {}
        	self.nameList[userId]["tweetList"] = []
        	self.nameList[userId]["follow"] = []
        	self.nameList[userId]["tweetList"].append(tweetId)
        else: 
        	self.nameList[userId]["tweetList"].append(tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        def tweetTime(a, b):
        	if self.tweetTime[b] < self.tweetTime[a]:
        		return 1
        	else:
        		return -1
        result = []
        if userId in self.nameList:
        	result += self.nameList[userId]["tweetList"]
        	for followeeId in self.nameList[userId]["follow"]:
        		if followeeId != userId:
        			result += self.nameList[followeeId]["tweetList"]
        	result.sort(tweetTime)
        	result.reverse()
        	return result[0:10]
        else:
        	return []

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.nameList:
        	self.nameList[followerId] = {}
        	self.nameList[followerId]["tweetList"] = []
        	self.nameList[followerId]["follow"] = []
        	self.nameList[followerId]["follow"].append(followeeId)
        else:
        	if followeeId not in self.nameList[followerId]["follow"]:
        		self.nameList[followerId]["follow"].append(followeeId)

        if followeeId not in self.nameList:
        	self.nameList[followeeId] = {}
        	self.nameList[followeeId]["tweetList"] = []
        	self.nameList[followeeId]["follow"] = []
        
      

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.nameList or followeeId not in self.nameList:
        	return 0
        if followeeId in self.nameList[followerId]["follow"]:
        	self.nameList[followerId]["follow"].remove(followeeId)