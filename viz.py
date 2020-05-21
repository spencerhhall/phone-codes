import matplotlib.pyplot as plt

def graphResults(results, fileName, characterCount):
	keys = results.keys()
	values = results.values()
	plt.bar(keys, values)
	fileName = fileName.replace(".txt", "")
	plt.savefig(fileName + "-" + characterCount + "-letters" + ".png")