from filter import Filter
import sys

train = sys.argv[1]
messages = sys.argv[2]

train_file = open(train, "rb")
messages_file = open(messages, "rb")

f = Filter()
f.train(train_file)

lineNumber = 0
for sms in messages_file:
	lineNumber+=1
	positive_product = 1.0
	negative_product = 1.0
	if lineNumber % 2 != 0:
		for word in f.get_intresting_words(sms):
			positive_product *= word.get_probability()
			negative_product *= (1.0 - word.get_probability())
		sms_spam_probability = positive_product / (positive_product + negative_product)
		if sms_spam_probability > 0.9:
			print "spam: " + sms.strip()
		else:
			print "ham: " + sms.strip()


train_file.close()
messages_file.close()
