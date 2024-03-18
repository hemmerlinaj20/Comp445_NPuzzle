# Author: Nathan Steiger

from NPuzzle import NPuzzle
from typing import Any


class Node:
    """Data class to store an 8 puzzle state and some useful information

    - priority: priority in the fringe, made up of manhattan distance and number of moves to get there
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


def generate_successor(successor: NPuzzle, parent: Node, verbosity: int):
    """Generates the successor node for the given puzzle"""

    # Create the node for this state
    s_node: Node = Node(successor.manhatten_distance() + parent.moves + 1, successor, parent, parent.moves + 1)

    # Debugging info
    if verbosity >= 2:
        print(f'Generating successor:\n{s_node.puzzle.string()}', end="")
        print(f'With a priority of: {s_node.priority}')
        if verbosity == 2:
            print()

    return s_node



def RBFS(node: Node, f_limit: int, verbosity: int, num_nodes_generated: int = 0) -> Any:
    """Recursive Best-First Search algorithm"""

    # If the node is a goal state

    if node.puzzle.is_solved:
        return node, 0, num_nodes_generated

    # Generate successors
    successors = []
    for i in range(4):
        # generate copy of the puzzle to manipulate
        successor = node.puzzle.copy()

        # make the moves and generate the successors
        if i == 0 and successor.move_up():
            successors.append(generate_successor(successor, node, verbosity))
            num_nodes_generated += 1
        if i == 1 and successor.move_right():
            successors.append(generate_successor(successor, node, verbosity))
            num_nodes_generated += 1
        if i == 2 and successor.move_down():
            successors.append(generate_successor(successor, node, verbosity))
            num_nodes_generated += 1
        if i == 3 and successor.move_left():
            successors.append(generate_successor(successor, node, verbosity))
            num_nodes_generated += 1

    # If there are no successors
    if len(successors) == 0:
        return None, float('inf'), num_nodes_generated

    # Evaluate each successor
    for s in successors:
        s.priority = max(s.priority, node.priority)

    while True:
        # Sort the successors based on their priority
        successors.sort()

        # Best successor
        best = successors[0]

        # If best's priority is greater than the f-limit
        if best.priority > f_limit:
            return None, best.priority, num_nodes_generated

        # Second best's f-value
        alternative = successors[1].priority if len(successors) > 1 else float('inf')

        # Recursive call
        result, best.priority, num_nodes_generated = RBFS(best, min(f_limit, alternative), verbosity,
                                                          num_nodes_generated)

        # If a goal was found
        if result is not None:
            return result, best.priority, num_nodes_generated


def RBFS_Search(puzzle: NPuzzle, verbosity: int = 0) -> Node:
    """Performs Recursive Best-First Search on the given puzzle instance using the manhattan distance heuristic"""

    # Initialize the root node
    root = Node(puzzle.manhatten_distance(), puzzle, None, 0)

    # Call RBFS algorithm
    result, _, ng = RBFS(root, float('inf'), verbosity)

    return result, ng


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

    # TODO: CHANGE VERBOSITY PARAMETER TO SEE MORE DETAILED ALGORITHM INFORMATION (Ranges from [0,2])
    result, runtime = RBFS_Search(puzzle=p1, verbosity=2)

    print('SEARCH COMPLETE')
    path = get_path(result)

    print(f'PATH LENGTH: {result.moves}')
    print('PATH:')
    while len(path) > 0:
        print(path.pop(len(path) - 1).string())
    print(f'RUNTIME (TOTAL NUMBER OF NODES GENERATED): {runtime}')

if __name__ == '__main__':
    main()
