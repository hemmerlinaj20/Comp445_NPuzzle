# Author: Alex Hemmerlin
# This file implements A* Search

from NPuzzle import NPuzzle
from typing import Any
import heapq

class Node:
    """Data class to store an 8 puzzle state and some useful information

    - priority: priority in the fringe, made up of manhatten distance and number of moves to get there
    - puzzle: the NPuzzle object at the state
    - parent: the NPuzzle that this NPuzzle came from (will be one move behind)
    - moves: the number of moves it took to get to this state
    """
    priority: int
    puzzle: NPuzzle
    parent: NPuzzle
    moves: int
    def __init__(self, priority, puzzle, parent, moves):
        self.priority = priority
        self.puzzle = puzzle
        self.parent = parent
        self.moves = moves
    def __lt__(self, other):
        return self.priority < other.priority
    def __gt__(self, other):
        return self.priority > other.priority
    def __le__(self, other):
        return self.priority <= other.priority
    def __ge__(self, other):
        return self.priority >= other.priority
    def __eq__(self, other):
        return self.priority == other.priority
    def __ne__(self, other):
        return self.priority != other.priority

def in_list(item, list):
    for val in list:
        if val == item:
            return True
    return False

def generate_successor(successor: NPuzzle, parent: Node, fringe: list[Node], closed: list, verbosity: int):
    # Check the closed list for this state: if not in the closed list generate the state
    if not in_list(successor.state, closed):
        # Create the node for this state
        s_node: Node = Node(successor.manhatten_distance()+parent.moves+1, successor, parent, parent.moves+1)

        # Debugging info
        if verbosity == 2:
            print(f'Generating successor: {s_node.puzzle.state}')
            print(f'With a priority of: {s_node.priority}')
            print()
        # check the fringe for this state and value
        for val in fringe:
            # if the state is in the fringe with better path to it, just return
            if s_node.puzzle.state == val.puzzle.state and s_node.priority > val.priority:
                return
            # else if this state has the better path, replace it in the fringe
            elif s_node.puzzle.state == val.puzzle.state and s_node.priority < val.priority:
                fringe.remove(val)
                break

        # Add the node to the fringe
        fringe.append(s_node)
        # Re organize the fringe (re heap the min heap to keep the priority queue)
        heapq.heapify(fringe)
    return

def AStarSearch(puzzle: NPuzzle, verbosity: int = 0) -> Node:
    """Performs A* Search on the given puzzle instance using the manhatten distance heuristic

    With a verbosity greater than 0 prints out extra information
    Returns . . . (Not sure yet lol)
    Loosely based on the psuedocode found here: https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
    Also based on the discussion of A* in class and the notes from the lecture
    """

    # Initialize the fringe with the starting state
    fringe = []
    fringe.append(Node(puzzle.manhatten_distance(), puzzle, None, 0))
    # Initialize the closed list
    closed = []

    # While the fringe is not empty: loop
    while len(fringe) > 0:
    
        # get the best item in the fringe
        parent: Node = fringe.pop(0)

        # Debugging info
        if verbosity >= 1:
            print(f'State removed from fringe: {parent.puzzle.state}')
            print(f'With a priority of: {parent.priority}')
            if verbosity == 2:
                if parent.parent is not None:
                    print(f'This states parent is: {parent.parent.puzzle.state}')
                else:
                    print(f'This state has no parent (start state)')
            print()

        # check if it is the goal: if goal -> return
        if parent.puzzle.is_solved:
            return parent

        # add it to the closed list: we are exploring it
        closed.append(parent.puzzle.state)

        # Generate Successors (4 possible moves: up, down, left, right)
        for i in range(4):
            # generate copy of the puzzle to manipulate
            successor: NPuzzle = NPuzzle(parent.puzzle.n, parent.puzzle.state)
            
            # make the moves and generate the successors
            if i == 0 and successor.move_up():
                generate_successor(successor, parent, fringe, closed, verbosity)
            if i == 1 and successor.move_right():
                generate_successor(successor, parent, fringe, closed, verbosity)
            if i == 2 and successor.move_down():
                generate_successor(successor, parent, fringe, closed, verbosity)
            if i == 3 and successor.move_left():
                generate_successor(successor, parent, fringe, closed, verbosity)

    # if the fringe is empty without finding a goal state, then the puzzle is unsolvable so return false
    return False


if __name__ == '__main__':
    p1 = NPuzzle(8)
    print("Original --------------")
    print(p1.string())
    print('-----------------------')
    #print('Search started')
    result = AStarSearch(p1)
    #print('Finished Search')

    #print(result.priority)
    #print(result.puzzle.string())
    #print(result.parent.puzzle.state)
    #print()

    parent = result.parent
    while parent is not None:
        print(parent.puzzle.string())
        parent = parent.parent

    print(f'Moves: {result.moves}')
