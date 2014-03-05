from word import Word
import sys

#file = sys.argv[1]

class Filter():

	def __init__(self):
		self.words = dict()


	def trim_word(self, word):
		word = word.strip(' .:,-!()"?+<>*')
		word = word.lower()
		return word


	def train(self, file_name):
		lineNumber = 1
		ham_words = 0
		spam_words = 0

		# Loop through all the lines
		for line in file_name:
			if lineNumber % 2 != 0:
				line = line.split('\t')
				category = line[0]
				input_words = line[1].strip().split(' ')

				#Loop through all the words in the line, remove some characters
				for input_word in input_words:
					input_word = input_word
					if input_word != "":
						input_word = self.trim_word(input_word)
						# Check if word is in dicionary, else add
						if input_word in self.words:
							word = self.words[input_word]
						else:
							word = Word(input_word)
							self.words[input_word] = word

						# Check wether the word is in ham or spam sentence, increment counters
						if category == "ham":
							word.increment_ham()
							ham_words += 1
						elif category == "spam":
							word.increment_spam()
							spam_words += 1

						# Probably bad input...
						else:
							print "Not valid"
						
			lineNumber+=1

		for word in self.words:
			self.words[word].compute_probability(ham_words, spam_words)
			
			#print word
			#print self.words[word].ham_count
			#print self.words[word].spam_count
			#print self.words[word].get_probability()

	def get_intresting_words(self, sms):
		intresting_words = []

		for input_word in sms.split(' '):
			input_word = self.trim_word(input_word)
			if input_word != "":
				if input_word in self.words:
					word = self.words[input_word]
				else:
					word = Word(input_word)
					word.set_probability(0.40)
				intresting_words.append(word)

		intresting_words.sort(key=lambda word: word.interesting(), reverse=True)
		return intresting_words[0:15]


train = sys.argv[1]
messages = sys.argv[2]

train_file = open(train, "rb")
messages_file = open(messages, "rb")

f = Filter()
f.train(train_file)

for sms in messages_file:
	print "*********************"
	print sms
	for word in f.get_intresting_words(sms):
		print word.get_word()
	print "*********************"


train_file.close()
messages_file.close()
