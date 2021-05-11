import matplotlib.pyplot as plt

# Ohad Ezer - 207439043
# Aviad Turm - 312556491
FAMILY_MEMBERS = 5


def get_input(sibling_number):
    weight = -1
    while weight < 2 or weight > 560:
        try:
            weight = int(input("please enter the weight for sibling number {}: ".format(sibling_number)))
            if weight < 2 or weight > 560:
                print("Oops!  That was no valid weight.  Try again...")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return weight


def create_weights_list(list_length):
    my_list = [0] * list_length
    for number in range(len(my_list)):
        my_list[number] = get_input(number + 1)
    return my_list


def create_nested_list(family_members):
    my_list = [0, 0]
    for x in range(len(my_list)):
        if x == 0:
            print("please enter the weights for the family in the beginning:")
        if x == 1:
            print("please enter the weights for the family in the end:")
        my_list[x] = create_weights_list(family_members)
    return my_list


def calculate_family_weight(my_list):
    total_weight = 0
    for x in my_list:
        total_weight += x


def calculate_change_for_sibling(my_list, sibling_number):
    return my_list[0][sibling_number] - my_list[1][sibling_number]


def calculate_biggest_weight(my_list):
    max_weight = -1
    sibling_index = -1
    for x in range(len(my_list)):
        if my_list[x] > max_weight:
            max_weight = my_list[x]
            sibling_index = x
    return max_weight, sibling_index


def main():
    family_list = create_nested_list(FAMILY_MEMBERS)
    print("family total weight in the beginning was", calculate_family_weight(family_list[0]))
    print("family total weight in the end is", calculate_family_weight(family_list[1]))
    weight_lost = [0] * FAMILY_MEMBERS
    for sibling_number in range(FAMILY_MEMBERS):
        change = calculate_change_for_sibling(family_list, sibling_number)
        weight_lost[sibling_number] = change
        print("the weight change for sibling", sibling_number, "is", change)
    max_beginning_weight = calculate_biggest_weight(family_list[0])
    max_end_weight = calculate_biggest_weight(family_list[1])
    print("the max weight in the beginning was", max_beginning_weight[0], "and belong to sibling number",
          max_beginning_weight[1] + 1)
    print("the max weight in the end was", max_end_weight[0], "and belong to sibling number",
          max_end_weight[1] + 1)
    create_pie_chart(weight_lost)


# this part is question 2
def create_pie_chart(weight_lost):
    slice_labels = [""] * FAMILY_MEMBERS
    for sibling in range(len(slice_labels)):
        slice_labels[sibling] = "family member number: " + str(sibling + 1)
    try:
        plt.pie(weight_lost, labels=slice_labels, labeldistance=0.9, shadow=True)
    except ValueError:
        print("there is something wring here. seems like some of the family members gain weight during the diet")
    else:
        plt.title('weight lost per family member')
        plt.show()


main()
