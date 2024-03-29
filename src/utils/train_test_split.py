def train_test_split( data, split):
	split_idx = int( len( data) * split)
	train = data[ 0:split_idx, :]
	test = data[ split_idx:len( data), :]

	return train, test