import os
import re
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt


def stats(name, *strategy):
    folder_path = 'D:\\SISE\\repo\\JAVA\\stats\\'
    stats_dict = defaultdict(lambda: {'L': [], 'C': [], 'F': [], 'D': [], 'T': []})
    stan = '([a-z]{4})'
    if strategy:
        stan = strategy[0]

    lineregex = re.compile(r'4x4_(\d{2})_\d{5}_' + name + '_' + stan + '_stats.txt')
    for filename in os.listdir(folder_path):
        mat = lineregex.match(filename)
        if mat:
            size = mat.group(1)
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    x, y, z, k, m = f.readlines()
                    if x != -1:
                        stats_dict[size]['L'].append(int(x))
                    stats_dict[size]['C'].append(int(y))
                    stats_dict[size]['F'].append(int(z))
                    stats_dict[size]['D'].append(int(k))
                    stats_dict[size]['T'].append(float(m))

    avgL = [sum(stats_dict[size]['L']) / len(stats_dict[size]['L']) for size in stats_dict]
    avgClosed = [sum(stats_dict[size]['C']) / len(stats_dict[size]['C']) for size in stats_dict]
    avgFrontier = [sum(stats_dict[size]['F']) / len(stats_dict[size]['F']) for size in stats_dict]
    avgDepth = [sum(stats_dict[size]['D']) / len(stats_dict[size]['D']) for size in stats_dict]
    avgTime = [sum(stats_dict[size]['T']) / len(stats_dict[size]['T']) for size in stats_dict]

    return avgL, avgClosed, avgFrontier, avgDepth, avgTime


names = ['1', '2', '3', '4', '5', '6', '7']
plt.rcParams["figure.figsize"] = [9, 13]
fig, ax = plt.subplots(2, 2, tight_layout=True)
names_axis = np.arange(len(names))

width = 0.3
ax[0, 0].bar(names_axis - width, stats('bfs')[0], width, color='yellow', edgecolor='black')
ax[0, 0].bar(names_axis, stats('dfs')[0], 0.3, color='orange', edgecolor='black')
ax[0, 0].bar(names_axis + width, stats('astr')[0], width, color='red', edgecolor='black')
ax[0, 0].set_ylabel("Avg solution length")
ax[0, 0].set_xticks(names_axis, names)
ax[0, 0].set_title("Overall")
ax[0, 0].legend(["BFS", "DFS", "A*"], loc="upper left")

ax[0, 1].bar(names_axis - 0.5 * width, stats('astr', 'hamm')[0], width, color='lightblue', edgecolor='black')
ax[0, 1].bar(names_axis + 0.5 * width, stats('astr', 'manh')[0], width, color='darkgreen' , edgecolor='black')
ax[0, 1].set_title("A*")
ax[0, 1].set_xticks(names_axis, names)
ax[0, 1].set_yticks([1, 2, 3, 4, 5, 6, 7])
ax[0, 1].legend(["Hamming", "Manhattan"], loc="upper left")

width = 0.10
ax[1, 0].bar(names_axis - 3.5 * width, stats('bfs', 'rdul')[0], width, color='lightblue', edgecolor='black')
ax[1, 0].bar(names_axis - 2.5 * width, stats('bfs', 'rdlu')[0], width, color='orange', edgecolor='black')
ax[1, 0].bar(names_axis - 1.5 * width, stats('bfs', 'drul')[0], width, color='darkgreen', edgecolor='black')
ax[1, 0].bar(names_axis - 0.5 * width, stats('bfs', 'drlu')[0], width, color='pink', edgecolor='black')
ax[1, 0].bar(names_axis + 0.5 * width, stats('bfs', 'ludr')[0], width, color='red', edgecolor='black')
ax[1, 0].bar(names_axis + 1.5 * width, stats('bfs', 'lurd')[0], width, color='magenta', edgecolor='black')
ax[1, 0].bar(names_axis + 2.5 * width, stats('bfs', 'uldr')[0], width, color='darkblue', edgecolor='black')
ax[1, 0].bar(names_axis + 3.5 * width, stats('bfs', 'ulrd')[0], width, color='lightgreen', edgecolor='black')
ax[1, 0].set_ylabel("Avg solution length")
ax[1, 0].set_xticks(names_axis, names)
ax[1, 0].set_title("BFS")
ax[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], loc="upper left")
ax[1, 0].set_xlabel("Depth")

