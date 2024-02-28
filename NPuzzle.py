import math

class NPuzzle:
    """Stores the state and methods of an n-puzzle.
    
    When initialized, creates a randomly generated n-puzzle state
    that is guarenteed to be solvable. May also initialize the puzzle
    with a chosen state specified by the input arguments.*

    *Note: n+1 must be a perfect square.
    *Note: When given a starting state, init DOES NOT check for illegal states.
    """

    state: list[list[int]]
    n: int

    def __init__(self, n: int, state: list[list[int]] = None):
        self.n = n
        if not math.sqrt(n+1).is_integer():
            raise Exception("n+1 must be a perfect square")
        # TODO: Randomize self.state
        if state is not None:
            self.state = state
        else:
            self.state = self.goal_state

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
        """Returns the location of the blank space in the puzzle.
        
        Location is in the form of (row, column), zero indexed.
        """

        for row in self.state:
            for val in row:
                if val == tile:
                    return (self.state.index(row), row.index(val))
