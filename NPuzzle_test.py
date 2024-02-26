import unittest
from NPuzzle import NPuzzle

class NPuzzle_tests(unittest.TestCase):

    def test_init(self):
        eight_puzzle = [[1,2,3],[4,5,6],[7,8,0]]
        my_8puzzle = NPuzzle(8)
        self.assertEqual(my_8puzzle.state, eight_puzzle, 'Init Failed on 8 puzzle')
        fifteen_puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        my_15puzzle = NPuzzle(15)
        self.assertEqual(my_15puzzle.state, fifteen_puzzle, 'Init Failed on 15 puzzle')

    def test_goal_state(self):
        goal_8puzzle = [[1,2,3],[4,5,6],[7,8,0]]
        goal_15puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        my_8puzzle = NPuzzle(8)
        my_15puzzle = NPuzzle(15)
        self.assertEqual(my_8puzzle.goal_state, goal_8puzzle, 'Goal State Failed on 8 puzzle')
        self.assertEqual(my_15puzzle.goal_state, goal_15puzzle, 'Goal State Failed on 15 puzzle')

    def test_find_tile(self):
        my_8puzzle = NPuzzle(8)
        loc_0 = (2,2)
        self.assertEqual(my_8puzzle.__find_tile__(0), loc_0, 'Find Tile Failed')
        loc_1 = (0,0)
        self.assertEqual(my_8puzzle.__find_tile__(1), loc_1, 'Find Tile Failed')
        loc_5 = (1,1)
        self.assertEqual(my_8puzzle.__find_tile__(5), loc_5, 'Find Tile Failed')
        loc_4 = (1,0)
        self.assertEqual(my_8puzzle.__find_tile__(4), loc_4, 'Find Tile Failed')

        [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        my_15puzzle = NPuzzle(15)
        loc_0 = (3,3)
        loc_12 = (2,3)
        loc_15 = (3,2)
        loc_4 = (0,3)
        self.assertEqual(my_15puzzle.__find_tile__(0), loc_0, 'Find Tile Failed')
        self.assertEqual(my_15puzzle.__find_tile__(12), loc_12, 'Find Tile Failed')
        self.assertEqual(my_15puzzle.__find_tile__(15), loc_15, 'Find Tile Failed')
        self.assertEqual(my_15puzzle.__find_tile__(4), loc_4, 'Find Tile Failed')

    def test_move_up(self):
        eight_puzzle_after_one_move = [[1,2,3],[4,5,0],[7,8,6]]
        my_8puzzle = NPuzzle(8)
        self.assertTrue(my_8puzzle.move_up(), 'Move Up Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_one_move, 'Move Up Failed: Action')
        eight_puzzle_after_two_moves = [[1,2,0],[4,5,3],[7,8,6]]
        self.assertTrue(my_8puzzle.move_up(), 'Move Up Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Up Failed: Action')
        self.assertFalse(my_8puzzle.move_up(), 'Move Up Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Up Failed: Action')

        fifteen_puzzle_one_move = [[1,2,3,4],[5,6,7,8],[9,10,11,0],[13,14,15,12]]
        my_15puzzle = NPuzzle(15)
        self.assertTrue(my_15puzzle.move_up(), 'Move Up Failed: Return')
        self.assertEqual(my_15puzzle.state, fifteen_puzzle_one_move, 'Move Up Failed: Action')
        self.assertTrue(my_15puzzle.move_up(), 'Move Up Failed: Return')
        self.assertTrue(my_15puzzle.move_up(), 'Move Up Failed: Return')
        self.assertFalse(my_15puzzle.move_up(), 'Move Up Failed: Return')

    def test_move_down(self):
        my_8puzzle = NPuzzle(8)
        my_8puzzle.move_up()
        my_8puzzle.move_up()
        self.assertTrue(my_8puzzle.move_down(), 'Move Down failed: Return')
        eight_puzzle_after_one_move = [[1,2,3],[4,5,0],[7,8,6]]
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_one_move, 'Move Down Failed: Action')
        self.assertTrue(my_8puzzle.move_down(), 'Move Down failed: Return')
        eight_puzzle_after_two_moves = [[1,2,3],[4,5,6],[7,8,0]]
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Down Failed: Action')
        self.assertFalse(my_8puzzle.move_down(), 'Move Down failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Down Failed,: Action')

        fifteen_puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        my_15puzzle = NPuzzle(15)
        my_15puzzle.move_up()
        self.assertTrue(my_15puzzle.move_down(), 'Move Down Failed: Return')
        self.assertEqual(my_15puzzle.state, fifteen_puzzle, 'Move Down Failed: Action')
        self.assertFalse(my_15puzzle.move_down(), 'Move Down Failed: Return')

    def test_is_solved(self):
        my_8puzzle = NPuzzle(8)
        self.assertTrue(my_8puzzle.is_solved, 'Is Solved Failed')
        my_8puzzle.move_up()
        self.assertFalse(my_8puzzle.is_solved, 'Is Solved Failed')
        my_8puzzle.move_down()
        self.assertTrue(my_8puzzle.is_solved, 'Is Solved Failed')

        my_15puzzle = NPuzzle(15)
        self.assertTrue(my_15puzzle.is_solved, 'Is Solved Failed')
        my_15puzzle.move_up()
        self.assertFalse(my_15puzzle.is_solved, 'Is Solved Failed')
        my_15puzzle.move_down()
        self.assertTrue(my_15puzzle.is_solved, 'Is Solved Failed')

    def test_move_left(self):
        eight_puzzle_after_one_move = [[1,2,3],[4,5,6],[7,0,8]]
        my_8puzzle = NPuzzle(8)
        self.assertTrue(my_8puzzle.move_left(), 'Move Left Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_one_move, 'Move Left Failed: Action')
        eight_puzzle_after_two_moves = [[1,2,3],[4,5,6],[0,7,8]]
        self.assertTrue(my_8puzzle.move_left(), 'Move Left Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Left Failed: Action')
        self.assertFalse(my_8puzzle.move_left(), 'Move Left Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Left Failed: Action')

        fifteen_puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]]
        my_15puzzle = NPuzzle(15)
        self.assertTrue(my_15puzzle.move_left(), 'Move Left Failed: Return')
        self.assertEqual(my_15puzzle.state, fifteen_puzzle, 'Move Left Failed: Action')
        self.assertTrue(my_15puzzle.move_left(), 'Move Down Failed: Return')
        self.assertTrue(my_15puzzle.move_left(), 'Move Down Failed: Return')
        self.assertFalse(my_15puzzle.move_left(), 'Move Down Failed: Return')

    def test_move_right(self):
        my_8puzzle = NPuzzle(8)
        my_8puzzle.move_left()
        my_8puzzle.move_left()
        eight_puzzle_after_one_move = [[1,2,3],[4,5,6],[7,0,8]]
        self.assertTrue(my_8puzzle.move_right(), 'Move Right Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_one_move, 'Move Right Failed: Action')
        eight_puzzle_after_two_moves = [[1,2,3],[4,5,6],[7,8,0]]
        self.assertTrue(my_8puzzle.move_right(), 'Move Right Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Right Failed: Action')
        self.assertFalse(my_8puzzle.move_right(), 'Move Right Failed: Return')
        self.assertEqual(my_8puzzle.state, eight_puzzle_after_two_moves, 'Move Right Failed: Action')

        fifteen_puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]]
        my_15puzzle = NPuzzle(15)
        my_15puzzle.move_left()
        my_15puzzle.move_left()
        self.assertTrue(my_15puzzle.move_right(), 'Move Right Failed: Return')
        self.assertEqual(my_15puzzle.state, fifteen_puzzle, 'Move Right Failed: Action')
        self.assertTrue(my_15puzzle.move_right(), 'Move Right Failed: Return')
        self.assertFalse(my_15puzzle.move_right(), 'Move Right Failed: Return')

if __name__ == '__main__':
    unittest.main()