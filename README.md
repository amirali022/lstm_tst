### LSTM Playground

#### Notebooks

1. [Time-series prediction using LSTM implemented using keras](./src/LSTM_with_keras.ipynb)
	- lag of one
	- single feature for network
2. [same as [1] + using window method](./src/LSTM_with_keras_window_input.ipynb)
	- lag of three
	- three features for network
	- single timestep
3. [same as [1] + using timesteps](./src/LSTM_with_keras_timesteps.ipynb)
	- lag of three
	- three timesteps
	- single feature
4. [same as [1] + stateful training](./src/LSTM_with_keras_stateful.ipynb)
	- lag of three
	- three timesteps
	- single feature
	- batch size of one
5. [same as [4] + stacked LSTM layers](./src/LSTM_with_keras_stacked.ipynb)
	- two lstm layer (first one returns sequence)
	- lag of three
	- three timesteps
	- single feature
	- batch size of one

6. [Fine Tuning LSTM Network](./src/LSTM_with_keras_tuning.ipynb)
	- finding best number of epochs
	- batch size

7. [RNN Implementation](./src/RNN_Numpy.ipynb)
	- implementing from scratch using numpy
	- simple sentiment analysis task

#### Requirements

- python 3.11 or above
- jupyter notebook

#### Libraries

- numpy
- pandas
- matplotlib
- scikit-learn (sklearn)
- tensorflow
- keras

#### Credit

- [Time-series prediction using lstm rnn](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)
- [How to Tune LSTM Hyperparameters with Keras for Time Series Forecasting](https://machinelearningmastery.com/tune-lstm-hyperparameters-keras-time-series-forecasting/)
- [Building a Neural Network Zoo From Scratch: The Recurrent Neural Network](https://medium.com/@CallMeTwitch/building-a-neural-network-zoo-from-scratch-the-recurrent-neural-network-9357b43e113c)