Alex Hemmerlin
Nathan Steiger
COMP 445 Intro to AI
N-Puzzle, A*, and RBFS

n-puzzle:
The NPuzzle.py file implements instances of n-puzzles and all of the necessary methods.

Alex Hemmerlin
A* Search:
    The AStarSearch.py file contains the implemented A* search algorithm. Running the AStarSearch.py file
as main shows the algorithm solving a simple instance of the 8-puzzle. This instance is illustrated below:
    [1 2 3]
    [4 8 5]
    [7 0 6]
The main() method inside of the AStarSearch.py file contains one TODO comment. This comment gives instructions
on how to change the verbosity parameter of the search to see more detailed information about the algorithm as
it is running. Simply change the verbosity inside of the AStarSearch() method call to the desired level.
    The test results of running A* search on random puzzle instances are in the AStarResults.py file.

Nathan Steiger
RBFS (Recursive Best First Search):
    The RBFS.py file contains the implemented Recursive Best First Search. Running ths file will run main() 
using RBFS solving a simple instance of the 8-puzzle. The instance is the same as the one used in AStarSearch.py 
and represented above. Verbosity is used the same way as A*.
    The test results of running RBFS on random puzzle instances are in the RBFSResults.py file.