import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = pd.read_csv('/Users/dokaja/ED/python/runs.csv')
team1 = f['team1']
legend = ['Team1, Team2']
team2 = f['team2']
plt.hist([team1,team2], color = ['blue', 'read'])
plt.xlabel("Teams score")
plt.ylabel("Frequency")
plt.legend(legend)
plt.yticks(10)
plt.xticks(20)
plt.title("The teams game 2020")
plt.show()