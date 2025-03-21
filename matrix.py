import random
from test_mining import TestMiningGrid

class MiningGrid:

    def __init__(self):
        self.grid = []

    def print_grid(self):

        for row in self.grid:
            print(" ".join(f"{num:>{6}}" for num in row))

    def generate(self):
        self.grid = [[1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5]]

    def generate_random(self, h, w, min_val, max_val):
        """
        Generates a grid of size width (h * w) filled with random values
        between min_val and max_val
        """
        

        for y in range(w):
            row =[]
            for x in range(h):
                row.append(random.randint(min_val,max_val))

            self.grid.append(row)

   

    def set_sector( self, location:tuple, val):
        x,y = location[0],location[1]
        self.grid[y][x] = val

    def mine_sector(self, location:tuple, amount:int):
        """
        Mines (removes) amount minerals at location. In the event not enough resources
        are present, they will all be mined and the sector would become 0 (depleted)

        Args:
        location: an (x,y) tuple of the location
        amount: an int representing the amount of minerals to be extracted

        Returns:
        int: the amount of minerals successfully mined


        """

        x,y = location[0],location[1]
        sector_val = self.grid[y][x]

        if sector_val  < amount:

            self.set_sector(location, 0)
            return sector_val

        else:
            self.set_sector(location, sector_val- amount)
            return self.grid[y][x]


    def bulk_mine(self, mine_list):
        """
        Mines the asteroid based on the locations and amount given in mine_list:

        Args:
        mine_list (tuple): a list of tuples (x,y,a) containing the x, y location and the amount to be mined
                            ex: [ (3,4,100), (4, 9, 70) ]
        Returns:
        the total amount mined from all locations
        """
        total = 0
        for sector in mine_list:
            x,y,a = sector[0],sector[1],sector[2]
            
            total +=self.mine_sector((x,y),a)
        return total


    def find_richest_sector(self):
        max_val = 0
        y_in = 0
        for x in self.grid:
            
            if max(x) > max_val:
                max_val = max(x)
                location = x.index(max_val)
                location_y =y_in
            y_in +=1

        return (location,location_y,max_val)  

    def find_depleted_sectors(self):
        min_val = max(self.grid[1])
        y_in = 0
        for x in self.grid:
            
            if min(x) < min_val:
                min_val = min(x)
                location = x.index(min_val)
                location_y =y_in
            y_in +=1

        return (location,location_y,min_val)         

    def average_resource_level(self):
        """
        Calculates the average resource level of the asteroid.
        """
        val = 0
        num = 0 
        for x in self.grid:
            for y in x:
                val += y
                num +=1
        return (val / num)

    def best_region(self):
        """
        Determines the best region (2x2 sectors) with the highest mineral count

        Returns:
        A list of 4 (x, y) tuples
        """
        


c = MiningGrid()
""""
    c.generate()
    c.print_grid()
    #print(c.mine_sector((1,2),5))
    print(c.bulk_mine([(4,2,9),(3,1,5)]))
    c.print_grid()
    c.find_richest_sector()
"""""
test  = TestMiningGrid()
test.test_find_richest_sector()