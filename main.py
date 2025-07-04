import random

MAX_LINES = 3
icons = ['heart', 'apple', 'seven', 'peach', 'bomb', 'coin']

# FUNCTIONS

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")


def get_numb_of_lines():
    while True:
        lines = input("Enter the number of lines you want to play on (1–3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Choose between 1 and 3 lines.")
        else:
            print("Please enter a number.")


def get_bet(user_balance):
    while True:
        bet = input(f'How much would you like to bet? (Balance: ${user_balance}) $')
        if bet.isdigit():
            bet = int(bet)
            if 0 < bet <= user_balance:
                return bet
            else:
                print(f'Bet must be between $1 and your balance (${user_balance}).')
        else:
            print('Please enter a valid number.')


def slot_machine():
    result = []
    for i in range(3):  # 3 rows
        row = [random.choice(icons) for i in range(3)]  # 3 columns
        result.extend(row)
    return result


def display_slots(result):
    print("----------SLOTS----------")
    for i in range(0, 9, 3):
        print("| {:<6}| {:<6}| {:<6}|".format(
            result[i], result[i+1], result[i+2]
        ))
    print("-------------------------")


def check_winnings(result, lines):
    multiplier = 0

    # HORIZONTAL
    for i in range(lines):
        row_start = i * 3
        if result[row_start] == result[row_start + 1] == result[row_start + 2]:
            multiplier += 15

    if lines == 3:
        # VERTICAL
        for i in range(3):
            if result[i] == result[i + 3] == result[i + 6]:
                multiplier += 15

        # DIAGONALS
        if result[0] == result[4] == result[8]:
            multiplier += 10
        if result[2] == result[4] == result[6]:
            multiplier += 10

        # JACKPOTS
        if len(set(result)) == 1:
            multiplier += 100
        elif result[0] == result[4] == result[8] and result[2] == result[4] == result[6]:
            multiplier += 25

    return multiplier


def main():
    global user_balance

    user_lines = get_numb_of_lines()
    user_bet = get_bet(user_balance)

    result = slot_machine()
    display_slots(result)

    multiplier = check_winnings(result, user_lines)
    winnings = user_bet * multiplier

    if multiplier != 0:
        user_balance += winnings
        print(f'🎉 Your multiplier: {multiplier}')
        print(f'🎉 You have won: ${winnings}')
    else:
        user_balance -= user_bet
        print(f'❌ You lost your bet of ${user_bet}.')

    print(f'💰 Your actual balance: ${user_balance}')


# GAME LOOP
user_balance = deposit()

while True:
    if user_balance == 0:
        print('You have lost all your money. Game over!')
        break

    main()

    if user_balance == 0:
        print('You have lost all your money. Game over!')
        break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
