import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Algorithm, Strategy, Initial Board File, Solution File, Statistic File")
parser.add_argument("algorithm")
parser.add_argument("strategy")
parser.add_argument("init_board_file")
parser.add_argument("sol_file")
parser.add_argument("stat_file")

args = parser.parse_args()

# argument - Algorithm, Strategy
if args.algorithm == "dfs" or args.algorithm == "bfs":
    # set of valid chars - order doesn't matter
    valid_chars = {'L', 'R', 'U', 'D'}
    STRATEGY = []
    for i in args.strategy:
        STRATEGY.append(i)
    if len(STRATEGY) != 4 or set(STRATEGY) != valid_chars:
        raise Exception("Wrong strategy argument")

elif args.algorithm == "astr":
    if args.strategy == "hamm" or args.strategy == "manh":
        HEURISTIC = args.strategy
    else:
        raise Exception("Wrong heuristic argument")
else:
    raise Exception("Wrong algorithm argument")

# argument - Initial Board File
INIT_FILE_PATH = args.init_board_file

with open(INIT_FILE_PATH, 'r') as file:
    w, k = file.readline().strip().split()
    w, k = int(w), int(k)
    read_board = []
    for i in range(w):
        row = file.readline().strip().split()
        read_board.append(row)
    for i in range(w):
        for j in range(k):
            read_board[i][j] = int(read_board[i][j])
INIT_BOARD = np.matrix(read_board)



