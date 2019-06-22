#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
playingStyles = ['cycle', 'reflect', 'random', 'rocker']
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

# In this intiliser function, i set 3 objects variable
#  and i assigned to them intial values


class Player:
    def __init__(self):
        self.score = 0
        self.enemymove = random.choice(moves)
        self.mylastmove = random.choice(moves)

    def move(self):
        return 'rock'
# In this function, i defined my move and their move
#  to make the game memorise the last move of both

    def learn(self, my_move, their_move):
        self.mylastmove = my_move
        self.enemymove = their_move

# In this function,i write assigment statements which return True or Falsa


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# Bellow are subclasses of player class which describe playing styles


class Random_Player (Player):
    def move(self):
        RandomMove = random.choice(moves)
        return RandomMove


class Human_Player(Player):
    def move(self):
        while True:
            HumanPlayerInput = input("Select a move: ").lower()
            if HumanPlayerInput in moves:
                return HumanPlayerInput


class ReflectPlayer(Player):
    def move(self):
        return self.enemymove


class CyclePlayer(Player):
    def move(self):
        if self.mylastmove == "rock":
            return "paper"
        elif self.mylastmove == "scissors":
            return "rock"
        else:
            return "scissors"

# Calculating the scores in each round and activating the learn function here


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player(1) won")
            self.p1.score += 1
        elif beats(move2, move1):
            print("Player(2) won")
            self.p2.score += 1
        else:
            print("Tie")

        print(f"Player 1 score: {self.p1.score}  Player 2: {self.p2.score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
# Presenting the final resultsand activating the play_round function

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"Player 1 score: {self.p1.score}  Player 2: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("Player(1) won")
        elif self.p2.score > self.p1.score:
            print("Player(2) won")
        else:
            print("No winner")


if __name__ == '__main__':
    while True:
        playingStyle = input(
            "choose playing style:('cycle','reflect'," +
            "'random','rocker'): ").lower()
        if playingStyle in playingStyles:
            break
# I put if statments and if the user input meets one of
# the playing styles, the object called game is created
    if playingStyle == "cycle":
        game = Game(Human_Player(), CyclePlayer())
    elif playingStyle == "reflect":
        game = Game(Human_Player(), ReflectPlayer())
    elif playingStyle == "random":
        game = Game(Human_Player(), Random_Player())
    else:
        game = Game(Human_Player(), Player())

    game.play_game()
