import getpass

PersonA_win = 0
PersonB_win = 0
Aiko = 0
Hands = [0,1,2]

while True:
    while True:
        PersonA = int(getpass.getpass(prompt="Tomo, please choose your hand\n0 is scissors, 1 is rock, 2 is paper\n"))
        if PersonA in Hands:
            break
        else:
            print("You did not choose a valid hand! Please input your hand again!\n")
    while True:
        PersonB = int(getpass.getpass(prompt="Hana, please choose your hand\n0 is scissors, 1 is rock, 2 is paper\n"))
        if PersonB in Hands:
            break
        else:
            print("You did not choose a valid hand! Please input your hand again!\n")
    if PersonA == 0:
        print("Tomo played scissors\n")
    elif PersonA == 1:
        print("Tomo played rock\n")
    elif PersonA == 2:
        print('Tomo played paper\n')
    
    if PersonB == 0:
        print("Hana played scissors\n")
    elif PersonB == 1:
        print("Hana played rock\n")
    elif PersonB == 2:
        print("Hana played paper\n")
    
    
    if PersonA == PersonB:
        print("Oh, it was Aiko")
        Aiko += 1
    elif (PersonA - PersonB)%3 == 1:
        print("Tomo won")
        PersonA_win += 1
    else:
        print("Hana won")
        PersonB_win += 1
    
    cont = input("Do you want to continue the game?[y/n]\n")
    if cont == "n":
        break
    
print("Tomo won %d times\n" % PersonA_win)
print("Hana won %d times\n" % PersonB_win)
print("Aiko %d times\n" % Aiko )
print("Tomo v.s. Hana\n %d : %d" % (PersonA_win/(PersonA_win+PersonB_win)*100, PersonB_win/(PersonA_win+PersonB_win)*100))
