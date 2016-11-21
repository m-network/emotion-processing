import csv
from tweetProfile import processedTweet
import indicoio
import apikey
# api-key contains: indicoio.config.api_key = '[key]'

m = csv.writer(open('test.csv','wb+'),quoting=csv.QUOTE_NONE, quotechar='',escapechar='\\')

with open('testdata.csv') as f:
	me = csv.reader(f)
	for i in me:
		emotionArray = indicoio.emotion(i)
		# print(i[0])
		# print(emotionArray[0])
		mydata = processedTweet(emotionArray[0],i[0])

		# write mydata as a line into CSV file
		m.writerow(mydata())

		print(mydata())
		print("\r\n")
	else:
		print("done")
		# python obj to csv using X tool
		# write into a new CSV
