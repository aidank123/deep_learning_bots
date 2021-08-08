# mathematical functions practice
# hello from vim

vec_a = [1,2,3,4]
vec_b = [1,2,3,4]

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
