def summarize(numberCombos, fileName, length):
	print("\n-= SUMMARY =-")
	print("File name: " + fileName)
	print("Chosen word length: " + length + " characters")
	print("Total number of combinations: " + str(len(numberCombos)))

	frequencies = numberCombos.values()

	print("Average frequency: " + str(  round(sum(frequencies)/len(frequencies), 3)))
	print("Lowest frequency: " + str(min(frequencies)))
	print("Highest frequency: " + str(max(frequencies)))