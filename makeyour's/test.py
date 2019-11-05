import numpy as np
from puzzle import Puzzle
import pickle
import matplotlib.pyplot as plt

# Constants
gamma = 0.95
moves = ('L', 'U', 'R', 'D')
oob = 1
game_ends = 1

#Epsilon greedy for Monte Carlo
# Probability of a is really 1 - eps + eps / |A|
def random_move(a, eps=0.1):

	p = np.random.random()

	if p < 1 - eps:
		return a
	else:
		return np.random.choice(moves)

# Return the max value and key from a dictionary
# Used to return max action given state for Q function
def max_dict(d):
	mk = None
	mv = float('-inf')
	for k, v in d.items():
		if v >  mv:
			mv = v
			mk = k
	return mk, mv

# Get action directly
# Initializes in-game if a state has not been visited since
# list of states are not known before starting to learn
def get_action(Q, s):

	if s in Q:
		return max_dict(Q[s])[0]
	else:
		Q[s] = {}
		for a in moves:
			Q[s][a] = 0
		return np.random.choice(moves)

def play_game(Q):
	# Get a game board, this initiatizes the game board based on a level of difficulty passed.
	# If 5 is passed, the game board will be set up so that the goal state is 5 moves away from the starting state.
	# It can be that it took 5 moves to generate the starting state but the agent finds it in 3. The init_board function works
	# from random states thus does not follow optimal paths.
	puzzle = Puzzle(np.random.randint(5, 15)+1)
	s = puzzle.current_state()
	#Get action based on current Q function
	a = get_action(Q, s)
	#Explore / Explot with Epsilon Greedy
	a = random_move(a)

	#Start list of States, actions, rewards
	states_actions_rewards = [(s, a, 0)]
	f = open('data.txt', 'w')
	cnt = 0
	while True:

		r = puzzle.move(a)
		s = puzzle.current_state()

		#If game over end the game
		if r==-10 or cnt >= 500:
			print("Out of Bounds")
			break
		elif puzzle.game_over():
			print("Game Over")

			state = list(s)
			for st in state:
				f.write(str(st) + ' ')
			f.write("\n")
			print(s)
			break
		# Continue playing, get next action, explore/exploit
		else:
			a = get_action(Q, s)
			print("State : ")
			state = list(s)
			for st in state:
				f.write(str(st) + ' ')
			f.write("\n")
			print(s)
		cnt += 1
	f.close()

#Tracks to see the number of out of bounds vs number of game_ends
#IF Game_ends do not increase over time, no learning is taking place.
oobs = []
ges = []

if __name__ == '__main__':

	Q = {}
	delta = []

	returns = {}
	with open('Q.pkl', 'rb') as f:
		Q = pickle.load(f)


	# print(Q)
	play_game(Q=Q)