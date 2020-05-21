associations = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5,"mno": 6,"pqrs": 7,"tuv": 8, "wxyz": 9}

def convertToNumbers(words):
	numbers = {}
	# iterate through the list of words
	# convert the word into a number
	# if the key (number) exists, increase frequency (value)
	# if not, make new key and value (number, 1)
	# return dictionary
	for word in words:
		number = ""
		for char in word:
			num = [val for key, val in associations.items() if char.lower() in key]
			number += str(num[0])

		# now we have a complete number
		if number in numbers:
			numbers[number] = numbers[number] + 1
		else:
			numbers[number] = 1

	return numbers