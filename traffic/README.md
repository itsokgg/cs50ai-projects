# Experimentation Process
Experimenting with different configurations for this neural network, an ai to identify traffic signs, made me realize some things.
1) Adding to the neural network - wether with extra convolution layer filters, hidden layers, and nodes in hidden layers - doesnt always improve accuracy. ( the optimal seems to be a convolution layer filter of 64, 7 hidden layers, and 128 nodes per layer)
2) Making the poolsize bigger sometimes improves accuracy. Specifically, going from 2x2 to 3x3,
but 4x4 makes it less accurate
3) AveragePooling is more accurate than MaxPooling
4) The most Accurate dropout is 0.1
The model version in traffic.py is the most accurate model i found possible