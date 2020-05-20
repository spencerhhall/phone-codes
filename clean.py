# cleans an imported wordlist

def cleanWordlist(fileName):
	cleanedList = {}
	f = open(fileName, "r")
	for line in f:
		cleanedList.add(line.lower())

