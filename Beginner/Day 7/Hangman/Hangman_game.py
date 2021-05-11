import random
from replit import clear
from hangman_img import stages, logo
from words import word_list

print(logo)
print("Guss the word !!!!")
ran_word=random.choice(word_list)
word_length=len(ran_word)

no_of_lives=6
display=[]
for _ in range(word_length):
    display+="_"

end_of_game=False

while not end_of_game:
    gus_letter=input("Guess a letter : ").lower()
    clear()
    if gus_letter in display:
      print(f"You have already guessed : {gus_letter}")
    for p in range(word_length):
        letter=ran_word[p]
        if(letter==gus_letter):
            display[p]=letter
    if gus_letter not in ran_word:
        print(f"You gussed {gus_letter}, that's not in the word. You lose a life.")
        no_of_lives-=1
        if no_of_lives == 0 : 
            end_of_game=True
            print("You Lose!!!")
            print(f"Word was : {ran_word}")
    print(display)
    if "_" not in display:
        end_of_game=True
        print("You Win!!!")
        print(f"Word was : {ran_word}")
    print(stages[no_of_lives])