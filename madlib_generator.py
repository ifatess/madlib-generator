import nltk # involves some downloading/installing dependencies to use all its features
import random

debug = False #True

# get file from user to make mad lib out of
if debug:
	print "Getting information from a file...\n"
fname = "madlib_test.txt" # need a file with this name in directory
#fname = raw_input("What's the file you want to turn into a madlib?\nEnter the full name.\n")

f = open(fname, 'r')
para = f.read()
if debug:
	print "Tokenizing file...\n"
tokenized_file = nltk.word_tokenize(para)
tagged_file = nltk.pos_tag(tokenized_file) # gives us a tagged list of tuples

# map abbrvs to POS for tags
tagmap = {"NN":"noun","NNS":"plural noun","VB":"verb","JJ":"adjective"}

if debug:
	print "Separating words into parts of speech list,\ntuples that look like('word','POS'), using NLTK methods...\n"
# take out a few random words of each tag type
nouns = [(n,t) for (n,t) in tagged_file if t == 'NN'] # how would you do this with a filter instead? etc
pnouns = [(n,t) for (n,t) in tagged_file if t == 'NNS']
verbs = [(n,t) for (n,t) in tagged_file if t == 'VB']
adjs = [(n,t) for (n,t) in tagged_file if t == 'JJ']
#adjs = filter(lambda n,t: t == "JJ", tagged_file)

# list all parts of speech we care about -- save tuple lists in one
all_types = [nouns, pnouns, verbs, adjs] # this is a list of lists of tuples

# function for picking random words from a set of words that are a certain pos
def pick_random_words(wordlist,number): # TODO: add check for number not being too many
	num = len(wordlist)
	indexes = [random.choice(range(num)) for x in range(number)]
	words = [wordlist[i][0] for i in indexes]
	return words
if debug:
	print "Going through each list and replacing them for each random word picked..."
for t in all_types: # a t is a list of tuples of that type
	wl = pick_random_words(t,2) # using the function, get a list of words and pick out a number to replace
	for w in wl:  # for each of those list of words we picked,
		para = para.replace(w,t[0][1]) # replace it with the abbrevation for the POS

# play madlib
i = 0 
interpolators = []
if debug:
	print "iterating over words and adding to a list to interpolate in...\n(we want to use a list because lists are mutable!\n"
split_text = nltk.word_tokenize(para) # retokenize the madlibbed text -- we want to go through a list of 'words'
for wd in split_text: # for each word in the list split_text
	if wd in tagmap: # if it's a POS abbreviation like NN or JJ
		new_word = raw_input("Please enter a %s:\n" % (tagmap[wd])) # ask for the correct type of word and save it in a variable
		interpolators.append(new_word)
		split_text[i] = "%s" # change the list, since lists are mutable, so that index is that word now
	i += 1 # add 1 to i to keep up index count
if debug:
	print "Joining the words together into a paragraph we can read...\n"
print " ".join(split_text) % (tuple(interpolators)) # use the " ".join() str method to put the list back together into a paragraph
