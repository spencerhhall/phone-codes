import clean, convert, viz, os.path
from os import path

def main():
	while False:
		fileName = input("Enter the name of the wordlist file (must be a txt)\n")
		if ".txt" not in fileName:
			fileName += ".txt"
		if path.exists(fileName):
	 		break

	while True:
		lengthSetting = input("Enter the desired word length\n")
		# Ensures that the length is a positive integer
		if lengthSetting.isdigit() and lengthSetting != "0":
			break

	cleanedList = clean.cleanWordlist("wiki-100k.txt", int(lengthSetting))
	numberCombos = convert.convertToNumbers(cleanedList)
	viz.graphResults(numberCombos, "wiki-100k.txt", lengthSetting)

if __name__ == "__main__":
   main()