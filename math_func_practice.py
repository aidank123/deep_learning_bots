# mathematical functions practice
vec_a = [1,2,3,4]
vec_b = [1,2,3]

def elementwise_multiplication(vec_a, vec_b):
    
    try:
        
        assert(len(vec_a) == len(vec_b))    
        output = []
        i = 0
    
        for i in range (len(vec_a)):
        
            output.append(vec_a[i] * vec_b[i])
        
        return output
    
    except AssertionError:
        
            print("oops those lists are not the same length.")
            

output = []

output = elementwise_multiplication(vec_a, vec_b)

for el in output:
    print(el)