Bayesian-Spam-Filter
====================

## Running the program
The Bayesian SMS filter can be run using Python in the following way:

    python main.py <training_file> <testing_file>

example:
    python main.py training.txt testing.txt


## Program details
The SMS-spam filter consist of three files, word.py, filter.py and main.py. 

### Main
The main file is used to handle all the files used in the program and handle the filter object, invoking training and filtering.

### Filter Class
The Filter class is the main logic of the Bayesian filter. It has a train, get_interesting_words and filter methods, in addition to the helper method trim_word:

#### train:
This method is used to train the filter using the training file given as argument by the user. It loops through all the words in the file (after splitting on tab to get the category separated from the sentence) trimming them, and making a Word-object for every new word and adds it to a dictionary. It then increments the ham/spam counter for each time the word occurs in a ham/spam message. After it is done reading the file, it runs through all the words in the dictionary, computing the spam-probability for each one using the compute_probability-method in the word-class.

#### get_interesting_words:
This method is used to create a list of the top <=15 interesting words in the message. How interesting a word is, is defined as the difference in spam probability from 50%. It takes the sms message (string) as input, splits words on space, trims them and add them to the interesting_words list. If we have seen this word in training, we use that word, else we create a new word-object with a spam-probability of 40%. We then sort the list, and return the sorted list if it is less than or equal to 15, else we return the 15 top interesting words.

#### filter:
This filter is used to filter the input file given as argument by the user. It reads all the messages in the file, using get_interesting_words to get a list of the most interesting words, and then compute the ham/spam product of all the top interesting words in the message. It then calculates the total spam-probability of the message by dividing the spam product by the spam product plus the ham product. If the spam-probability of the message is higher than 90% we classify the message as spam, and write this to the result_file.

### Word Class
The Word class is used to store words, their spam/ham count spam/ham fraction and their spam probability. In addition to getters and setters, it has the following methods:

#### increment_ham:
This method is used to increment the counter of how many times this word has been labeled as ham.

#### increment_spam:
This method is used to increment the counter of how many times this word has been labeled as spam.

#### interesting:
This method is used to compute how interesting the word is. We define interesting as the deviation from 50% spam probability.

#### compute_probability:
This method is used to compute the probability of the word being spam. It takes the total number of ham and spam words as input to compute the fraction of ham/spam this word amount to using the ham/spam-count divided by the total ham/spam count. It then computes the probability using the spam fraction divided by the spam+ham fraction. If the probability of the word being spam is lower than 1%, we set it to 1%. If it is higher than 99%, we set it to 99%.

