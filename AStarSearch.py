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
    parent: Any=field(compare=False)

def in_list(item, list):
    for val in list:
        if val == item:
            return True
    return False

def generate_successor(successor: NPuzzle, parent: Node, g: int, fringe: PriorityQueue, closed: list, verbosity: int):
    # Check the closed list for this state
    if not in_list(successor.state, closed):
        s_node: Node = Node(successor.manhatten_distance()+g, successor, parent)
        if verbosity == 2:
            print(f'Generating successor: {s_node.puzzle.state}')
            print(f'With a priority of: {s_node.priority}')
            print()
        # TODO: check the fringe for this state and value
        fringe.put(s_node)

def AStarSearch(puzzle: NPuzzle, verbosity: int = 0) -> Node:
    """Performs A* Search on the given puzzle instance using the manhatten distance heuristic

    With a verbosity greater than 0 prints out extra information
    Returns . . . (Not sure yet lol)
    """

    h = puzzle.manhatten_distance()
    g = 0

    fringe = PriorityQueue()
    fringe.put(Node(h+g, puzzle, None))
    closed = []
    while not fringe.empty():
    
        # get the best item in the fringe
        parent: Node = fringe.get()

        if verbosity >= 1:
            print(f'State removed from fringe: {parent.puzzle.state}')
            print(f'With a priority of: {parent.priority}')
            if verbosity == 2:
                if parent.parent is not None:
                    print(f'This states parent is: {parent.parent.puzzle.state}')
                else:
                    print(f'This state has no parent (start state)')
            print()

        # check if it is the goal
        if parent.puzzle.is_solved:
            return parent

        # add it to the closed list
        closed.append(parent.puzzle.state)

        # Increment the total path distance by one (one more move)
        g += 1

        # Generate Successors (4 possible moves)
        for i in range(4):
            # generate copy to manipulate
            successor: NPuzzle = NPuzzle(parent.puzzle.n, parent.puzzle.state)

            if i == 0 and successor.move_up():
                generate_successor(successor, parent, g, fringe, closed, verbosity)
            if i == 1 and successor.move_right():
                generate_successor(successor, parent, g, fringe, closed, verbosity)
            if i == 2 and successor.move_down():
                generate_successor(successor, parent, g, fringe, closed, verbosity)
            if i == 3 and successor.move_left():
                generate_successor(successor, parent, g, fringe, closed, verbosity)

    return False


if __name__ == '__main__':
    p1 = NPuzzle(8, [[1,2,3],[4,0,5],[7,8,6]])
    result = AStarSearch(p1, 2)

    if result != False:
        print(result.priority)
        print(result.puzzle.state)
        print(result.parent)
    else:
        print('bad')
