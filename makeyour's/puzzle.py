import numpy as np

class Puzzle:

	def __init__(self, diff, step_cost=0):

		#List of possible moves
		self.moves = ('U', 'L', 'R', 'D')
		#Only reward the agent for completing the game, given the goal state return a reward of 1
		self.rewards = {
			tuple(np.append(np.arange(1, 9), 0).tolist()) : 1.0
		}
		# Change the game board based on move
		self.actions = {
			'U' : (-1, 0),
			'L' : (0, -1),
			'R' : (0, 1),
			'D' : (1, 0)
		}
		# 0 cost for moves or step_cost (usually -0.1) for moves
		self.step_cost = step_cost
		# Initiate the board
		self.init_board(diff)

		# Get current state as a tuple since it is hashable
	def current_state(self):
		return tuple(self.board.reshape(-1, ).tolist())

		#Game logic for a move. If the move is legal return the reward else return -10 for Out of Bounds errors. 
	def move(self, a):

		idx = np.argwhere(self.board == 0)[0]

		if (max(idx + self.actions[a]) < 3) & (min(idx + self.actions[a]) > -1):
			new_idx = idx + self.actions[a]
			value = self.board[tuple(new_idx)]
			self.board[tuple(idx)] = value
			self.board[tuple(new_idx)] = 0
			ret = self.rewards.get(self.current_state(), self.step_cost)
			return ret

		else:
			return -10

		# Function is used when finding the starting state
		# I play the game in reverse to generate a game since we need to know the complexity
		# of the game we are making. Using random number generator here may produce games
		# that are not possible to solve based on the allowed moved for the zero piece. 
	def is_valid(self, a):

		idx = np.argwhere(self.board == 0)[0]
		return (max(idx + self.actions[a]) < 3) & (min(idx + self.actions[a]) > -1)

		# Function used when finding the starting state
	def temp_move(self, a):

		idx = np.argwhere(self.board == 0)[0]
		if (max(idx + self.actions[a]) < 3) & (min(idx + self.actions[a]) > -1):
			board = self.board.copy()
			new_idx = idx + self.actions[a]
			value = board[tuple(new_idx)]
			board[tuple(idx)] = value
			board[tuple(new_idx)] = 0
			return tuple(board.reshape(-1, ).tolist())

		# Function to generate the starting state.
		# Plays game in reverse
	def init_board(self, diff):

		self.board = np.append(np.arange(1, 9), 0).reshape(3, 3)

		success = 0
		ctr = 0
		seen = set(self.current_state())

		while success < diff:

			if ctr > 2*diff:
				break
			ctr += 1
			a = np.random.choice(self.moves)
			if self.is_valid(a):
				temp_move = self.temp_move(a)
				if (temp_move not in seen) & (temp_move is not None):
					self.move(a)
					seen.add(self.current_state())
					success += 1

		#Game over checker
	def game_over(self):

		return self.current_state() == tuple(np.append(np.arange(1, 9), 0).tolist())

		#String function to print board, is simply a 2D array
	def __str__(self):

		print(self.board)
		return ''

