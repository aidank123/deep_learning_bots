#UPDATES:

#I am having trouble understanding the part where we calculate error and update the weights. Does each input X weight create a prediction (each pixel)
#that will choose 0 - 9 and then you compare that to the correct label for that image and update that weight accordingly? I suppose that makes
#sense but it is a pretty roundabout way of doing things. See if you can get that to work for now.

#How do I get the prediction to choose a number 0 - 9? right now it just returns a vector of length 784, elementwise multiplication of inputs
#and their weights

#I think you need to change the 'correct guesses' vector to be made up of the pixels of the image ur looking at? i am not sure right now. 

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import chap_5_img_reader as m

#importing the math functions module u created
import math_func_practice as p

#neural network function

def neural_network(inputs,weights):
    
    #multiplying each input by each corresponding weight
    
    prediction = p.elementwise_multiplication(inputs,weights)
    return prediction

#calling the reader function and setting vars equal to the data
#ntrimages = number of training images (60,000)
train_images, train_labels, ntrimages, test_images, test_labels, nteimages = m.mnist_read()

x = 0
y = 0

img_num = 0 #what img number we are on
inputs = [] #initializing list of inputs, will be cleared at the start of each new image
alpha = .01 #setting alpha to .01


#initializing the weights, all to 1?
weights = []
i = 0
for i in range(784):
    weights.append(1)
    
#initializing list of correct guesses
correct_guess = []
i = 0
for i in range(784):
    correct_guess.append(train_labels[i])
    
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
    for i in range(len(inputs)):
        error.append(0)
    
    #initializing delta vector, vector of 0's
    delta = []
    i = 0
    for i in range(len(inputs)):
        delta.append(0)
        
    i = 0
    for i in range(len(correct_guess)):
        error[i] = ((prediction[i] - correct_guess[i]) ** 2)
        delta[i] = prediction[i] - correct_guess[i]
    
    #moving the the next image
    img_num += 1

# plt.imshow(train_images[0], cmap=cm.Greys)
# plt.title(train_labels[0])
# plt.grid()
# plt.show()
# 
# 