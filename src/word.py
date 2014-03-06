class Word():

	def __init__(self, word):
		self.word = word;
		self.spam_count = 0.0
		self.ham_count = 0.0
		self.spam_fraction = 0.0
		self.ham_fraction = 0.0
		self.spam_probability = 0.0

	def compute_probability(self, ham_total, spam_total):
		# Compute spam and ham fractions of the word using the total number of ham and spam messages
		self.spam_fraction = float(self.spam_count) / float(spam_total)
		self.ham_fraction = float(self.ham_count) / float(ham_total)

		# Compute the spam-probability using spam and ham fractions
		if self.ham_fraction + self.spam_fraction > 0:
			self.spam_probability = self.spam_fraction / (self.spam_fraction + self.ham_fraction)
		if self.spam_probability < 0.01:
			self.spam_probability = 0.01
		elif self.spam_probability > 0.99:
			self.spam_probability = 0.99

	def set_probability(self, probability):
		self.spam_probability = probability

	def interesting(self):
		# Compute how much the word differs from 50% spam probability
		# We denote this as how interesting the word is
		return abs(0.5-self.spam_probability)

	def increment_ham(self):
		self.ham_count += 1.0

	def increment_spam(self):
		self.spam_count += 1.0

	def get_probability(self):
		return self.spam_probability

	def get_word(self):
		return self.word

