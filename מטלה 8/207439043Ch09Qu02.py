#note - Idan Roth (PhD) authorised usage of functions that were not in class yet.
# Ohad Ezer - 207439043
# Aviad Turm - 312556491


def ask_for_students_num():
    # Set a Boolean flag
    valid_number = 1
    # check if number of students is  above 0 and is an int
    while valid_number:
         number_of_students = input("how many students are in this class? : ")
         try:
           val = int(number_of_students)
           number_of_students = int(number_of_students)
           if number_of_students>=1:
             valid_number = 0
           else:print("number must be positive, try againg")
         except ValueError:
           print("That's not an int!, try againg")

    return number_of_students


def ask_for_grades(number_of_students):
    grades_list = []
    for x in range(number_of_students):
        # Set a Boolean flag
        valid_number = 1
        # check if grade is in range and is an int
        while valid_number:
            grade = input("please enter the grade:")
            try:
                val = int(grade)
                grade = int(grade)
                if grade>0 and grade<=100:
                    valid_number = 0
                else:print("grade out of range, try again") 

            except ValueError:
                print("That's not an int!, try againg")
            
        grades_list.append(grade)
    return grades_list

# This function calculates the average grade
def calc_average(grades_list):
    sum = 0
    counter = 0
    average = 0
    for x in range(len(grades_list)):
        sum = sum+grades_list[x]
        counter = counter+1
    average = (sum/counter)
    return average


def range_grade(grades_list):
    #ask for printing index

    valid_number = 1
    while valid_number:
        index_i = input("please enter the first index: ")
        try:
            val = int(index_i)
            index_i = int(index_i)
            valid_number = 0
        except ValueError:
                print("That's not an int!, try againg")

    valid_number = 1
    while valid_number:
        index_j = input("please enter the seconde index: ")
        try:
            val = int(index_j)
            index_j = int(index_j)
            valid_number = 0
        except ValueError:
                print("That's not an int!, try againg")

    index_i = index_i-1
    if index_i<index_j:
        # List Slicing
        range = grades_list[index_i:index_j]
        print ("the grades before factor is:")
        print(range)
    else:
        # List Slicing
        temp_list = grades_list[index_j-1:index_i+1]
        print ("the grades before factor is:")
        print ([x for x in temp_list[::-1]])
        

def calc_grade(grades_list):
    # call a function calculates the average grade
    average = calc_average(grades_list)
    if average<70:
        # calculates the factor
        factor = 70-average
        for x in range(len(grades_list)):
            # if after adding the factor the grade is still not out of range, add factor. else - grade will be 100
            if (grades_list[x]+factor) <= 100:
                grades_list[x] = grades_list[x] + factor
            else:
                 grades_list[x] =100
    print("the grades after factor is:")
    print(grades_list)
    return grades_list
    

def main():
  number_of_students = ask_for_students_num()
  grades_list = ask_for_grades(number_of_students)
  average = calc_average(grades_list)
  range_grade(grades_list)
  calc_grade(grades_list)
  input("press any key for exit:")


main()