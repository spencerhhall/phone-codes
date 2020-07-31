import clean, convert, viz, os.path
from ask import getInput

PROMPT = "Enter the desired number of results"

def main():
	# The second argument is only True if we're looking to find a file
	fileName = getInput("Enter the name of the wordlist file (must be a txt)", True)
	lengthSetting = getInput("Enter the desired word length", False)

	cleanedList = clean.cleanWordlist(fileName, int(lengthSetting))
	numberCombos = convert.convertToNumbers(cleanedList)
	viz.graphResults(numberCombos, fileName, lengthSetting, int(getInput(PROMPT, False)))

if __name__ == "__main__":
   main()