# Ohad Ezer - 207439043
# Aviad Turm - 312556491

#get a number from the user.
num =int(input('please enter number from 0 to 10: '))

#check if it is a valid number, if not kepp asking a valid number.
while num>10 or num<0:
    num =int(input('please enter a valid number, (0 to 10): '))
i = num

for i in range(1,i+1):
    for num in range(1,num+1):
          print ((num) * i,end ="\t")    
    print ('\n')
