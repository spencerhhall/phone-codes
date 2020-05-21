from unidecode import unidecode

def cleanWordlist(fileName, length):
	cleanedList = []
	wordlist = open(fileName, "r")

	for word in wordlist:
		# Transforms non-Unicode characters and strips newline characters
		word = unidecode(word.rstrip()).lower()
		if len(word) == length and word.isalpha(): # Checks length and must be 100% letters
			cleanedList.append(word)

	return cleanedList