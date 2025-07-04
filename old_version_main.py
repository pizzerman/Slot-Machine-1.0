import random

MAX_LINES = 3

# VARIABLES

icons = ['heart','apple','seven','peach','bomb','coin']

# FUNCTIONS

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("There was some problem, please try again and check the data you type. (It must be a number)")
    return amount
    
def get_numb_of_lines():
    while True:
        lines = input("Enter the number of lines you want to play on: ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("You must choose between 1-3")
        else:
            print("There was some problem, please try again and check the data you type. (It must be a number)")
    return lines

def slot_machine(lines):
    icon_list = []
    for i in range(1, (lines * 3)+1):
        y = random.choice(icons)
        icon_list.append(y)
    return icon_list

def main():
    multiplier = 0
    user_balance = deposit()
    print(f'You have ${user_balance}')
    
    user_lines = get_numb_of_lines()
    print(f'You want to play on {user_lines} lines.')
    
    result = slot_machine(user_lines)
    result_length = len(result)
    
    if result_length == 1:
        print(f'|{result[0]}|')
        print(f'|{result[1]}|')
        print(f'|{result[2]}|')


        
    elif result_length == 2:
        print(f'|{result[0]}|{result[1]}|')
        print(f'|{result[2]}|{result[3]}|')
        print(f'|{result[4]}|{result[5]}|')
        

    else:
        print(f'|{result[0]}|{result[1]}|{result[2]}|')
        print(f'|{result[3]}|{result[4]}|{result[5]}|')
        print(f'|{result[6]}|{result[7]}|{result[8]}|')
        
        for i in range(0,3):
            if result[i] == result[i+3] == result[i+6]:
                multiplier += 15
        for i in range(0,7,3):
            if result[i] == result[i+1] == result[i+2]:
                multiplier += 15
                
        if result[0] == result[0+4] == result[0+8]:
            multiplier += 10
        if result[2] == result[2+2] == result[2+4]:
            multiplier += 10
            
        if result[2] == result[2+2] == result[2+4] == result[0] == result[0+4] == result[0+8]:
            multiplier += 25

        bigwin = len(set(result)) == 1
        if bigwin:
            multiplier += 100
    
        user_balance *= multiplier
        
            
        print(f'Your multiplier: {multiplier}')
        print(f'Your have won: ${user_balance}')
        
            
main()

play_again = input(f'Do you want to play again?(y/n): ').lower()
if play_again == 'y':
    main()