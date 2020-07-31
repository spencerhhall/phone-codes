import os.path
from os import path

def getInput(prompt, isFilename):
	while True:
		response = input(prompt + "\n")

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