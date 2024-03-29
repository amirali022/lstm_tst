import matplotlib.pyplot as plt

def plot_loss( history):
	plt.figure()
	plt.plot( history.history[ "loss"])
	plt.xlabel( "Epochs")
	plt.title( "Training Loss")
	plt.show()