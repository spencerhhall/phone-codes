from unidecode import unidecode

def cleanWordlist(fileName, characterCount):
	cleanedList = []
	f = open(fileName, "r")

	for line in f:
		line = unidecode(line.rstrip().lower())
		if len(line) == characterCount and line.isalpha():
			cleanedList.append(line)

	return cleanedList