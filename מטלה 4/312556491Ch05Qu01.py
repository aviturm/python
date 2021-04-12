#note - Idan Roth (PhD) authorised usage of functions that were not in class yet, such as lists
# Ohad Ezer - 207439043
# Aviad Turm - 312556491

BLOCK_FACTOR = 0.0325
NUMBER_OF_PARTIES = 5

def main():
    paries = get_and_check_input()
    parties_mandats = calculate_mandats_per_party(paries)

# getting input from the user
def get_and_check_input():
    parties = []
    for x in range(NUMBER_OF_PARTIES):
        parties.append(0)

    for x in range(len(parties)):
        print("please enter the number of valid votes for party number",x+1)
        input_num = input()
        while(not(input_num.isdigit())):
            print("error - invalid input. please enter the number of valid votes for party number", x + 1)
            input_num = input()
        parties[x] = int(input_num)
    return parties

# calculating the total valit votes
def calculate_mandats_per_party(parties):
    valid_votes = sum(parties)
    # calculating the voted that are the block number, and votes to mandat
    block_votes = valid_votes*BLOCK_FACTOR
    for x in range(NUMBER_OF_PARTIES):
        if(parties[x]<block_votes):
            parties[x] = 0

    valid_votes = sum(parties)
    mandat = valid_votes//120
    # determing the number of mandats per party
    parties_mandats = []
    for x in range(NUMBER_OF_PARTIES):
        parties_mandats.append(0)

    if mandat == 0:
        print("error - mandat value is 0")
    else:
        for x in range(NUMBER_OF_PARTIES):
            parties_mandats[x] = parties[x] // mandat
    for x in range(NUMBER_OF_PARTIES):
        print("the number of mandats for party number", x+1, "is:", format(parties_mandats[x], '.0f'))
    return parties_mandats

main()