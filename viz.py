import matplotlib.pyplot as plt

def graphResults(results):
	keys = results.keys()
	values = results.values()
	plt.bar(keys, values)
	plt.savefig("out.png")

