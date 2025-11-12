import random
def spin_row():
    symbols = ['🍒','🌸','🍉','🫠']
    return [random.choice(symbols) for symbol in range(3)]    

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🫠':
            return bet * 5
        elif row[0] == '🌸':
            return bet * 6 
    return 0    
        
   

def main():
    balance = 100

    print("  Welcome to the Game  ")
    print("  Symbols:🍒🌸🍉🫠 ")
    print("****************************")

    while balance > 0 :
        print(f"current balance: ${balance}")

        bet = input("put your bet amount: ")

        if not bet.isdigit():
            print("invalid number")
            continue

        bet = int(bet)

        if bet>balance:
            print("insufficient balance")    
            continue

        if bet<=0:
            print("must be greater than zero")
            continue

        balance -=bet

        row = spin_row()
        print("Spinnig......\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout>0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this round")  

        balance += payout   

        play_again = input("Do you want to play again? (Y/N): ")

        if play_again.lower() != 'y':
            break 

    print(f"Game over Your Balance is ${balance}")         

       


if __name__ == '__main__':
    main()