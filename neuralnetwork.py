"""
This was taken and modified from the following website:
https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1#.opgpgl80g

and is a clone of :
https://gist.github.com/miloharper/62fe5dcc581131c96276#file-short_version-py

This is not my code nor my design. There are no licenses associated in the
above GitHub account, and there are none in mine. 
"""

# need exponential, array transforms, randomness, and dot product of matrices
from numpy import exp, array, random, dot 

#training set to determine the weights
training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
#training set output is the goal
training_set_outputs = array([[0,1,1,0]]).T
#use fixed seed for rng (for repeatability)
random.seed(1)
#randomly assign weights
synaptic_weights = 2 * random.random((3,1))-1
#generate 10,000 samples
for iteration in range(10000):
        #use Sigmoid function to calculate results
        output = 1 / (1 + exp(-(dot(training_set_inputs,synaptic_weights))))
	#adjust the weights using the results and the current knowledge
	synaptic_weights += dot(training_set_inputs.T,
                                (training_set_outputs - output) * output * (1-output))
#display results to user
print(1 / (1 + exp(-(dot(array([1,0,0]),synaptic_weights)))))
