#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

# Three different moves the player can make
moves = ['rock', 'paper', 'scissors']


#The Player class is the parent class for all of the Players in this game
class Player:
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


#What move the opponent played last round, and plays that move in the next round
class ReflectPlayer(Player):
    def move(self):
    if not self.their_move:
        return random.choice(moves)
    else:
        return self.their_move


#Chooses its move at random and it returns 'rock','paper', or 'scissors'
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


#It remembers what move _it_ played last round and cycles through the different moves.
class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    #Rotate moves until it restarts with rock again
    def move(self):
        moves_available = moves.index(self.my_move)
        if moves_available == 2:
            return moves[0]
        else:
            return moves[moves_available + 1]

    #Sets up the player to recall its own previous move
    def learn(self, my_move, their_move):
        self.my_move = p1_move






#Keep the score
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def p1_beats_p2(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def p2_beats_p1(one, two):
    return ((two == 'rock' and one == 'scissors') or
            (two == 'scissors' and one == 'paper') or
            (two == 'paper' and one == 'rock'))



#Asks the player to choose the move
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.behavior = "Human Player"

    def move(self):
        #Method that asks the player to choose the move
        while True:
            move = input('Choose a move: (rock / paper / scissors)\n').lower()
            if move in moves:
                return move
            else:
                print("The name of the move is wrong. Try again!")



class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        p1wins = 0
        p2wins = 0
        if p1_beats_p2(move1,move2) == True and p2_beats_p1(move1,move2) == False:
            p1wins += 1
            print("Player 1 won")
        elif p2_beats_p1(move1,move2) == True and p1_beats_p2(move1,move2) == False:
            p2wins += 1
            print("Player 2 won")
        else:
            print("It's a tie!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)




if __name__ == '__main__':
    game = Game(Player(), Random())
    game.play_game()



#5 players
#1 roca
#1humano
#1random
#1circular
#1 que aprende del humano
