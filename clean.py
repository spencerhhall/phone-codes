# cleans an imported wordlist
from unidecode import unidecode

def cleanWordlist(fileName):
	cleanedList = []
	f = open(fileName, "r")

	for line in f:
		line = unidecode(line.rstrip())
		if line.isalpha():
			cleanedList.append(line.lower())

	return cleanedList