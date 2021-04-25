# Ohad Ezer - 207439043
# Aviad Turm - 312556491
import os


def print_menu():
    #print the menu
    print("please select action:\n" +
          "1 to edit MK's vote\n" +
          "2 to delete NK's vote\n"+
          "99 to exit\n")


def edit_vote():
    #get the name and the new vote + validate
    search = input("please enter the MK's name you wish to edit:\n")
    new_vote = input("please enter the MK's correct vote:" +
                     "1 for in favor, 2 for against, or 3 for abstained ")
    while new_vote != '1' and new_vote != '2' and new_vote != '3':
        new_vote = input("wrong input. please try again\n" +
                         "please vote: 1 for in favor, 2 for against, or 3 for abstained ")
    new_vote = int(new_vote)
    #open the vote recording and search for the name. if found - edit the vote
    votes_recordings = open('votes_recordings.txt', 'r')
    temp_file = open('temp.txt', 'w')
    name = votes_recordings.readline()
    while name != '':
        vote = int(votes_recordings.readline())
        name = name.rstrip('\n')
        if name == search:
            #name found - update the vote
            temp_file.write(search + '\n')
            temp_file.write(str(new_vote) + '\n')
            found = True
        else:
            #name not found - copy the vote as it is
            temp_file.write(name + '\n')
            temp_file.write(str(vote) + '\n')
        name = votes_recordings.readline()
    votes_recordings.close()
    temp_file.close()
    #run over the file with the new one
    os.remove('votes_recordings.txt')
    os.rename('temp.txt', 'votes_recordings.txt')
    if found:
        print('The vote has been updated.')
    else:
        print('That item was not found in the file.')


def delete_vote():
    #get the name to search
    search = input("please enter the MK's name you wish to delete:\n")
    votes_recordings = open('votes_recordings.txt', 'r')
    temp_file = open('temp.txt', 'w')
    name = votes_recordings.readline()
    found = False
    while name != '':
        vote = int(votes_recordings.readline())
        name = name.rstrip('\n')
        if name != search:
            # if not found - copy the vote as it is
            temp_file.write(name + '\n')
            temp_file.write(str(vote) + '\n')
        else:
            #if name found - dont copy it so it will be deleted
            found = True
        name = votes_recordings.readline()
    votes_recordings.close()
    temp_file.close()
    #run over the file
    os.remove('votes_recordings.txt')
    os.rename('temp.txt', 'votes_recordings.txt')
    if found:
        print('The vote has been deleted.')
    else:
        print('That item was not found in the file.')


def votes_summarize():
    in_favor = 0
    against = 0
    abstained = 0
    votes_recordings = open('votes_recordings.txt', 'r')
    name = votes_recordings.readline()
    while name != '':
        vote = votes_recordings.readline()
        vote = int(vote)
        if vote == 1:
            in_favor += 1
        if vote == 2:
            against += 1
        else:
            abstained += 1
        name = votes_recordings.readline()
    votes_recordings.close()
    vote_summery = open('votes_summery.txt', 'w')
    vote_summery.write(str(in_favor) + '\n')
    vote_summery.write(str(against) + '\n')
    vote_summery.write(str(abstained) + '\n')
    print("votes were summerized and were writen to votes_summery.txt successfully")


def desicion_calculate():
    vote_summery = open('votes_summery.txt', 'r')
    in_favor = int(vote_summery.readline())
    against = int(vote_summery.readline())
    abstained = int(vote_summery.readline())
    if in_favor > against:
        print("we have majority of MKs in favor. we have a coalition. yay.")
    else:
        print("oh no, it looks like we are goint to elections. again.")


def main():
    another = 'y'
    #get and validate the choise. call the function
    while(another =='y' or another == 'Y'):
        print_menu()
        action = input()
        while (action != '1' and action != '2' and action != '99'):
            print("error, please select fromn the list:")
            print_menu()
            action = input()
        if (action == '1'):
            edit_vote()
            votes_summarize()
            desicion_calculate()
            print('Do you want to add another record?')
            another = input('Y = yes, anything else = no: ')
        if (action == '2'):
            delete_vote()
            votes_summarize()
            desicion_calculate()
            print('Do you want to add another record?')
            another = input('Y = yes, anything else = no: ')
        if(action == '99'):
            print('bye')
            another = 'oh god please dont'

main()
