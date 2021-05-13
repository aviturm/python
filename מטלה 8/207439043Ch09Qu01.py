#note - Idan Roth (PhD) authorised usage of functions that were not in class yet.
# Ohad Ezer - 207439043
# Aviad Turm - 312556491

def ask_and_check_input():

    # Set a Boolean flag
    valid_number = 1

    # check if input is int and in size of 9 digits.
    while valid_number:
        print("please enter your ID number, if the number shorter then 9 digits - add zero(s) from left : ")
        user_id = input()

        try:
            val = int(user_id)
            #create a list from the input and check the size
            user_id_list = [int(x) for x in str(user_id)]
            if len(user_id_list) ==9:
                valid_number = 0
            else:print("That's not a 9 digits int!, try againg")

        except ValueError:
            print("That's not an int!, try againg")

    return user_id_list
    

def check_id(user_id_list):
    # create control lists
    control_list = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    temp_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]


    for x in range(9):
        # insert multiplication result into list
        temp_num = user_id_list[x] * control_list[x]
        temp_list[x] = temp_num

        # create list for evrey element in the multiplication result list
        add_num_list = [int(y) for y in str(temp_num)]
        temp_size =len(add_num_list)

        # Add the result of the addition of all elements to the result list
        result_num = 0
        for k in range(temp_size):
            result_num = (result_num + add_num_list[k])
        result_list[x] = result_num

    return result_list

def checkSum_and_print_result(result_list):
   # Calculate the sum and check whether it is divisible by 10 with no remainder
    sum=0
    for x in range(9):
        sum = (sum + result_list[x])
    if (sum %10) == 0 :
            print("ID is ok")
    else: print("ID is not valid")


def main():
    user_id_list = ask_and_check_input()
    result_list = check_id(user_id_list)
    checkSum_and_print_result(result_list)
    input("press any key for exit:")


main()





   


