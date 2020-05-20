import clean, os.path
from os import path


# import clean
# import a specified wordlist (check existence and file type)
# clean the file
# convert the file (probably use a dict)
# ~visualize~
def main():
	while False:
		fileName = input("Enter the name of the wordlist file (must be a txt)\n")
		if ".txt" not in fileName:
			fileName += ".txt"
		if path.exists(fileName):
	 		break

	characterCount = input("Enter an amount of characters\n")
	cleanedWordlist = clean.cleanWordlist("wiki-100k.txt", int(characterCount))
	print(cleanedWordlist)


if __name__ == "__main__":
   main()