ax[1, 1].bar(names_axis - 3.5 * width, stats('dfs', 'rdul')[0], width, color='lightblue', edgecolor='black')
ax[1, 1].bar(names_axis - 2.5 * width, stats('dfs', 'rdlu')[0], width, color='orange', edgecolor='black')
ax[1, 1].bar(names_axis - 1.5 * width, stats('dfs', 'drul')[0], width, color='darkgreen', edgecolor='black')
ax[1, 1].bar(names_axis - 0.5 * width, stats('dfs', 'drlu')[0], width, color='pink', edgecolor='black')
ax[1, 1].bar(names_axis + 0.5 * width, stats('dfs', 'ludr')[0], width, color='red', edgecolor='black')
ax[1, 1].bar(names_axis + 1.5 * width, stats('dfs', 'lurd')[0], width, color='magenta', edgecolor='black')
ax[1, 1].bar(names_axis + 2.5 * width, stats('dfs', 'uldr')[0], width, color='darkblue', edgecolor='black')
ax[1, 1].bar(names_axis + 3.5 * width, stats('dfs', 'ulrd')[0], width, color='lightgreen', edgecolor='black')
ax[1, 1].set_xticks(names_axis, names)
ax[1, 1].set_title("DFS")
ax[1, 1].set_xlabel("Depth")
plt.savefig('wykresy.png')
plt.clf()


plt.rcParams["figure.figsize"] = [9, 13]
fig, ax = plt.subplots(2, 2, tight_layout=True)
width = 0.3
ax[0, 0].bar(names_axis - 0.25, stats('bfs')[1], 0.25, color='yellow', log=True, edgecolor='black')
ax[0, 0].bar(names_axis, stats('dfs')[1], 0.25, color='orange', log=True, edgecolor='black')
ax[0, 0].bar(names_axis + 0.25, stats('astr')[1], 0.25, color='red', log=True, edgecolor='black')
ax[0, 0].set_ylabel("Number of visited nodes")
ax[0, 0].set_xticks(names_axis, names)
ax[0, 0].set_title("Overall")
ax[0, 0].legend(['BFS', 'DFS', 'A*'], loc="upper left")
ax[0, 0].set_yticks([1, 10, 100, 1000, 10000, 100000, 1000000])

ax[0, 1].bar(names_axis - 0.5 * width, stats('astr', 'hamm')[1], width, color='lightblue', edgecolor='black')
ax[0, 1].bar(names_axis + 0.5 * width, stats('astr', 'manh')[1], width, color='darkgreen', edgecolor='black')
ax[0, 1].set_title("A*")
ax[0, 1].set_xticks(names_axis, names)
ax[0, 1].legend(['Hamming', 'Manhattan'], loc="upper left")
ax[0, 1].set_yticks([0, 5, 10, 15, 20, 25])

width = 0.1
ax[1, 0].bar(names_axis - 3.5 * width, stats('bfs', 'rdul')[1], width, color='lightblue', log=True, edgecolor='black')
ax[1, 0].bar(names_axis - 2.5 * width, stats('bfs', 'rdlu')[1], width, color='orange', log=True, edgecolor='black')
ax[1, 0].bar(names_axis - 1.5 * width, stats('bfs', 'drul')[1], width, color='darkgreen', log=True, edgecolor='black')
ax[1, 0].bar(names_axis - 0.5 * width, stats('bfs', 'drlu')[1], width, color='pink', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 0.5 * width, stats('bfs', 'ludr')[1], width, color='red', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 1.5 * width, stats('bfs', 'lurd')[1], width, color='magenta', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 2.5 * width, stats('bfs', 'uldr')[1], width, color='darkblue', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 3.5 * width, stats('bfs', 'ulrd')[1], width, color='lightgreen', log=True, edgecolor='black')
ax[1, 0].set_ylabel("Number of visited nodes")
ax[1, 0].set_xticks(names_axis, names)
# ax[1, 0].set_yticks([1, 10, 100, 1000])
ax[1, 0].set_title("BFS")
ax[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], loc="upper left")
ax[1, 0].set_xlabel("Depth")

