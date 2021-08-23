# Neural Network Code!
import numpy as np
import math_func_practice as ma

# toes % wins # fans


# weights = np.array([0.1,0.2,0])
ih_wgt = np.array([
                  [0.1, 0.2, -0.1], #hid[0]
                  [-0.1, 0.2, 0.9], #hid[1]
                  [0.0, 0.4, 0.1]]).T #hid[2]

# hid[0], hid[1], hid[2]

hp_wgt = np.array([
                  [0.3, 1.1, -0.3], # hurt?
                  [0.1, 0.2, 0.0],  #win?
                  [0.1, 0.4, 0.1]]).T #sad?

weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
    
#     prediction = ma.weighted_sum(input,weights)
    hid = input.dot(weights[0])
    pred = input.dot(weights[1])
    #prediction = input.dot(weights)
    return pred


toes = np.array([8.5, 9.5, 10, 9])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])


input = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network(input, weights)
print(pred)

