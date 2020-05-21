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
		characterCount = input("Enter an amount of characters\n")
		if characterCount.isdigit() and characterCount != "0":
			break

	cleanedWordlist = clean.cleanWordlist("wiki-100k.txt", int(characterCount))
	print(cleanedWordlist)
	numbers = convert.convertToNumbers(cleanedWordlist)
	print(numbers)
	viz.graphResults(numbers, "wiki-100k.txt", characterCount)

if __name__ == "__main__":
   main()