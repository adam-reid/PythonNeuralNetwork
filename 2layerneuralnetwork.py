#!/usr/bin/python
import numpy as np

def nonlin(x,deriv=False):
	if deriv:
		return x*(1-x)
	return 1.0 / (1+np.exp(-x))

def analyze():
	X = np.array([[0,0,1],
				[ 0,1,1],
				[1,0,1],
				[1,1,1]])
				
	y = np.array([[0],
				[1],
				[1],
				[0]])
				
	np.random.seed(69069)

	syn0 = 2*np.random.random((3,4)) - 1
	syn1 = 2*np.random.random((4,1)) - 1

	for j in range(50000):
		layer0 = X
		
		layer1 = nonlin(np.dot(layer0,syn0))
		layer2 = nonlin(np.dot(layer1,syn1))
		
		layer2_error = y - layer2
		layer2_delta = layer2_error*nonlin(layer2,True)
		
		if j%5000==0:
			print("Update: " + str(np.mean(np.abs(layer2_error))))
		
		layer1_error = layer2_delta.dot(syn1.T)
		layer1_delta = layer1_error*nonlin(layer1,True)
		
		syn1+=layer1.T.dot(layer2_delta)
		syn0+=layer0.T.dot(layer1_delta)
		
	x = input("Press enter to continue!")
	
if __name__ == "__main__":	
	analyze()