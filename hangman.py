import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    gussed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print("Lets play Hangman!")
    print(display_hangman(tries))
    print("\n")
    while not gussed and tries > 0:
        guess = input("Please enter a letter or a word  ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Your have already gussed this letter ")
            elif guess not in word:
                print(guess , " is not the word ")
                tries -=1
                guessed_letters.append(guess)
            else:
                print("Goojob. ",guess ," is the word ")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices = [i for i ,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion ="".join(word_as_list)
                if "_" not in word_completion:
                    gussed = True
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
               print("Your have aalready gussed the word ",guess)
            elif guess != word:
                print(guess," is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                gussed = True
                world_completion = word

        else:
            print("Not a valid Word .")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if gussed:
        print("You win")
    else:
        print("You lost the word was "+ word + " Better Luck Next Time")



def display_hangman(tries):
    stages = [ """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                """ ,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                """,
                """
                     --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -
                """ ,
                """
                     --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                """,
                """
                     --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                """,
                """
                     --------
                    |      |
                    |      O
                    |      
                    |      
                    |     
                    -
                """,
                """
                     --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input ("play again? Y/N").upper() == "Y":
        word = get_word()
        play(word)
        
if __name__ == "__main__":
    main()
