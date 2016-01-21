#This progrmam will simulate a dice

# allow the to receive strins from the user
import string
#Allows you to exit the program
from sys import exit
# impolrt random: generate random numbers.
from random import randint


# It will run the dice
def runDice():
    # number=random.randint: chose random number between 1,6.
    number=randint(1,6)

    # if number 1 or any other numer is picked you should be able to see the figure at the bottom.
    if number==1:
        print("[----------]")
        print("[          ]")
        print("[     O    ]")
        print("[          ]")
        print("[----------]")
    elif number==2:
        print("[----------]")
        print("[          ]")
        print("[  O    O  ]")
        print("[          ]")
        print("[----------]")
    elif number==3:
        print("[----------]")
        print("[  O       ]")
        print("[    O     ]")
        print("[       O  ]")
        print("[----------]")
    elif number==4:
        print("[----------]")
        print("[   O   O  ]")
        print("[          ]")
        print("[   O   O  ]")
        print("[----------]")
    elif number==5:
        print("[----------]")
        print("[  O    O  ]")
        print("[     O    ]")
        print("[  O     O ]")
        print("[----------]")
    elif number==6:
        print("[----------]")
        print("[   O   O  ]")
        print("[   O   O  ]")
        print("[   O   O  ]")
        print("[----------]")
    else:
        sys.exit()

def runProgram():
#This is what the user will see. if the user type y the dice will roll or the user type n the simulator will exit
    print "Run the program? [y/n]\n:"
    cmd = raw_input()
    if cmd == "n":
        print "Bye"
        exit()
    elif cmd =='y':
        runDice()
    else:
        runProgram()

#while true: makes it keep rolling the dice.
while True:
# print: is what i want to display for the user to see
    print ("DICE ROLL SIMULATOR")
    runProgram()
