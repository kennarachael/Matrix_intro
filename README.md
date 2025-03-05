# Matrix_intro
A 2D list (also called a nested list) is a list where each element is itself a list. It is useful for representing data in rows and columns, like a spreadsheet or a grid.

Example: Representing a Space Mining Grid
Imagine a mining operation on an asteroid where we track mineral deposits in a grid. Each cell in the grid represents a section of the asteroid, and its value represents the amount of a specific mineral found there.


asteroid_grid = [
    [2, 5, 3],
    [0, 4, 7],
    [6, 1, 8]
]

# Accessing values
print(asteroid_grid[0][1])  # Output: 5 (Row 0, Column 1)
Working with 2D Lists
Iterating through a 2D List
We can use nested loops to process all elements in a 2D list.

for value in row:
    print(value, end=" ")
print()  # New line after each row
Modifying Elements

# Updating the mineral deposit at Row 2, Column 1
asteroid_grid[2][1] = 9
3. Practical Problem: Space Mining Scanning System
Problem Statement
AstroMining Inc. needs an automated scanning system to analyze mineral concentrations on different asteroid sectors. You will:

Create a 5x5 grid representing mineral deposits (random values between 1 and 10).
Calculate the total minerals in each row and identify the richest sector.
Find the average mineral concentration per sector across the entire grid.
Starter Code
import random



	
  
