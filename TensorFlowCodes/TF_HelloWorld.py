
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-

### Learning TensorFlow with Laurence Moroney, Google Brain on Coursera
### /Users/trannguyen/TranData/WORK/BioinformaticsSpecialization_Tran_2019/\
###/MachineLearning/TensorFlow/TensorFlowCodes

### import modules used here -- sys is a very standard one
import tensorflow as tf
import numpy as np
from tensorflow import keras
import h5py
#keras: the framework for defining a neural network as a set of Sequential layers


def simple_neural_network(xs,ys):
    ## define a neural network (nn)
    # a simplest nn: 1 layer, 1 neuron, the input shape to it is just 1 value.
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    ## define a model 
    model.compile(optimizer='sgd', loss='mean_squared_error')
    #optimizer: stochastic gradient descent
    #loss: cost function using mean squared error

    ##training the nn
    model.fit(xs, ys, epochs=500)

    return model

########################################################################
# The main() function
def main():
    ##input data
    xs=np.array([-1.0,0.0,1.0,2.0,3.0,4.0], dtype=float)
    ys=np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
    y=simple_neural_network(xs,ys).predict([10.0])
    print(y)
#######################################################################
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()

