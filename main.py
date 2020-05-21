import ask, clean, convert, viz, os.path
from os import path

def main():
	fileName = ask.getInput("Enter the name of the wordlist file (must be a txt)", True)
	lengthSetting = ask.getInput("Enter the desired word length", False)
	outputMax = ask.getInput("Enter the desired number of results", False)

	cleanedList = clean.cleanWordlist(fileName, int(lengthSetting))
	numberCombos = convert.convertToNumbers(cleanedList)
	viz.graphResults(numberCombos, fileName, lengthSetting, int(outputMax))

if __name__ == "__main__":
   main()