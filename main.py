import csv
from tweetProfile import processedTweet
import indicoio
import apikey
# api-key contains: indicoio.config.api_key = '[key]'

m = csv.writer(open('test.csv','wb+'))

with open('testdata.csv') as f:
	me = csv.reader(f)
	for i in me:
		emotionArray = indicoio.emotion(i)
		# print(i[0])
		# print(emotionArray[0])
		mydata = processedTweet(emotionArray[0],i[0])

		# write mydata as a line into CSV file
		m.writerow(mydata())
		# m.writerow([i, "joy":Emotions["joy"],
		# 	"anger":Emotions["anger"],
		# 	"fear":Emotions["fear"],
		# 	"sadness":Emotions["sadness"],
		# 	"surprise":Emotions["surprise"]
		# )

		print(mydata())
		print("\r\n")
	else:
		print("done")
		# python obj to csv using X tool
		# write into a new CSV

# ["8cd9ccbc2a7f864edff7306faae88064","sentiment sentencesentiment sentencesentiment sentencesentiment sentence",{"Sentiment":{"joy":.0.1}}],
