import random

states = [
    "goa",
    "gujarat",
    "bihar",
    "assam",
    "punjab",
    "kerala",
    "maharashtra",
    "karnataka",
    "odisha",
    "sikkim",
    "rajasthan",
    "haryana",
    "jharkhand",
    "tripura",
    "manipur",
    "nagaland"
]
let = "abcdefghijklmnopqrstuvwxyz"
word = random.choice(states)
chances = 6
guess_word = "_"*len(word)
print('🔡 HANGMAN 🔡')

print("<<=========xx==========>>")
print("Guess the following State in India")
print(" ", guess_word," ")
while chances !=0:
    guess_letter = input("guess a letter : ").lower()
    if guess_letter in let:
        if guess_letter in word:
            for index in range(len(word)):
                if word[index] == guess_letter:
                    guess_word = guess_word[:index] + guess_letter + guess_word[index+1:]
            print(guess_word)
            print()
            if guess_word == word:
                print("Congratulations...! you guessed a correct state 🤩")
                break
        else:
            chances -= 1
            
            print("incorrect guess")
            print("remaining chances are ", chances)
            print("<<=========xx==========>>")
            print()
    else:
        print("🙄 please enter alphabetical letter")
else:
    print("game over...🙁")
    print("all chances are exhausted")
    print("Correct Answer is = ",word)





























































































































