def summarize(numberCombos, fileName, length):
	print("\n-= SUMMARY =-")
	print("File name: " + fileName)
	print("Chosen word length: " + length + " characters")
	print("Total number of combinations: " + str(len(numberCombos)))

	frequencies = numberCombos.values()

	print("Average frequency: " + str(sum(frequencies)/len(frequencies)))
	print("Lowest frequency: " + str(min(frequencies)))
	print("Highest frequency: " + str(max(frequencies)))