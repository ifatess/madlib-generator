# code developed by Jackie Cohen; revised by Paul Resnick and Colleen Van Lent
import nltk #
import random

debug = False #True
if debug:
	print "Getting information from file madlib_test.txt...\n"
fname = "madlib_test.txt" # need a file with this name in directory

f = open(fname, 'r')
para = f.read()
tokens = nltk.word_tokenize(para)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
if debug:
	print "First few tagged tokens are:"
	for tup in tagged_tokens[:5]:
		print tup

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.1,"NNS":.2,"VB":.25,"JJ":.25}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities 
		if random.random() > substitution_probabilities[tag]:
			final_words.append(spaced(word))
		substitution_probabilities[tag]:
			final_words.append(spaced(word)) # This is a terrible revision, but it will introduce a conflict
	else:
		new_word = raw_input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print "".join(final_words)