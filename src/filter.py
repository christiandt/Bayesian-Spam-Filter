from word import Word
import sys

#file = sys.argv[1]

class Filter():

	def __init__(self):
		self.words = dict()


	def train(self, file_name):
		lineNumber = 1
		ham_words = 0
		spam_words = 0

		for line in file_name:
			if lineNumber % 2 != 0:
				line = line.split('\t')
				category = line[0]
				input_words = line[1].strip().split(' ')
				for input_word in input_words:
					input_word = input_word.strip(' .:,-!()"?+<>*')
					input_word = input_word.lower()
					if input_word != "":

						if input_word in self.words:
							word = self.words[input_word]
						else:
							word = Word(input_word)
							self.words[input_word] = word

						if category == "ham":
							word.increment_ham()
							ham_words += 1
						elif category == "spam":
							word.increment_spam()
							spam_words += 1
						else:
							print "Not valid"
						
			lineNumber+=1
		#print ham_words
		#print spam_words

		for word in self.words:
			self.words[word].compute_probability(ham_words, spam_words)
			
			#print word
			#print self.words[word].ham_count
			#print self.words[word].spam_count
			#print self.words[word].get_probability()



train_file = open("smsSpamCollection-train.txt", "rb")

f = Filter()
f.train(train_file)