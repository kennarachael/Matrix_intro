import unittest
import random
from matrix import MiningGrid

class TestMiningGrid(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh MiningGrid for each test"""
        self.mg = MiningGrid()


    def test_generate_random(self):
        """Test if grid generates with correct dimensions and values within range"""
        random.seed(42)  # Set seed for reproducibility
        self.mg.generate_random(5, 5, 10, 50, empty_factor=0)

        # Ensure grid has correct dimensions
        self.assertEqual(len(self.mg.grid), 5)
        self.assertEqual(len(self.mg.grid[0]), 5)

        # Ensure all values are within the given range
        for row in self.mg.grid:
            for value in row:
                self.assertTrue(10 <= value <= 50)

    def test_set_and_get(self):
        """Test setting and getting values in the grid"""
        self.mg.generate_random(3, 3, 10, 50, empty_factor=0)
        self.mg.set((1, 1), 99)

        self.assertEqual(self.mg.get((1, 1)), 99)

    def test_mine_sector(self):
        """Test mining from a sector"""
        self.mg.grid = [
            [10, 20, 30],
            [40, 90, 50],
            [60, 70, 80]
        ]

        mined = self.mg.mine_sector((0, 1), 30) # Mine 30 from the current 40

        self.assertEqual(mined, 30)
        self.assertEqual(self.mg.get((0, 1)), 10) # 10 remains

    def test_bulk_mine(self):
        """Test mining multiple sectors"""
        self.mg.generate_random(3, 3, 50, 50, empty_factor=0)
        total_mined = self.mg.bulk_mine([(0, 0, 20), (1, 1, 30), (0,1,100)])

        self.assertEqual(total_mined, 100)
        self.assertEqual(self.mg.get((0, 0)), 30)
        self.assertEqual(self.mg.get((1, 1)), 20)
        self.assertEqual(self.mg.get((0, 1)), 0)

    def test_find_richest_sector(self):
        """Test identifying the richest sector"""
        self.mg.grid = [
            [10, 20, 30],
            [40, 90, 50],
            [60, 70, 80]
        ]
        richest = self.mg.find_richest_sector()
        self.assertEqual(richest, (1, 1, 90))  # (row, column, value)

    def test_find_depleted_sectors(self):
        """Test finding all depleted sectors"""
        self.mg.grid = [
            [10,  0, 30],
            [40,  0, 50],
            [ 0, 70,  0]
        ]
        depleted = self.mg.find_depleted_sectors()
        expected = [(0, 1), (1, 1), (2, 0), (2, 2)]
        self.assertEqual(depleted, expected)

    def test_average_resource_level(self):
        """Test computing the average resource level"""
        self.mg.grid = [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ]
        avg = self.mg.average_resource_level()
        self.assertEqual(avg, 50.0)  # (sum of all values) / 9



if __name__ == '__main__':
    unittest.main()
