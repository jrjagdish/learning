# import random
# def spin_row():
#     symbols = ['🍒','🌸','🍉','🫠']
#     return [random.choice(symbols) for symbol in range(3)]    

# def print_row(row):
#     print("****************")
#     print(" | ".join(row))
#     print("****************")

# def get_payout(row,bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet * 3
#         elif row[0] == '🍉':
#             return bet * 4
#         elif row[0] == '🫠':
#             return bet * 5
#         elif row[0] == '🌸':
#             return bet * 6 
#     return 0    
        
   

# def main():
#     balance = 100

#     print("  Welcome to the Game  ")
#     print("  Symbols:🍒🌸🍉🫠 ")
#     print("****************************")

#     while balance > 0 :
#         print(f"current balance: ${balance}")

#         bet = input("put your bet amount: ")

#         if not bet.isdigit():
#             print("invalid number")
#             continue

#         bet = int(bet)

#         if bet>balance:
#             print("insufficient balance")    
#             continue

#         if bet<=0:
#             print("must be greater than zero")
#             continue

#         balance -=bet

#         row = spin_row()
#         print("Spinnig......\n")
#         print_row(row)

#         payout = get_payout(row,bet)

#         if payout>0:
#             print(f"you won ${payout}")
#         else:
#             print("Sorry you lost this round")  

#         balance += payout   

#         play_again = input("Do you want to play again? (Y/N): ")

#         if play_again.lower() != 'y':
#             break 

#     print(f"Game over Your Balance is ${balance}")         

       


# if __name__ == '__main__':
#     main()

import random

words = ("apple" , "orange" , "banana" , "coconut")
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   ",),
               2:(" o ",
                  " | ",
                  "   ",),
               3:(" o ",
                  "/| ",
                  "   ",),
               4:(" o ",
                  "/|\\",
                  "   ",),
               5:(" o ",
                  "/|\\",
                  "/  ",),
               6:(" o ",
                  "/|\\",
                  "/ \\",),            
                         }

def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guess = 0
    guess_letters = set()
    is_runnig = True

    while is_runnig:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() :
            print("Invalid input")
            continue

        if guess in guess_letters:
            print(f"{guess} Alredy guessed")
            continue

        guess_letters.add(guess)



        if guess in answer:
           for i in range(len(answer)):
                if answer[i] == guess:
                   hint[i] = guess
        else:
            wrong_guess +=1    

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)  
            print("YOU WIN")
            is_runnig = False     
        elif wrong_guess>= len(hangman_art) -1 :
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU LOSE") 
            is_runnig =False      
                   



if __name__ == '__main__':
    main()