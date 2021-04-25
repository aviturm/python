# Ohad Ezer - 207439043
# Aviad Turm - 312556491
import os

MAX_MKS = 120


def votes_recording():
    # count to make sure not to exceese max MK posible
    vote_counter = 0
    # open the file
    votes_recordings = open('votes_recordings.txt', 'w')
    another = 'y'
    while another == 'y' or another == 'Y':
        # get and validate name. must be full name, first and last name, with space between
        name = input("please enter the MK's full name: ")
        while len(name) < 5 or name.find(" ") == -1:
            name = input("wrong input. please try again. make sure to write full name\n" +
                         "please enter the MK's full name: ")
        # get and validate vote
        vote = input("please vote: 1 for in favor, 2 for against, or 3 for abstained ")
        while vote != '1' and vote != '2' and vote != '3':
            vote = input("wrong input. please try again\n" +
                         "please vote: 1 for in favor, 2 for against, or 3 for abstained ")
        vote = int(vote)
        vote_counter += 1
        # add vote to file
        votes_recordings.write(name + '\n')
        votes_recordings.write(str(vote) + '\n')
        # check to see if reached max
        if vote_counter == MAX_MKS:
            print("you have riched the max MKs posible")
            another = 'oh god please dont'
        # if no maxed - ask if want to add another
        else:
            print('Do you want to add another record?')
            another = input('Y = yes, anything else = no: ')
    votes_recordings.close()
    print('Data appended to votes_recordings.txt')


def votes_summarize():
    # set vriables
    in_favor = 0
    against = 0
    abstained = 0
    # open and read file
    votes_recordings = open('votes_recordings.txt', 'r')
    name = votes_recordings.readline()
    while name != '':
        # add the vote to the counter
        vote = int(votes_recordings.readline())
        if vote == 1:
            in_favor += 1
        if vote == 2:
            against += 1
        else:
            abstained += 1
        name = votes_recordings.readline()
    votes_recordings.close()
    # write the summery to a file
    vote_summery = open('votes_summery.txt', 'w')
    vote_summery.write(str(in_favor) + '\n')
    vote_summery.write(str(against) + '\n')
    vote_summery.write(str(abstained) + '\n')
    print("votes were summerized and were writen to votes_summery.txt successfully")


def desicion_calculate():
    # open and read the summery
    vote_summery = open('votes_summery.txt', 'r')
    in_favor = int(vote_summery.readline())
    against = int(vote_summery.readline())
    abstained = int(vote_summery.readline())
    # check the resolt and pront it
    if in_favor > against:
        print("we have majority of MKs in favor. we have a coalition. yay.")
    else:
        print("oh no, it looks like we are goint to elections. again.")


def main():
    votes_recording()
    votes_summarize()
    desicion_calculate()


main()
