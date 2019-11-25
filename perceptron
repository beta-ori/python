#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:23:18 2019

@author: beta-ori
"""

import numpy as np

def sigmoid(x):
	return 1 /(1 + np.exp(-x))


def sigmoid_derivative(x):
    return x*(1-x)

training_inputs = np.array([[0, 0, 1],
				          [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

weights = np.random.random((3,1))


for i in range(10000):
    outputs = sigmoid(np.dot(training_inputs, weights))
    error = training_outputs - outputs
    adjustments = error*sigmoid_derivative(outputs)
    weights += np.dot(training_inputs.T, adjustments)
    
print('Weights:')
print(weights)
print('\nOutputs:')
print(np.round(outputs))


inputs = np.array([[1, 0, 0],
                   [0, 1, 1],
                   [1, 1, 0]])
        
outputs = sigmoid(np.dot(inputs, weights))
print('\nOutputs:')
print(np.round(outputs))
