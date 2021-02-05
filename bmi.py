# terminal program to take user input, calculate and display BMI
# inputs user height in cms, user weight in kg
# outputs height, metres, weight in kgs, bmi 
# author glen gardiner

# print new blank line
print("\n")

# display message to user
print("We need some details to calculate:)")

# print new blank line
print("\n")

# get user height in cms
user_height_cms = float(input("Emter your height in cms: "))

# convert cms to metres
user_height_metres = user_height_cms / 100

# print height in metres
print("Height: " + str(user_height_metres))

# get user weight in kgs
user_weight = float(input("Enter your weight in kg: "))

# print user weight
print("Weight: " + str(user_weight))

# calculate bmi as userweight divided by height in metres squared
bmi = (user_weight / (user_height_metres ** 2))
abs_bmi = abs((user_weight / (user_height_metres ** 2)))

# print bnew lank line
print("\n")

# print bmi message, print with string function after round to 2 decimal places
#print("Your BMI is : " + str(round(bmi, 2)))
print("Your BMI is : " + str(abs_bmi))

