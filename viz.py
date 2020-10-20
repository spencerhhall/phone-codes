import numpy as np, matplotlib.pyplot as plt, summarize

def graphResults(numberCombos, fileName, length, maxBars):
	
	summarize.summarize(numberCombos, fileName, length)

	values = numberCombos.values()
	dictCopy = dict(numberCombos)

	# With large wordlists, there will be far too many number combinations to display
	# It is easier to have the user suggest a number of combinations to display
	# Because I'm lazy and there will usually be combos with the same frequency, the suggested
	# number is not usually the actual display number
	if len(numberCombos) > maxBars:
		valCopies = [] # why make a copy?

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

	# shoutout stack
	dictCopy = {k: v for k, v in sorted(dictCopy.items(), key=lambda item: item[1])}

	keys = dictCopy.keys()
	values = dictCopy.values()

	plt.bar(keys, values)
	plt.xlabel("Combination")
	plt.ylabel("Frequency")
	plt.title("Top " + str(len(keys)) + " " + length + "-Letter Combinations from " + fileName)
	plt.xticks(rotation = 75)
	plt.yticks(np.arange(0, valMax + 1, step = 1))
	plt.grid(True, alpha = .25)
	plt.show()

	# plotting the frequencies (values)
	# frequencies
	frequencies = numberCombos.values()

	# setting the ranges and no. of intervals 

	# plotting a histogram 
	plt.hist(frequencies, bins = max(frequencies), align = "mid", histtype = 'bar', rwidth = .9)

	plt.yscale("log")

	# x-axis label 
	plt.xlabel('Frequency of a Combination') 
	# frequency label 
	plt.ylabel('Combinations') 
	# function to show the plot 
	plt.show() 