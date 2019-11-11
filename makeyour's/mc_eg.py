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

	while True:

		r = puzzle.move(a)
		s = puzzle.current_state()

		#If out of bounds, end the game
		if r == -10:
			states_actions_rewards.append((s, None, r))
			global oob
			oob += 1
			break
		#If game over end the game
		elif puzzle.game_over():
			global game_ends
			game_ends +=1
			states_actions_rewards.append((s, None, r))
			break
		# Continue playing, get next action, explore/exploit
		else:
			a = get_action(Q, s)
			a = random_move(a)
			states_actions_rewards.append((s, a, r))

	#Convert those rewards into returns.
	G = 0
	states_actions_returns = []
	first = True

	for s, a, r in reversed(states_actions_rewards):
		if first:
			first = False
		else:
			states_actions_returns.append((s, a, G))
		G = r + gamma * G
	states_actions_returns.reverse()
	return states_actions_returns

#Tracks to see the number of out of bounds vs number of game_ends
#IF Game_ends do not increase over time, no learning is taking place.
oobs = []
ges = []

if __name__ == '__main__':

	Q = {}
	delta = []

	returns = {}
	for epi in range(30000):

		#Keep track during epochs
		if epi % 1000 == 0:
			print('epi', epi)
			print('pct oob', oob / (oob + game_ends))
			oobs.append( oob / (oob + game_ends))
			print('pct ends', game_ends / (oob + game_ends))
			ges.append(game_ends / (oob + game_ends))
			oob = 0
			game_ends = 0

		# Get list of retruns for a given played game
		states_actions_returns = play_game(Q)
		# First visit is applied here, so we only add the returns for the state
		# the first time it was visited.
		seen = set()


		for s, a, G in states_actions_returns:
			sa = (s, a)
			if sa not in seen:
				if sa not in returns:
					returns[sa] = [0, 1]
				#Update the mean without keeping super long lists of numbers. Update using update equation.
				x = returns[sa]
				x[1] += 1
				x[0] =  ((x[1] - 1) / x[1]) * x[0] + (1 / x[1]) * G
				#Q at s at s gets the mean of those returns
				Q[s][a] = x[0]
				seen.add(sa)

	pickle.dump(Q, open('Q.pkl', 'wb'))
	plt.plot(oobs)
	plt.plot(ges)
	plt.savefig("result.png")
	# plt.show()

