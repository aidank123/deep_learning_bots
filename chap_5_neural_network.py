#UPDATES:

#Getting there man just hard to understand IDK!!! Keep working
#Current error:  RuntimeWarning: invalid value encountered in double_scalars -- out[i][j] = vec_a[i] * vec_b[j]

#how do I solve this error first, then see if weight updates make literally any sense whatsoeover

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import chap_5_img_reader as m

#importing the math functions module u created
import math_func_practice as p

#neural network function

def neural_network(inputs,weights):
    
    #multiplying each input by each corresponding weight
    
    prediction = p.vect_matrix_multiplication(inputs,weights)
    return prediction

#calling the reader function and setting vars equal to the data
#ntrimages = number of training images (60,000)
train_images, train_labels, ntrimages, test_images, test_labels, nteimages = m.mnist_read()

x = 0
y = 0

img_num = 0 #what img number we are on
inputs = [] #initializing list of inputs, will be cleared at the start of each new image
alpha = 1 #setting alpha to .01


#initializing the weights, all to 1?
#turning weights into a matrix, 784 x 10 (i for each number)
weights = []
weight_rows = []
i = 0
j = 0
for j in range(10):
    i = 0
    weight_rows.clear()
    for i in range(784):
        weight_rows.append(1)

    weights.append(weight_rows)
    
#initializing list of correct guesses
correct_guess = []
i = 0
for i in range(784):
    correct_guess.append(train_labels[i])
    
#initializing list of possible predictions
possible_predictions = [0,1,2,3,4,5,6,7,8,9]
    
#loop continues until we have gone thru every image in the training set
while (img_num <= ntrimages):
    
    inputs.clear()
    
    # this concatates the 28 x 28 grid into a single list of inputs, 784 to be exact
    for x in range (0,28):
        for y in range (0,28):
        
            inputs.append((train_images[img_num])[x][y])
            
    #once the loop has finished adding to the inputs list (each pixel of the image), now we perform neural network calculations
    
    prediction = neural_network(inputs,weights)

    #initializing error vector, vector of 0's
    error = []
    i = 0
    for i in range(len(prediction)):
        error.append(0)
    
    #initializing delta vector, vector of 0's
    delta = []
    i = 0
    for i in range(len(prediction)):
        delta.append(0)
    
    #make list of desired outputs, 1 = correct, 0 = incorrect
    true = [0,0,0,0,0,0,0,0,0,0]   
    if(correct_guess[img_num] == 0):
        true[0] = 1
    elif(correct_guess[img_num] == 1):
        true[1] = 1
    elif(correct_guess[img_num] == 2):
        true[2] = 1
    elif(correct_guess[img_num] == 3):
        true[3] = 1
    elif(correct_guess[img_num] == 4):
        true[4] = 1
    elif(correct_guess[img_num] == 5):
        true[5] = 1
    elif(correct_guess[img_num] == 6):
        true[6] = 1
    elif(correct_guess[img_num] == 7):
        true[7] = 1
    elif(correct_guess[img_num] == 8):
        true[8] = 1
    elif(correct_guess[img_num] == 9):
        true[9] = 1
        
    
    
    i = 0
    for i in range(len(true)):
        error[i] = ((prediction[i] - true[i]) ** 2)
        delta[i] = prediction[i] - true[i]
    
    weight_deltas = p.outer_product(delta,inputs)
    #print(len(weight_deltas))

    i = 0
    j = 0
    
    for i in range(len(weights)):
        for j in range (len(weights[0])):
            weights[i][j] -= alpha * weight_deltas[i][j]
    #moving the the next image
    img_num += 1
    
    #print(weights)
# plt.imshow(train_images[0], cmap=cm.Greys)
# plt.title(train_labels[0])
# plt.grid()
# plt.show()
# 
# 