ax[1, 1].bar(names_axis - 3.5 * width, stats('dfs', 'rdul')[1], width, color='lightblue', log=True, edgecolor='black')
ax[1, 1].bar(names_axis - 2.5 * width, stats('dfs', 'rdlu')[1], width, color='orange', log=True, edgecolor='black')
ax[1, 1].bar(names_axis - 1.5 * width, stats('dfs', 'drul')[1], width, color='darkgreen', log=True, edgecolor='black')
ax[1, 1].bar(names_axis - 0.5 * width, stats('dfs', 'drlu')[1], width, color='pink', log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 0.5 * width, stats('dfs', 'ludr')[1], width, color='red', log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 1.5 * width, stats('dfs', 'lurd')[1], width, color='magenta', log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 2.5 * width, stats('dfs', 'uldr')[1], width, color='darkblue', log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 3.5 * width, stats('dfs', 'ulrd')[1], width, color='lightgreen', log=True, edgecolor='black')
ax[1, 1].set_xticks(names_axis, names)
# ax[1, 1].set_yticks([1, 10, 100, 1000, 10000, 100000, 1000000])
ax[1, 1].set_title("DFS")
ax[1, 1].set_xlabel("Depth")

plt.savefig('wykresy1.png')
plt.clf()


fig, ax = plt.subplots(2, 2, tight_layout=True)

ax[0, 0].bar(names_axis - 0.2, stats('bfs')[2], 0.2, color='yellow', log=True, edgecolor='black')
ax[0, 0].bar(names_axis, stats('dfs')[2], 0.2, color='orange', log=True, edgecolor='black')
ax[0, 0].bar(names_axis + 0.2, stats('astr')[2], 0.2, color='red', log=True, edgecolor='black')
ax[0, 0].set_ylabel("Number of processed nodes")
ax[0, 0].set_xticks(names_axis, names)
ax[0, 0].set_title("Overall")
ax[0, 0].legend(['BFS', 'DFS', 'A*'], loc="upper left")
# ax[0, 0].set_yticks([1, 10, 100, 1000, 10000, 100000, 1000000])
width = 0.3
ax[0, 1].bar(names_axis - 0.5*width, stats('astr', 'hamm')[2], width, color='lightblue', edgecolor='black')
ax[0, 1].bar(names_axis+ 0.5*width, stats('astr', 'manh')[0], width, color='darkgreen', edgecolor='black')
ax[0, 1].set_title("A*")
ax[0, 1].set_xticks(names_axis, names)
ax[0, 1].legend(['Hamming', 'Manhattan'], loc="upper left")
ax[0, 1].set_yticks([0, 2, 4, 6, 8, 10])

width = 0.1
ax[1, 0].bar(names_axis - 3.5 * width, stats('bfs', 'rdul')[2], width, color='lightblue', log=True, edgecolor='black')
ax[1, 0].bar(names_axis - 2.5 * width, stats('bfs', 'rdlu')[2], width, color='orange', log=True, edgecolor='black')
ax[1, 0].bar(names_axis - 1.5 * width, stats('bfs', 'drul')[2], width, color='darkgreen', log=True, edgecolor='black')
ax[1, 0].bar(names_axis - 0.5 * width, stats('bfs', 'drlu')[2], width, color='pink', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 0.5 * width, stats('bfs', 'ludr')[2], width,      color='red', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 1.5 * width, stats('bfs', 'lurd')[2], width, color='magenta', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 2.5 * width, stats('bfs', 'uldr')[2], width, color='darkblue', log=True, edgecolor='black')
ax[1, 0].bar(names_axis + 3.5 * width, stats('bfs', 'ulrd')[2], width, color='lightgreen', log=True, edgecolor='black')
ax[1, 0].set_ylabel("Number of processed nodes")
ax[1, 0].set_xticks(names_axis, names)
# ax[1, 0].set_yticks([1, 10, 100, 1000])
ax[1, 0].set_title("BFS")
ax[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], loc="upper left")
ax[1, 0].set_xlabel("Depth")

ax[1, 1].bar(names_axis - 3.5 * width, stats('dfs', 'rdul')[2], width, color='lightblue', log=True, edgecolor='black')
ax[1, 1].bar(names_axis - 2.5 * width, stats('dfs', 'rdlu')[2], width, color='orange',  log=True, edgecolor='black')
ax[1, 1].bar(names_axis - 1.5 * width, stats('dfs', 'drul')[2], width, color='darkgreen', log=True, edgecolor='black')
ax[1, 1].bar(names_axis - 0.5 * width, stats('dfs', 'drlu')[2], width, color='pink', log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 0.5 * width, stats('dfs', 'ludr')[2], width,       color='red', log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 1.5 * width, stats('dfs', 'lurd')[2], width, color='magenta',  log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 2.5 * width, stats('dfs', 'uldr')[2], width, color='darkblue',  log=True, edgecolor='black')
ax[1, 1].bar(names_axis + 3.5 * width, stats('dfs', 'ulrd')[2], width, color='lightgreen' ,log=True, edgecolor='black')
ax[1, 1].set_xticks(names_axis, names)
ax[1, 1].set_title("DFS")
ax[1, 1].set_xlabel("Depth")
# ax[1, 1].set_yticks([1, 10, 100, 1000, 10000, 100000, 1000000])

