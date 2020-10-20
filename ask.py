import os.path
from os import path

# prompt: string that contains the input prompt
# isFilename: boolean that indicates if the desired input is a file name
def getInput(prompt, isFilename):
	while True:
		response = input(prompt + "\n")

		# Checks for an existing file
		if isFilename:
			if ".txt" not in response:
				response += ".txt"
			if path.exists(response):
	 			break
	 	# Not looking for files, just need a non-zero number
		else:
			if response.isdigit() and response != "0":
				break

	return response