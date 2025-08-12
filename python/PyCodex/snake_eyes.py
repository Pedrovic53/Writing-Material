import random

while True:
    die1 = random.randint(1,6) 
    die2 = random.randint(1,6)

    num_rolls = 0
    total = die1 + die2

    if total != 2:
        print ("Nope:🎲 " + str(die1) +",🎲 " + str(die2))
        num_rolls = num_rolls + 1
    else:
        print('Snake Eyes!')
        break
