# Author: Nathan Steiger

from NPuzzle import NPuzzle
from RBFS import RBFS_Search
import time

num_problem_instances = 10
max_total_time = 1000 # time in seconds allotted to run the algorithm (may go over, only checks between puzzles)

runtimes = []

start = time.time()
for i in range(num_problem_instances):
    # Create a random puzzle
    p1: NPuzzle = NPuzzle(8)

    # solve the puzzle
    result, runtime = RBFS_Search(p1)

    # record the results
    runtimes.append(runtime)
    print(f'Solved: {len(runtimes)}')

    # if the runtime exceeds the time limit
    if time.time() - start > max_total_time:
        break

end = time.time()

print(f'TOTAL WALL-CLOCK RUNTIME: {end-start} SECONDS')
print(f'NUMBER OF PROBLEMS SOLVED: {len(runtimes)}/{num_problem_instances}')
print(f'AVERAGE RUNTIME IN NODES GENERATED: {sum(runtimes)/len(runtimes)} PER PUZZLE')
for val in runtimes:
    print(val)