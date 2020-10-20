# Dictionary containing the number associated with each part of the alphabet
ASSOCIATIONS = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5,"mno": 6,"pqrs": 7,"tuv": 8, "wxyz": 9}

# wordlist: array that contains all words from the wordlist that are the desired length
def convertToNumbers(wordlist):
	combos = {}

	for word in wordlist:
		combo = ""
		# Iterates through each letter in the word and checks if it is part of any dict keys
		# (it should be 100% of the time) and then concatenates the associated value to the
		# combination
		for letter in word:
			# Shoutout StackOverflow for this tasty line
			number = [val for key, val in ASSOCIATIONS.items() if letter in key]
			combo += str(number[0]) # combo += number[0]

		# Combination is complete, now to add to dict if not already recorded or the frequency
		# of the combo is increased by 1
		if combo in combos:
			# Increases frequency by 1
			combos[combo] += 1
		else:
			combos[combo] = 1

	# combos is a dictionary containing all x length number combinations and their
	# frequency
	return combos