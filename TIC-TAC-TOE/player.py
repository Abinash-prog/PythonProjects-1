import math
import random

class Player:
    def __init__(self,letter):
        # Letter is x or o
        self.letter = letter

    # We want all players to get their next move given a game
    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_sqaure = False
        val = None
        while not valid_sqaure:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not availabe on the board, we also say it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqaure = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # Randomly choose one
        else:
            square = self.minimax(game,self.letter)
        return square
    
    def minimax(self,state,player):
        max_player = self.letter #Youself
        other_player = 'O' if player == 'X' else "X"

        # first we want check if the previous move is a winner
        if state.current_winner == other_player:
            # We should return position and score because we nned to keep track of the score
            # for minimax to work
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
            
        elif not state.empty_sqaures(): #no empty sqaures
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #Each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} #each score should minimize 

        for possible_move in state.available_moves():
            # step-1 : make a move, try that spot
            # step-2 : recurse using minimax to simulate a game after making that move
            state.make_move(possible_move,player)
            sim_score = self.minimax(state,other_player) #simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score ['position']  = possible_move #this represents the move optimal next move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                else:
                    if sim_score['score'] < best['score']:
                        best = sim_score
        return best