# Source of this Code: https://github.com/mosh-hamedani/python-projects-for-beginners

import random

times_to_play = int(input("How many times do you want to play?"))
roll_count = 0

for i in range(times_to_play):
    choice = input('Roll the Dice? (y/n): ').lower()
    
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_count += 1
        print(f'({die1}, {die2})')        #f'({}, {})'
        print("Roll Count: ", roll_count)
        
    elif choice == 'n':
        print("Thanks for Playing!")
        break
    
    else: print('Invalid Choice!')

        
        