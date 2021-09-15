# mathematical functions practice
# hello from vim
import numpy as np

vec_a = [1,2,3,4]
vec_b = [1,2,3,4]

def outer_product(vec_a, vec_b):
    
    out = np.zeros((len(vec_a),len(vec_b)))
    #print(out)
    i = 0
    j = 0
    for i in range(len(vec_a)):
        for j in range(len(vec_b)):
            out[i][j] = vec_a[i] * vec_b[j]
    #print(out)
    return out

def vect_matrix_multiplication(vect, matrix):
    
    output = []
    t = 0
    for t in range(10):
        output.append(0)
        
    h = 0
    for h in range(len(matrix)):
        output[h] = weighted_sum(vect,matrix[h])
    return output
        
def elementwise_multiplication(vec_a, vec_b):
    
    try:    
        assert(len(vec_a) == len(vec_b))    
        output = []
        i = 0
        for i in range (len(vec_a)):
            output.append(vec_a[i] * vec_b[i])
        return output
    except AssertionError:
            print("Those lists are not the same length!")
    
def elementwise_addition(vec_a, vec_b):
    
    try:    
        assert(len(vec_a) == len(vec_b))    
        output = []
        i = 0
        for i in range (len(vec_a)):
            output.append(vec_a[i] + vec_b[i])
        return output
    except AssertionError:
            print("Those lists are not the same length!")
         
def vector_sum(vec_a):
    
    total = 0
    for elements in vec_a:
        total = total + elements
    return total

def vector_average(vec_a):
    
    total = 0
    for elements in vec_a:
        total = total + elements
    return total/len(vec_a)

def weighted_sum(a,b):
    
    c = elementwise_multiplication(a,b)
    return vector_sum(c)

#method will turn the prediction values into a guess, 0 - 1 (percentage)

def percenter(input):
    
    output = [0,0,0,0,0,0,0,0,0,0]
    total = vector_sum(input)
    
    i = 0
    for i in range(len(input)):
        

        output[i] = input[i]/total
        
    return output

#method to choose the top guess choice based on the percents

def chooseNum(input):
    
    i = 0
    choice = 0
    for i in range(len(input)):
        if (input[i] > choice):
            choice = i
            
    return choice


#method to test why weights arent holding correct value
# def weight_holder(wt,i,j):
#     
#     weights = []
#     weight_rows = []
#     i = 0
#     j = 0
#     for j in range(10):
#         i = 0
#         weight_rows.clear()
#         for i in range(784):
#             weight_rows.append(1)
# 
#         weights.append(weight_rows)
#         
#     weights[i][j] = wt


