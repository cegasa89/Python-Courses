import random
from string import ascii_lowercase
import hangmanDrawwed





def hangman():
    word = random.choice(["lion", "cow", "elephant", "fox", "tiger", "rabbit"])
    turns = 10
    guessmade = ''
    
    while len(word) > 0:
        main = ""
        missed = 0
        
        for letter in word:
            
            if letter in guessmade:
                main += letter
            else:
                main += "_" + ""
                
        if main == word:
            print(main)
            print("You won.")
            break
        print("Guess the word: ", main)
        guess = input()
        
        if guess in ascii_lowercase:
            guessmade += guess
        else:
            print("Enter a valid character. ")
            guess = input()
            
        if guess not in word:
            turns -= 1
            hangmanDrawwed.figure(turns)
            print()
            if turns == 0:
                break
            

if __name__ == "__main__":
    name = input("Enter your name: ")
    print("Welcome ", name)
    print("-----------------------------")
    print("Try to guess the word  in less than 10 trys.")
    hangman()
    print()
