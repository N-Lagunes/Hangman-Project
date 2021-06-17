import random as rd
import os
import platform
import time

def getFileLen(fileLen = 0):
    with open("words.txt","r",encoding="UTF-8") as file:    
        for _ in file:
            fileLen+=1
    return fileLen


def getWord():
    rdIndex,i, = rd.randint(0,getFileLen()), 0
    newStr=''
    with open("words.txt","r",encoding="UTF-8") as file:
        for line in file:
            if i == rdIndex:
                line = list(line)
                line.pop()
                for char in line:
                    newStr += char
                return newStr.upper()
            i+=1 


def getPlatform():
    OpSys = platform.system().upper()
    if OpSys=='LINUX':
        return 'clear'
        
    if OpSys=='WINDOWS':
        return 'cls'


def hangman(word,platform):
    word_completion,tries = "_" * len(word), 6
    guessed,guessed_letters,guessed_words = False, [], []
    print(f''' 
        Let's play hangman!
        {printHangman(tries)}
        {word_completion}

    ''')
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You already guessed the letter {guess}')
            elif guess not in word:
                print(f'{guess} is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Good job {guess} is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # Linear search for letter in word an return a listComp with the indices
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # stops when theres not "_" char any longer, so we've discovered everything
                if "_" not in word_completion:
                    guessed = True
        # the case you already know the entire word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed the word {guess}')
            elif guess != word:
                print(f'{guess} is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess.')
        
        time.sleep(2)
        os.system(platform)
        print(f'''
            {printHangman(tries)}
            {word_completion}
            ''')
        
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def printHangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
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


def run():
    word = getWord()
    platform = getPlatform()
    hangman(word,platform)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = getWord()
        hangman(word,platform)


if __name__ == "__main__":
    run()    