
# while true: makes it keep going
while True:
# import random: generate random numbers
    import random
# print: is what i want to display
    print ("DICE ROLL SIMULATOR")
    print ("press enter")
# cmd: what you want the computer to do after you press those keys.
    cmd = raw_input ("Enter to run, e to quit")
# number=random.randint: chose random number between 1,6.
    number=random.randint(1,6)
# if number 1 is picked you should be able to see the figure at the bottom
    if number==1:
        print("[----------]")
        print("[          ]")
        print("[     O    ]")
        print("[          ]")
        print("[----------]")
    if number==2:
        print("[----------]")
        print("[          ]")
        print("[  O    O  ]")
        print("[          ]")
        print("[----------]")
    if number==3:
        print("[----------]")
        print("[  O       ]")
        print("[    O     ]")
        print("[       O  ]")
        print("[----------]")
    if number==4:
        print("[----------]")
        print("[   O   O  ]")
        print("[          ]")
        print("[   O   O  ]")
        print("[----------]")
    if number==5:
        print("[----------]")
        print("[  O    O  ]")
        print("[     O    ]")
        print("[  O     O ]")
        print("[----------]")
    if number==6:
        print("[----------]")
        print("[   O   O  ]")
        print("[   O   O  ]")
        print("[   O   O  ]")
        print("[----------]")
