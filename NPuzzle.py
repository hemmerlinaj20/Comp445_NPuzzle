# Author: Alex Hemmerlin

import math
import random
import copy

class NPuzzle:
    """Stores the state and methods of an n-puzzle.
    
    When initialized, creates a randomly generated n-puzzle state
    that is guarenteed to be solvable. May also initialize the puzzle
    with a chosen state specified by the input arguments.*

    *Note: n+1 must be a perfect square.
    *Note: When given a starting state, init DOES NOT check for illegal states. So be sure to
    check that the assigned state is a legal n-puzzle format. Any given state is not guarenteed
    to be solvable. Undefined behaviour may occur if given an illegal/improper starting instance.
    *Note: When given a starting state, a deep copy is made
    """

    state: list[list[int]]
    n: int

    def __init__(self, n: int, state: list[list[int]] = None):
        self.n = n
        if not math.sqrt(n+1).is_integer():
            raise Exception("n+1 must be a perfect square")
        if state is not None:
            self.state = copy.deepcopy(state)
        else:
            self.state = self.goal_state
            self.__randomize__()

    @property
    def goal_state(self) -> list[list[int]]:
        """Returns the goal state of the n-puzzle.
        
        The goal state is defined as all of the numbers are arranged in ascending order
        left to right and top to bottom with the blank space (0) in the bottom right corner.
        """

        base = int(math.sqrt(self.n+1))
        goal_state = []
        for i in range(base):
            goal_state.append([])
        val = 1
        for row in goal_state:
            for i in range(base):
                if val == self.n+1:
                    row.append(0)
                else:
                    row.append(val)
                val += 1
        return goal_state
        
    @property
    def is_solved(self) -> bool:
        """Returns True if the n-puzzle is in the goal state."""

        if self.state == self.goal_state:
            return True
        else:
            return False
    
    def move_up(self) -> bool:
        """Moves the blank space (0) up by one
        
        Returns True if the move succeeds.
        Returns False if the blank space cannot be moved up. For example,
        if the blank space is already at the top of the puzzle.
        """

        zero_loc = self.__find_tile__(0)
        above_zero = (zero_loc[0]-1, zero_loc[1])
        # Checks if the blank space is at the top of the puzzle
        if above_zero[0] < 0:
            return False
        # Moves the space
        val_above = self.state[above_zero[0]][above_zero[1]]
        self.state[above_zero[0]][above_zero[1]] = 0
        self.state[zero_loc[0]][zero_loc[1]] = val_above
        return True
    
    def move_down(self) -> bool:
        """Moves the blank space (0) down by one
        
        Returns True if the move succeeds.
        Returns False if the blank space cannot be moved down. For example,
        if the blank space is already at the bottom of the puzzle.
        """

        zero_loc = self.__find_tile__(0)
        below_zero = (zero_loc[0]+1, zero_loc[1])
        # Checks if the blank space is at the bottom of the puzzle
        if below_zero[0] > math.sqrt(self.n+1)-1:
            return False
        # Moves the space
        val_below = self.state[below_zero[0]][below_zero[1]]
        self.state[below_zero[0]][below_zero[1]] = 0
        self.state[zero_loc[0]][zero_loc[1]] = val_below
        return True

    def move_left(self) -> bool:
        """Moves the blank space (0) left by one
        
        Returns True if the move succeeds.
        Returns False if the blank space cannot be moved left. For example,
        if the blank space is already at the far left of the puzzle.
        """

        zero_loc = self.__find_tile__(0)
        left_of_zero = (zero_loc[0], zero_loc[1]-1)
        # Checks if the blank space is at the far left of the puzzle
        if left_of_zero[1] < 0:
            return False
        # Moves the space
        val_left = self.state[left_of_zero[0]][left_of_zero[1]]
        self.state[left_of_zero[0]][left_of_zero[1]] = 0
        self.state[zero_loc[0]][zero_loc[1]] = val_left
        return True

    def move_right(self) -> bool:
        """Moves the blank space (0) right by one
        
        Returns True if the move succeeds.
        Returns False if the blank space cannot be moved right. For example,
        if the blank space is already at the far right of the puzzle.
        """

        zero_loc = self.__find_tile__(0)
        right_of_zero = (zero_loc[0], zero_loc[1]+1)
        # Checks if the blank space is at the far right of the puzzle
        if right_of_zero[1] > math.sqrt(self.n+1)-1:
            return False
        # Moves the space
        val_right = self.state[right_of_zero[0]][right_of_zero[1]]
        self.state[right_of_zero[0]][right_of_zero[1]] = 0
        self.state[zero_loc[0]][zero_loc[1]] = val_right
        return True

    def __find_tile__(self, tile: int) -> tuple[int, int]:
        """Returns the location of the specified tile in the puzzle.
        
        Location is in the form of (row, column), zero indexed.
        """

        for row in self.state:
            for val in row:
                if val == tile:
                    return (self.state.index(row), row.index(val))
                
    def __randomize__(self):
        """Randomizes the state of the puzzle.
        
        Randomly performs 1000 moves on the puzzle to randomize the tile positions
        """

        for i in range(0,1000):
            num = random.randrange(0,1000)/1000
            if num < .25:
                self.move_up()
            elif num < .5:
                self.move_down()
            elif num < .75:
                self.move_left()
            else:
                self.move_right()

    def manhatten_distance(self) -> int:
        """Returns the total manhatten distance of the combined tiles
        
        Calculates the manhatten distance of each tile and returns the sum of the distances.
        """

        dist = 0
        for tile in range(1, self.n+1):
            dist += self.__manhatten_helper__(tile)
        return dist

    def __manhatten_helper__(self, tile: int) -> int:
        """Calculates and returns the manhatten distance for the specified tile."""

        tile_loc = self.__find_tile__(tile)
        dist = abs(tile_loc[0] - self.solved_positions[tile][0]) + abs(tile_loc[1] - self.solved_positions[tile][1])
        #print(f'Tile: {tile} Dist: {dist}')
        return dist
    
    def string(self):
        s = ""
        for l in self.state:
            s += f'[ '
            for val in l:
                s += f'{val} '
            s += ']\n'
        return s
    
    @property
    def solved_positions(self) -> dict[int:tuple[int,int]]:
        """The positions of each tile when the puzzle is solved.
        
        A dictionary mapping int (tile) to its solved position (tuple[int, int])
        """

        solved_positions = {}
        t = 1
        for row in range(0, int(math.sqrt(self.n+1))):
            for col in range(0, int(math.sqrt(self.n+1))):
                solved_positions[t] = (row, col)
                t += 1
        return solved_positions

if __name__ == '__main__':
    p1 = NPuzzle(15)
    p2 = NPuzzle(15)

    print(p1.state)
    print(p1.manhatten_distance())
    print(p2.state)
    print(p2.manhatten_distance())