plt.savefig('wykresy2.png')
plt.clf()


fig, ax = plt.subplots(2, 2, tight_layout=True)

ax[0, 0].bar(names_axis - 0.2, stats('bfs')[3], 0.2, color='yellow', edgecolor='black')
ax[0, 0].bar(names_axis, stats('dfs')[3], 0.2, color='orange', edgecolor='black')
ax[0, 0].bar(names_axis + 0.2, stats('astr')[3], 0.2, color='red', edgecolor='black')
ax[0, 0].set_ylabel("Max recursion depth")
ax[0, 0].set_xticks(names_axis, names)
ax[0, 0].set_title("Overall")
ax[0, 0].legend(['BFS', 'DFS', 'A*'], loc="upper left")
ax[0, 0].set_yticks([0, 5, 10, 15, 20])

width = 0.25
ax[0, 1].bar(names_axis - 0.5*width, stats('astr', 'hamm')[3], width, color='lightblue', edgecolor='black')
ax[0, 1].bar(names_axis + 0.5*width, stats('astr', 'manh')[3], width, color='darkgreen', edgecolor='black')
ax[0, 1].set_title("A*")
ax[0, 1].set_xticks(names_axis, names)
ax[0, 1].legend(['Hamming', 'Manhattan'], loc="upper left")

width = 0.1
ax[1, 0].bar(names_axis - 3.5 * width, stats('bfs', 'rdul')[3], width, color='lightblue',  edgecolor='black')
ax[1, 0].bar(names_axis - 2.5 * width, stats('bfs', 'rdlu')[3], width, color='orange', edgecolor='black')
ax[1, 0].bar(names_axis - 1.5 * width, stats('bfs', 'drul')[3], width, color='darkgreen', edgecolor='black')
ax[1, 0].bar(names_axis - 0.5 * width, stats('bfs', 'drlu')[3], width, color='pink', edgecolor='black')
ax[1, 0].bar(names_axis + 0.5 * width, stats('bfs', 'ludr')[3], width,      color='red',  edgecolor='black')
ax[1, 0].bar(names_axis + 1.5 * width, stats('bfs', 'lurd')[3], width, color='magenta' , edgecolor='black')
ax[1, 0].bar(names_axis + 2.5 * width, stats('bfs', 'uldr')[3], width, color='darkblue',  edgecolor='black')
ax[1, 0].bar(names_axis + 3.5 * width, stats('bfs', 'ulrd')[3], width, color='lightgreen', edgecolor='black')
ax[1, 0].set_ylabel("Max recursion depth")
ax[1, 0].set_xticks(names_axis, names)
ax[1, 0].set_title("BFS")
ax[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], loc="upper left")
ax[1, 0].set_xlabel("Depth")

ax[1, 1].bar(names_axis - 3.5 * width, stats('dfs', 'rdul')[3], width, color='lightblue', edgecolor='black')
ax[1, 1].bar(names_axis - 2.5 * width, stats('dfs', 'rdlu')[3], width, color='orange',  edgecolor='black')
ax[1, 1].bar(names_axis - 1.5 * width, stats('dfs', 'drul')[3], width, color='darkgreen',  edgecolor='black')
ax[1, 1].bar(names_axis - 0.5 * width, stats('dfs', 'drlu')[3], width, color='pink', edgecolor='black')
ax[1, 1].bar(names_axis + 0.5 * width, stats('dfs', 'ludr')[3], width,       color='red', edgecolor='black')
ax[1, 1].bar(names_axis + 1.5 * width, stats('dfs', 'lurd')[3], width, color='magenta' ,  edgecolor='black')
ax[1, 1].bar(names_axis + 2.5 * width, stats('dfs', 'uldr')[3], width, color='darkblue',  edgecolor='black')
ax[1, 1].bar(names_axis + 3.5 * width, stats('dfs', 'ulrd')[3], width, color='lightgreen',edgecolor='black')
ax[1, 1].set_xticks(names_axis, names)
ax[1, 1].set_title("DFS")
ax[1, 1].set_xlabel("Depth")
plt.savefig('wykresy3.png')
plt.clf()

