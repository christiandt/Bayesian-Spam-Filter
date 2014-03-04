class Word():

	def __init__(self, word):
		self.word = word;
		self.spam_count = 0
		self.ham_count = 0
		self.spam_fraction = 0.0
		self.ham_fraction = 0.0
		self.spam_probability = 0.0

	def compute_probability(self, ham_total, spam_total):
		self.spam_fraction = float(self.spam_count) / float(spam_total)
		self.ham_fraction = float(self.ham_count) / float(ham_total)

		print str(self.spam_count) + " / " + str(spam_total) + " = " + str(self.spam_fraction)

		#print self.ham_fraction
		#print self.spam_fraction

		if self.ham_fraction + self.spam_fraction > 0:
			self.spam_probability = self.spam_fraction / (self.spam_fraction + self.ham_fraction)
		#if self.spam_probability < 0.01:
		#	self.spam_probability = 0.01
		#elif self.spam_probability > 0.99:
		#	self.spam_probability = 0.99

	def interesting(self):
		return Math.abs(0.5-self.spam_probability)

	def increment_ham(self):
		self.ham_count += 1

	def increment_spam(self):
		self.spam_count += 1

	def get_probability(self):
		return self.spam_probability
