# Author: Alex Hemmerlin
# This file implements A* Search

from NPuzzle import NPuzzle
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Node:
    priority: int
    puzzle: NPuzzle=field(compare=False)
    parent: NPuzzle=field(compare=False)

def in_list(item, list):
    for val in list:
        if val == item:
            return True
    return False

def AStarSearch(puzzle: NPuzzle, verbosity: int = 0) -> Node:
    h = puzzle.manhatten_distance()
    g = 0

    fringe = PriorityQueue()
    fringe.put(Node(h+g, puzzle, None))
    closed = []
    while not fringe.empty():
    
        # get the best item in the fringe
        parent: Node = fringe.get()

        # check if it is the goal
        if parent.puzzle.is_solved():
            return parent

        # add it to the closed list
        closed.append(parent.puzzle.state)

        # TODO: generate successors
        # - give them values
        # - check if they are already in the fringe
        # - if they are, keep the best path
        # - if they aren't add them to the fringe

        g += 1
        # Generate Successors (4 possible moves)
        for i in range(4):
            # generate copy to manipulate
            successor: NPuzzle = NPuzzle(parent.puzzle.n, parent.puzzle.state)

            if i == 0 and successor.move_up():
                # Check the closed list for this state
                if not in_list(successor.state, closed):
                    s_node: Node = Node(successor.manhatten_distance()+g, successor, parent)
                    # TODO: check the fringe for ths state
                    fringe.put(s_node)

            elif i == 1 and successor.move_right():
                # Check the closed list for this state
                if not in_list(successor.state, closed):
                    s_node: Node = Node(successor.manhatten_distance()+g, successor, parent)
                    fringe.put(s_node)

            elif i == 2 and successor.move_down():
                # Check the closed list for this state
                if not in_list(successor.state, closed):
                    s_node: Node = Node(successor.manhatten_distance()+g, successor, parent)
                    fringe.put(s_node)

            elif i == 3 and successor.move_left():
                # Check the closed list for this state
                if not in_list(successor.state, closed):
                    s_node: Node = Node(successor.manhatten_distance()+g, successor, parent)
                    fringe.put(s_node)
    

if __name__ == '__main__':
    myQ = PriorityQueue()

    item1 = Node(10,'hi', None)
    item2 = Node(2,'hello', None)
    item3 = Node(5,'bye', None)

    myQ.put(item1)
    myQ.put(item2)
    myQ.put(item3)

    print(myQ.get())
    print(myQ.get())
    print(myQ.get())

    c = []
    p1 = NPuzzle(8, [[1,2,3],[4,5,6],[7,8,0]])
    p2 = NPuzzle(8, [[1,2,3],[4,5,6],[7,8,0]])

    c.append(p1.state)
    print(c[0] == p2.state)

