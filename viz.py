import numpy as np, matplotlib.pyplot as plt, summarize

def graphResults(numberCombos, fileName, length, maxBars):
	
	summarize.summarize(numberCombos)

	values = numberCombos.values()
	dictCopy = dict(numberCombos)

	# With large wordlists, there will be far too many number combinations to display
	# It is easier to have the user suggest a number of combinations to display
	# Becuase I'm lazy and there will usually be combos with the same frequency, the suggested
	# number is not usually the actual display number
	if len(numberCombos) > maxBars:
		valCopies = []

		# Sorts the frequencies so we can take the desired amount
		for v in values:
			valCopies.append(v)
		valCopies.sort()

		valMin = valCopies[-maxBars]
		valMax = valCopies[-1]

		# Removes items that do not meet the minimum frequency requirement
		for x, y in numberCombos.items():
			if numberCombos[x] < valMin:
				dictCopy.pop(x)

	keys = dictCopy.keys()
	values = dictCopy.values()

	plt.bar(keys, values)
	plt.xlabel("Combination")
	plt.ylabel("Frequency")
	plt.title("Top " + str(len(keys)) + " " + length + "-Letter Combinations from " + fileName)
	plt.xticks(rotation = 70)
	plt.yticks(np.arange(0, valMax + 1, step = 1))
	plt.grid(True, alpha = .25)
	plt.show()

	# plt.savefig(fileName[:-4] + "-" + length + "-letters" + ".png")