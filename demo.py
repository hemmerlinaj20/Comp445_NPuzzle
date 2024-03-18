# Author: Alex Hemmerlin

from NPuzzle import NPuzzle
from AStarSearch import AStarSearch, get_path
from RBFS import RBFS_Search

p = NPuzzle(8, [[1,2,3],[4,8,5],[7,0,6]])
#p = NPuzzle(15, [[1,2,3,4],[5,7,0,8],[9,6,11,12],[13,10,14,15]])

print('STARTING STATE:')
print(p.string())

print('SEARCHING')
result, runtime, memory = AStarSearch(puzzle = p)
#result, runtime = RBFS_Search(puzzle = p)
print('SEARCH COMPLETE')

path = get_path(result)
print(f'PATH LENGTH: {result.moves}')
print('PATH:')
while len(path) > 0:
    print(path.pop(len(path)-1).string())

print(f'RUNTIME (TOTAL NUMBER OF NODES GENERATED): {runtime}')
#print(f'MEMORY USAGE (PEAK FRINGE SIZE (NUMBER OF NODES)): {memory}')