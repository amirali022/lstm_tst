import numpy as np

def feature_label_split( dataset, lag=1):
	dataX, dataY = [], []

	for i in range( len( dataset) - lag - 1):
		a = dataset[ i:( i + lag), 0]
		dataX.append( a)
		dataY.append( dataset[ i + lag, 0])
	return np.array( dataX), np.array( dataY)