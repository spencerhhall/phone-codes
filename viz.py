import numpy as np, matplotlib.pyplot as plt

def graphResults(numberCombos, fileName, length):
	values = numberCombos.values()
	dictCopy = dict(numberCombos)
	maxBars = 30

	if len(numberCombos) > maxBars:
		print(len(numberCombos))
		valCopies = []

		for v in values:
			valCopies.append(v)
		valCopies.sort()

		valMin = valCopies[-maxBars]
		valMax = valCopies[-1]
		for x, y in numberCombos.items():
			if numberCombos[x] <= valMin:
				dictCopy.pop(x)

	keys = dictCopy.keys()
	values = dictCopy.values()

	plt.grid(True, alpha = .25)
	plt.bar(keys, values)
	plt.yticks(np.arange(0, valMax + 2, step = 1))
	plt.xticks(rotation = 70)
	plt.xlabel("Combination")
	plt.ylabel("Frequency")
	plt.title("Top " + str(len(keys)) + " " + length + "-Letter Combinations from " + fileName)
	plt.show()

	#plt.savefig(fileName[:-4] + "-" + length + "-letters" + ".png")