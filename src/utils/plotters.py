import matplotlib.pyplot as plt

def plot_loss( loss):
	plt.figure()
	plt.plot( loss)
	plt.xlabel( "Epochs")
	plt.title( "Training Loss")
	plt.show()