from NPuzzle import NPuzzle
from AStarSearch import AStarSearch
import time

num_problem_instances = 50
max_total_time = 60 # time in seconds allotted to run the algorithm

runtimes = []
memory_usages = []

start = time.time()
for i in range(num_problem_instances):
    # Create a random puzzle
    p1: NPuzzle = NPuzzle(8)

    # solve the puzzle
    result, runtime, memory = AStarSearch(p1)

    # record the results
    runtimes.append(runtime)
    memory_usages.append(memory)

    # if the runtime exceeds the time limit
    if time.time() - start > max_total_time:
        break

end = time.time()

print(f'TOTAL WALL-CLOCK RUNTIME: {end-start} SECONDS')
print(f'NUMBER OF PROBLEMS SOLVED: {len(runtimes)}/{num_problem_instances}')
print(f'AVERAGE RUNTIME IN NODES GENERATED: {sum(runtimes)/len(runtimes)} PER PUZZLE')
print(f'AVERAGE MEMORY USAGE (AVERAGE PEAK FRINGE SIZE): {sum(memory_usages)/len(memory_usages)} PER PUZZLE')