fig2, ax2 = plt.subplots(2, 2, tight_layout=True)
ax2[0, 0].bar(names_axis - 0.2, stats('bfs')[4], 0.2, color='yellow', log=True, edgecolor='black')
ax2[0, 0].bar(names_axis, stats('dfs')[4], 0.2, color='orange', log=True, edgecolor='black')
ax2[0, 0].bar(names_axis + 0.2, stats('astr')[4], 0.2, color='red', log=True, edgecolor='black')
ax2[0, 0].set_ylabel("Runtime [ms]")
ax2[0, 0].set_xticks(names_axis, names)
# ax2[0, 0].set_yticks([0.01, 0.1, 1, 10, 100])
ax2[0, 0].set_title("Overall")
ax2[0, 0].legend(['BFS', 'DFS', 'A*'], loc="upper left")

width = 0.3
ax2[0, 1].bar(names_axis - 0.5*width, stats('astr', 'hamm')[4], width, color='lightblue', edgecolor='black')
ax2[0, 1].bar(names_axis + 0.5*width, stats('astr', 'manh')[4], width, color='darkgreen', edgecolor='black')
ax2[0, 1].set_title("A*")
ax2[0, 1].set_xticks(names_axis, names)
# ax2[0, 1].set_yticks([0, 0.02, 0.04, 0.06, 0.08, 0.1])
ax2[0, 1].legend(['Hamming', 'Manhattan'], loc="upper left")

width = 0.1
ax2[1, 0].bar(names_axis - 3.5 * width, stats('bfs', 'rdul')[4], width, color='lightblue',  edgecolor='black')
ax2[1, 0].bar(names_axis - 2.5 * width, stats('bfs', 'rdlu')[4], width, color='orange', edgecolor='black')
ax2[1, 0].bar(names_axis - 1.5 * width, stats('bfs', 'drul')[4], width, color='darkgreen',  edgecolor='black')
ax2[1, 0].bar(names_axis - 0.5 * width, stats('bfs', 'drlu')[4], width, color='pink', edgecolor='black')
ax2[1, 0].bar(names_axis + 0.5 * width, stats('bfs', 'ludr')[4], width,      color='red', edgecolor='black')
ax2[1, 0].bar(names_axis + 1.5 * width, stats('bfs', 'lurd')[4], width, color='magenta' ,  edgecolor='black')
ax2[1, 0].bar(names_axis + 2.5 * width, stats('bfs', 'uldr')[4], width, color='darkblue',   edgecolor='black')
ax2[1, 0].bar(names_axis + 3.5 * width, stats('bfs', 'ulrd')[4], width, color='lightgreen', edgecolor='black')
ax2[1, 0].set_ylabel("Runtime [ms]")
ax2[1, 0].set_xticks(names_axis, names)
ax2[1, 0].set_title("BFS")
ax2[1, 0].legend(['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'], loc="upper left")
ax2[1, 0].set_xlabel("Depth")
# ax2[1, 0].set_yticks([0, 0.05, 0.1, 0.15, 0.2, 0.25])

ax2[1, 1].bar(names_axis - 3.5 * width, stats('dfs', 'rdul')[4], width, color='lightblue', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis - 2.5 * width, stats('dfs', 'rdlu')[4], width, color='orange', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis - 1.5 * width, stats('dfs', 'drul')[4], width, color='darkgreen', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis - 0.5 * width, stats('dfs', 'drlu')[4], width, color='pink', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis + 0.5 * width, stats('dfs', 'ludr')[4], width,      color='red', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis + 1.5 * width, stats('dfs', 'lurd')[4], width, color='magenta', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis + 2.5 * width, stats('dfs', 'uldr')[4], width, color='darkblue', log=True, edgecolor='black')
ax2[1, 1].bar(names_axis + 3.5 * width, stats('dfs', 'ulrd')[4], width, color='lightgreen', log=True, edgecolor='black')
ax2[1, 1].set_xticks(names_axis, names)
ax2[1, 1].set_title("DFS")
ax2[1, 1].set_xlabel("Depth")
# ax2[1, 1].set_yticks([0.01, 0.1, 1, 10, 100, 1000])

plt.savefig('wykresy4.png')
plt.clf()
