from unidecode import unidecode

# fileName: string that contains the name of the wordlist file
# length: int that represents the length of the combination
def cleanWordlist(fileName, length):
	cleanedList = []
	wordlist = open(fileName, "r")

	for word in wordlist:
		# Transforms non-Unicode characters and strips newline characters
		word = unidecode(word.rstrip()).lower()
		if len(word) == length and word.isalpha(): # Checks length and must be 100% letters
			cleanedList.append(word)

	# cleanedList now contains all words of x length
	return cleanedList