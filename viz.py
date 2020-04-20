import clean
# ask for file
# ask for specific char length
# analyze list and produce visualization

# Get the desired file
fileName = None
while fileName == None:
	fileName = input("Enter the name of the wordlist file\n")

	if ".txt" not in fileName:
		fileName += ".txt"

	try:
		f = open(fileName, "r")
		# ask for character count
		# clean file
	except:
		print("Invalid file name.")
		fileName = None

# call analysis on new df
# 