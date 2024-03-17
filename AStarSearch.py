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
    """True if the specified item is in the list, False otherwise"""

    for val in list:
        if val == item:
            return True
    return False

def generate_successor(successor: NPuzzle, parent: Node, fringe: list[Node], closed: list, verbosity: int):
    """Generates the successor node for the given puzzle and checks the fringe for other paths to it"""

    # Check the closed list for this state: if not in the closed list generate the state
    if not in_list(successor.state, closed):
        # Create the node for this state
        s_node: Node = Node(successor.manhatten_distance()+parent.moves+1, successor, parent, parent.moves+1)

        # Debugging info
        if verbosity >= 2:
            print(f'Generating successor:\n{s_node.puzzle.string()}', end="")
            print(f'With a priority of: {s_node.priority}')
            if verbosity == 2:
                print()
        # check the fringe for this state and value
        for val in fringe:
            # if the state is in the fringe with better path to it, just return
            if s_node.puzzle.state == val.puzzle.state and s_node.priority > val.priority:
                if verbosity >= 3:
                    print('Successor NOT added to fringe (a better path has already been found)')
                return 1
            # else if this state has the better path, replace it in the fringe
            elif s_node.puzzle.state == val.puzzle.state and s_node.priority < val.priority:
                if verbosity >= 3:
                    print('Successor REPLACES other state/path in the fringe (better than the previoulsy found path)')
                fringe.remove(val)
                break

        # Add the node to the fringe
        if verbosity >= 3:
            print('Successor added to fringe')
            if verbosity != 2:
                print()
        fringe.append(s_node)
        # Re organize the fringe (re heap the min heap to keep the priority queue)
        heapq.heapify(fringe)
        return 1

    return 0

def AStarSearch(puzzle: NPuzzle, verbosity: int = 0) -> Node:
    """Performs A* Search on the given puzzle instance using the manhatten distance heuristic

    With a verbosity greater than 0 the program prints out extra information (can be set to 0, 1, 2, or 3)
    Returns . . . (Not sure yet lol)
    Loosely based on the psuedocode found here: https://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
    Also based on the discussion of A* in class and the notes from the lecture
    """

    # Initialize the variables to measure runtime and memory
    num_nodes_generated = 0
    peak_fringe_size = 0

    # Initialize the fringe with the starting state
    fringe = []
    fringe.append(Node(puzzle.manhatten_distance(), puzzle, None, 0))
    # Initialize the closed list
    closed = []

    # While the fringe is not empty: loop
    while len(fringe) > 0:
    
        # Update the memory tracking variable to measure peak fringe size
        if len(fringe) > peak_fringe_size:
            peak_fringe_size = len(fringe)

        # get the best item in the fringe
        parent: Node = fringe.pop(0)

        # Debugging info
        if verbosity >= 1:
            print(f'State removed from fringe:\n{parent.puzzle.string()}', end="")
            print(f'With a priority of: {parent.priority}')
            if verbosity >= 2:
                if parent.parent is not None:
                    print(f'This states parent is:\n{parent.parent.puzzle.string()}', end="")
                else:
                    print(f'This state has no parent (start state)')
            print()

        # check if it is the goal: if goal -> return
        if parent.puzzle.is_solved:
            if verbosity >= 1:
                print('GOAL FOUND')
            return (parent, num_nodes_generated, peak_fringe_size)

        # add it to the closed list: we are exploring it
        closed.append(parent.puzzle.state)
        if verbosity >= 3:
            print(f'State added to closed list:\n{parent.puzzle.string()}')

        # Generate Successors (4 possible moves: up, down, left, right)
        for i in range(4):
            # generate copy of the puzzle to manipulate
            successor: NPuzzle = NPuzzle(parent.puzzle.n, parent.puzzle.state)
            
            # make the moves and generate the successors
            if i == 0 and successor.move_up():
                num_nodes_generated += generate_successor(successor, parent, fringe, closed, verbosity)
            if i == 1 and successor.move_right():
                num_nodes_generated += generate_successor(successor, parent, fringe, closed, verbosity)
            if i == 2 and successor.move_down():
                num_nodes_generated += generate_successor(successor, parent, fringe, closed, verbosity)
            if i == 3 and successor.move_left():
                num_nodes_generated += generate_successor(successor, parent, fringe, closed, verbosity)

    # if the fringe is empty without finding a goal state, then the puzzle is unsolvable so return false
    return False

def get_path(result: Node):
    path = []
    path.append(result.puzzle)
    parent: Node = result.parent
    while parent is not None:
        path.append(parent.puzzle)
        parent = parent.parent
    return path

def main():
    p1 = NPuzzle(8, [[1,2,3],[4,8,5],[7,0,6]])

    print('STARTING STATE:')
    
    print(p1.string())

    print('SEARCHING')

    # TODO: CHANGE VERBOSITY PARAMETER TO SEE MORE DETAILED ALGORITHM INFORMATION (Ranges from [0,3])
    result, runtime, memory = AStarSearch(puzzle = p1, verbosity = 2)

    print('SEARCH COMPLETE')
    path = get_path(result)

    print(f'PATH LENGTH: {result.moves}')
    print('PATH:')
    while len(path) > 0:
        print(path.pop(len(path)-1).string())

    print(f'RUNTIME (TOTAL NUMBER OF NODES GENERATED): {runtime}')
    print(f'MEMORY USAGE (PEAK FRINGE SIZE (NUMBER OF NODES)): {memory}')

if __name__ == '__main__':
    main()
