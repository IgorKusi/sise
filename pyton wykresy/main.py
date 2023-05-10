import os
import glob
import matplotlib.pyplot as plt
import numpy as np

def parse_filename(filename):
    filename = filename.replace(".txt", "")
    parts = filename.split("_")
    size = int(parts[0].replace("x", ""))
    depth = int(parts[1])
    file_id = int(parts[2])
    algorithm = parts[3].lower()
    order_or_heuristic = parts[4].lower()
    return size, depth, file_id, algorithm, order_or_heuristic

def read_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        solution_length = int(lines[0])
        visited_states = int(lines[1])
        processed_states = int(lines[2])
        max_recursion_depth = int(lines[3])
        execution_time = float(lines[4])
        return solution_length, visited_states, processed_states, max_recursion_depth, execution_time

def process_files(folder_path):
    files = glob.glob(os.path.join(folder_path, "*.txt"))

    data = {
        'bfs': {'Depth': [], 'Solution Length': [], 'Visited States': [], 'Processed States': [], 'Recursion Depth': [], 'Execution Time': []},
        'dfs': {'Depth': [], 'Solution Length': [], 'Visited States': [], 'Processed States': [], 'Recursion Depth': [], 'Execution Time': []},
        'astr': {'Depth': [], 'Solution Length': [], 'Visited States': [], 'Processed States': [], 'Recursion Depth': [], 'Execution Time': []}
    }

    for file_path in files:
        size, depth, file_id, algorithm, order_or_heuristic = parse_filename(os.path.basename(file_path))
        solution_length, visited_states, processed_states, max_recursion_depth, execution_time = read_file(file_path)

        data[algorithm]['Depth'].append(depth)
        data[algorithm]['Solution Length'].append(solution_length)
        data[algorithm]['Visited States'].append(visited_states)
        data[algorithm]['Processed States'].append(processed_states)
        data[algorithm]['Recursion Depth'].append(max_recursion_depth)
        data[algorithm]['Execution Time'].append(execution_time)

    return data

def plot_bar_chart(ax, x, y, xlabel, ylabel, title):
    ax.bar(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

# Path to the folder with files
folder_path = r"C:\studia\sise\JAVA\stats"

# Process the files and extract the data
data = process_files(folder_path)

# Create separate figures for each criterion
fig_solution_length = plt.figure()
fig_visited_states = plt.figure()
fig_processed_states = plt.figure()
fig_recursion_depth = plt.figure()
fig_execution_time = plt.figure()

# Plot for solution length
ax_solution_length = fig_solution_length.add_subplot(111)
plot_bar_chart(ax_solution_length, ['bfs', 'dfs', 'astr'], [np.mean(data['bfs']['Solution Length']),
                                                          np.mean(data['dfs']['Solution Length']),
                                                          np.mean(data['astr']['Solution Length'])],
               'Algorithm', 'Average Solution Length', 'Average Solution Length for Algorithms')

# Plot for visited states
ax_visited_states = fig_visited_states.add_subplot(111)
plot_bar_chart(ax_visited_states, ['bfs', 'dfs', 'astr'], [np.mean(data['bfs']['Visited States']),
                                                        np.mean(data['dfs']['Visited States']), np.mean(data['astr']['Visited States'])],
                                                        'Algorithm', 'Average Visited States', 'Average Visited States for Algorithms')


ax_processed_states = fig_processed_states.add_subplot(111)
plot_bar_chart(ax_processed_states, ['bfs', 'dfs', 'astr'], [np.mean(data['bfs']['Processed States']),
np.mean(data['dfs']['Processed States']),
np.mean(data['astr']['Processed States'])],
'Algorithm', 'Average Processed States', 'Average Processed States for Algorithms')

ax_recursion_depth = fig_recursion_depth.add_subplot(111)
plot_bar_chart(ax_recursion_depth, ['bfs', 'dfs', 'astr'], [np.mean(data['bfs']['Recursion Depth']),
np.mean(data['dfs']['Recursion Depth']),
np.mean(data['astr']['Recursion Depth'])],
'Algorithm', 'Average Recursion Depth', 'Average Recursion Depth for Algorithms')


ax_execution_time = fig_execution_time.add_subplot(111)
plot_bar_chart(ax_execution_time, ['bfs', 'dfs', 'astr'], [np.mean(data['bfs']['Execution Time']),
np.mean(data['dfs']['Execution Time']),
np.mean(data['astr']['Execution Time'])],
'Algorithm', 'Average Execution Time', 'Average Execution Time for Algorithms')



plt.show()
