class processedTweet(object):
	def __init__(self,Emotions,Tweet):
		self.emotions = {
			"joy":Emotions["joy"],
			"anger":Emotions["anger"],
			"fear":Emotions["fear"],
			"sadness":Emotions["sadness"],
			"surprise":Emotions["surprise"]
		}
		self.emotionFields = [
			Tweet,
			Emotions["joy"],
			Emotions["anger"],
			Emotions["fear"],
			Emotions["sadness"],
			Emotions["surprise"]
		]
		self.tweetData = Tweet
	#	self.time = Timestamp
	def __call__(self):
		preparedString = self.emotionFields
		return preparedString
