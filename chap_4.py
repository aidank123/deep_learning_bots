#Chapter 4 main

# knob_weight = 0.5
# input = 0.5
# goal_pred = 0.8
# 
# pred = input * knob_weight
# 
# error = (pred - goal_pred) ** 2
# print(error)

# weight = 0.5
# input = 0.5
# goal_prediction = 0.8
# step_amount = 0.001

#PREDICTING A NUMBER USING HOT AND COLD CORRECTIONS

# for iteration in range(1101):
#     
#     prediction = input * weight
#     error = (prediction - goal_prediction) ** 2
#     
#     print("Error:" + str(error) + " Prediction:" + str(prediction))
#     
#     up_prediction = input * (weight + step_amount)
#     up_error = (goal_prediction - up_prediction) ** 2
#     
#     down_prediction = input * (weight - step_amount)
#     down_error = (goal_prediction - down_prediction) ** 2
#     
#     if(down_error < up_error):
#         weight = weight - step_amount
#         
#     elif(down_error > up_error):
#         weight = weight + step_amount

#PREDICTION OF NUMBER USING GRADIENT DESCENT
# for iteration in range(20):
#     
#     prediction = input * weight
#     error = (prediction - goal_prediction) ** 2
#     direction_and_amount = (prediction - goal_prediction) * input
#     weight = weight - direction_and_amount
#     
#     print("Direction and amount:", direction_and_amount)
#     print("Weight:", weight)
#     print("Error:" + str(error) + " Prediction:" + str(prediction))
#     
  
#EXAMPLE FROM pgs 58-59
# 
# weight = 0.1
# alpha = .01
# 
# def neural_network(input,weight):
#     prediction = input * weight
#     return prediction
# 
# number_of_toes = [8.5]
# win_or_lose_binary = [1]
# 
# input = number_of_toes[0]
# goal_prediction = win_or_lose_binary[0]
# 
# prediction = neural_network(input,weight)
# 
# error = (goal_prediction - prediction) ** 2
# 
# delta = prediction - goal_prediction
# weight_delta = input * delta
# alpha = .01
# 
# weight -= weight_delta * alpha

#PREDICTION OF NUMBER USING GRADIENT DESCENT + DELTA

# weight, goal_pred, input = (0.0, 0.8, 0.5)
# 
# for iteration in range(20):
#     
#     pred = input * weight
#     error = (pred - goal_pred) ** 2
#     delta = pred - goal_pred
#     weight_delta = delta * input
#     weight = weight - weight_delta
#     print("Error:" + str(error) + " Prediction:" + str(pred))

#MY OWN MINI NEURAL NETWORK USING ALPHA AND DELTA

weight, goal, input = (10, 1000, 50)
alpha = .0001
for iteration in range(100):
    
    prediction = weight * input
    
    error = (prediction - goal) ** 2

    delta = prediction - goal

    weight_delta = delta * input

    weight = weight - (weight_delta * alpha)
    
    print('Error:', error, 'Prediction:', prediction)
    

    



