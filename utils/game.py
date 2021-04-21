import re
import random


class Hangman:
    

    


    def __init__(self):
        self.possible_words = ['becode','learning','mathematics','sessions']
        self.word_to_find = list(str(random.choice(self.possible_words)))
        self.lives = 5
        self.correctly_guessed_letters = ["_"]*len(self.word_to_find) 
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0




    def play(self):
        while(self.lives>=0 and self.word_to_find != self.correctly_guessed_letters):
            input_letter = str(input("Enter a letter : "))
            if(re.match("^[a-z]{1}",input_letter)):
                for letter in self.word_to_find:
                    for i in range (len(self.word_to_find)):
                        if(input_letter == self.word_to_find[i]):
                            self.correctly_guessed_letters[i] = input_letter
                            print(self.correctly_guessed_letters)
            if(input_letter not in self.word_to_find):
                    print("faux")
                    self.wrongly_guessed_letters.append(input_letter)
                    self.error_count+=1
                    self.lives-=1
            self.turn_count+=1
            if(self.correctly_guessed_letters == self.word_to_find):
                print("bravo")
        print(self.error_count)
        print(self.turn_count)
        print(self.wrongly_guessed_letters)
        def start_game(self):
            play()
            if(self.lives==0):
                game_over(self)
            if(correctly_guessed_letters == word_to_find):
                well_played()


        def game_over(self):
            print("Game Over!")

        def well_played(self):
            print("You win")

game = Hangman()
game.play()


                    
                    
                    

