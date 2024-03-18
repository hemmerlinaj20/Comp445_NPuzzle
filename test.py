from NPuzzle import NPuzzle
from AStarSearch import AStarSearch
import time

p1 = NPuzzle(15,[[11,5,0,1],[2,6,4,7],[13,9,12,3],[10,14,15,8]])

print('STARTING STATE:')
    
print(p1.string())

print('SEARCHING')

start = time.time()
result, runtime, memory = AStarSearch(puzzle = p1, verbosity = 0)
end = time.time()

print('SEARCH COMPLETE')

print(f'PATH LENGTH: {result.moves}')

print(f'RUNTIME (TOTAL NUMBER OF NODES GENERATED): {runtime}')
print(f'MEMORY USAGE (PEAK FRINGE SIZE (NUMBER OF NODES)): {memory}')
print(f'Time: {end-start}')