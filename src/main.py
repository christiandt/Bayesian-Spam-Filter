from filter import Filter
import sys

# Get arguments from user
train = sys.argv[1]
messages = sys.argv[2]

# Open files for reading and writing
train_file = open(train, "rb")
messages_file = open(messages, "rb")
predictions_file = open("predictions.txt", "w")

# Create new filter and train it using the train-file
f = Filter()
f.train(train_file)

# Loop through all SMSes and compute total spam probability of the sms-message
lineNumber = 0
for sms in messages_file:
	lineNumber+=1
	spam_product = 1.0
	ham_product = 1.0
	if lineNumber % 2 != 0:
		for word in f.get_intresting_words(sms):
			spam_product *= word.get_probability()
			ham_product *= (1.0 - word.get_probability())

		sms_spam_probability = spam_product / (spam_product + ham_product)

		if sms_spam_probability > 0.9:
			predictions_file.write("spam")
		else:
			predictions_file.write("ham")
	predictions_file.write("\n")


# Close all the files
train_file.close()
messages_file.close()
predictions_file.close()