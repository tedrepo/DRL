import pandas as pd
import matplotlib.pylab as plt
import numpy as np
plt.style.use('ggplot')
 

def moving_average(x):
	x = list(x)
	N = len(x)
	window = 16
	x_new = []
	for i in range(N-window):
		x_new.append(np.mean(x[i:i+window]))
	x_new = x_new + x[N-window : N]
	return np.array(x_new)	

if __name__=='__main__':
	folders = ['Data_Basic_A3C', 'Data_1level_A3C', 'Data_2level_A3C', 'Data_3level_A3C']
	#game = 'pong'
	#game = 'pacman'
	game = 'breakout'
	PATH = '/home/jingtao/Work/DRL_Data/' + game + '/'
	selected_folders = [0, 1]
	N_folders = len(selected_folders)
	data = []
	for i in selected_folders:
		this_path = PATH + folders[i] + '/reward_data.csv'
		this_df = pd.read_csv(this_path)
		this_Y = moving_average(this_df['reward'].values)
		this_X = this_df['step'].values
		data.append(this_X)
		data.append(this_Y)

	plt.figure(figsize=(8, 8))
	plt.plot(*data, linewidth=1.2)
	plt.xlabel('Step')
	plt.ylabel('Episode Reward')
	plt.title('Episode Reward v.s. Step')
	legend = []
	for i in selected_folders:
		legend.append(folders[i])
	plt.legend(legend)
	#plt.show()
	plt.savefig(PATH + 'result.eps', format='eps', dpi=1000)
	

