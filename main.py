import csv
from tweetProfile import processedTweet
import indicoio
import api-key.py
# api-key contains: indicoio.config.api_key = '[key]'

with open('xcn.csv') as f:
	me = csv.reader(f)
	for i in me:
		emotionArray = indicoio.emotion(i)
		# print(i[0])
		# print(emotionArray[0])
		mydata = processedTweet(emotionArray[0],i[0])

		# write mydata as a line into CSV file
		# OR! push it to an array, and run a cleanup task at the end
		# of the loop to write to file all at once.
		# ...well...the challenge is holding it all in memory

		print(mydata())
		print("\r\n")
	else:
		print("done")
		# python obj to csv using X tool
		# write into a new CSV



# ["8cd9ccbc2a7f864edff7306faae88064","sentiment sentencesentiment sentencesentiment sentencesentiment sentence",{"Sentiment":{"joy":.0.1}}],
