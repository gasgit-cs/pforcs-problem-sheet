# terminal program to take user input, calculate and display BMI
# inputs user height in cms, user weight in kg
# outputs height, metres, weight in kgs, bmi 
# author glen gardiner

###################################################################################
# v1
# print new blank line
# print("\n")

# # display message to user
# print("We need some details to calculate:)")

# # print new blank line
# print("\n")

# # get user height in cms
# user_height_cms = float(input("Emter your height cms: "))

# # convert cms to metres
# user_height_metres = user_height_cms / 100

# # print height in metres
# print("Height: " + str(user_height_metres))

# # get user weight in kgs
# user_weight = float(input("Enter your weight kg: "))

# # print user weight
# print("Weight: " + str(user_weight))

# # calculate bmi as userweight divided by height in metres squared
# bmi = (user_weight / (user_height_metres ** 2))
# abs_bmi = abs((user_weight / (user_height_metres ** 2)))

# # print bnew lank line
# print("\n")

# # print bmi message, print with string function after round to 2 decimal places
# #print("Your BMI is : " + str(round(bmi, 2)))
# print("Your BMI is : " + str(abs_bmi))

##################################################################################

# v2 complete program with main and functions

def get_height():
    
    # print new blank line
    print("\n")

    # display message to user
    print("We need some details to calculate:)")

    # print new blank line
    print("\n")

    # get user height in cms
    # uhcms -
    # uhm
    user_height_cms = float(input("Enter your height cms: "))

    # convert cms to metres
    user_height_metres = user_height_cms / 100

    # print height in metres
    print("Height: " + str(user_height_metres))

    # return height in metres
    return user_height_metres

    # uw - user weight
def get_weight():

    # get user weight in cms
    user_weight = float(input("Enter your weight kg: "))
    # print user weight
    print("Weight: " + str(user_weight))
    # return user weight
    return user_weight

# function to calculate the bmi, take 2 args user weigh & user height in metres
def calculate(user_weight, user_height_metres):

    # calculate bmi user weight kg divided by height m2
    bmi = (user_weight / (user_height_metres ** 2))
    # return bm1
    return bmi

# function to display bmi, accepts 1 args bmi
def display(bmi):

    # print message and bmi
    print("Your BMI is : " + str(bmi))

# main method for program, call other functions as required
def main():
    
    x = get_height()
    y = get_weight()
    b = calculate(y, x)
    display(b)

# conditional block to check if the script contains a main function, running while True
if __name__ == "__main__":
    main()

