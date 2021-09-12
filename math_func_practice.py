# mathematical functions practice
# hello from vim
import numpy as np

vec_a = [1,2,3,4]
vec_b = [1,2,3,4]

def outer_product(vec_a, vec_b):
    
    out = np.zeros((len(vec_a),len(vec_b)))
    print(out)
    i = 0
    j = 0
    for i in range(len(vec_a)):
        for j in range(len(vec_b)):
            out[i][j] = vec_a[i] * vec_b[j]
    print(out)
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


# print(vector_average(vec_a))
