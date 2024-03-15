# Author: Alex Hemmerlin
# This file implements A* Search

from NPuzzle import NPuzzle
from PriorityQueue import PriorityQueue

def AStarSearch(puzzle: NPuzzle, verbosity: int = 0):
    h = puzzle.manhatten_distance()
    g = 0

    fringe = PriorityQueue()
    fringe.insert((puzzle, h+g))
    closed_list = []
    while len(fringe) > 0:
        pass
        # TODO: get the best item in the fringe
        parent: NPuzzle = fringe.dequeue()[0]

        # TODO: check if it is the goal
        if parent.is_solved:
            return parent

        # TODO: add it to the closed list

        # TODO: loop through neighbors
        # - give them values
        # - check if they are already in the fringe
        # - if they are, keep the best path
        # - if they aren't add them to the fringe

if __name__ == '__main__':
    myQ = PriorityQueue()
    myQ.insert(('hi',5))
    myQ.insert(('hello',10))
    myQ.insert(('bye',1))

    print(myQ.isEmpty())
    print(myQ.dequeue())
    print(myQ.dequeue())
    print(myQ.dequeue())
    print(myQ.isEmpty())
