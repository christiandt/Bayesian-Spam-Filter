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

#filter the messages in messages_file, write results to predictions_file
f.filter(messages_file, predictions_file)

# Close all the files
train_file.close()
messages_file.close()
predictions_file.close()