import clean, convert, viz, os.path
from os import path

def main():
	while False:
		fileName = input("Enter the name of the wordlist file (must be a txt)\n")
		if ".txt" not in fileName:
			fileName += ".txt"
		if path.exists(fileName):
	 		break
	fileName = "wiki-100k.txt"

	while True:
		lengthSetting = input("Enter the desired word length\n")
		# Ensures that the length is a positive integer
		if lengthSetting.isdigit() and lengthSetting != "0":
			break

	while True:
		outputMax = input("Enter the desired number of results\n")
		if outputMax.isdigit() and outputMax != "0":
			break

	cleanedList = clean.cleanWordlist(fileName, int(lengthSetting))
	numberCombos = convert.convertToNumbers(cleanedList)
	viz.graphResults(numberCombos, fileName, lengthSetting, int(outputMax))

if __name__ == "__main__":
   main()