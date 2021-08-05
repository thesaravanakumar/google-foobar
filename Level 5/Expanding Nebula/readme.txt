    Expanding Nebula
    ================
    You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies.
    But - oh no! - one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start
    monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. However, you do find
    that the gas of the steadily expanding nebula follows a simple pattern, meaning that you should be able to determine
    the previous state of the gas and narrow down where you might find the pod.
    From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can
    model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its
    4 nearby cells, specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, and (4) the
    cell below and to the right of it. If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas,
    then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.
    For example, let's say the previous state of the grid (p) was:
    .O..
    ..O.
    ...O
    O...
    To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of
    cells around each cell.  Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, which
    means this 2x2 block would become cell c[0][0] with gas in the next time step:
    .O -> O
    ..
    Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], two of the
    containing cells have gas, so in the next state of the grid, c[0][1] will NOT have gas:
    O. -> .
    .O
    Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:
    O.O
    .O.
	O.O
	
	Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell 
	below and to the right of them, respectively.
	Write a function answer(g) where g is an array of array of bools saying whether there is gas in each cell (the current scan 
	of the nebula), and return an int with the number of possible previous states that could have resulted in that grid after 1 
	time step.  For instance, if the function were given the current state c above, it would deduce that the possible previous 
	states were p (given above) as well as its horizontal and vertical reflections, and would return 4. The width of the grid 
	will be between 3 and 50 inclusive, and the height of the grid will be between 3 and 9 inclusive.  The answer will always 
	be less than one billion (10^9).
		
    Test cases
    ==========
    Inputs:
        (boolean) g = [
                        [true, false, true],
                        [false, true, false],
                        [true, false, true]
                      ]
    Output:
        (int) 4
    Inputs:
        (boolean) g = [
                        [true, false, true, false, false, true, true, true],
                        [true, false, true, false, false, false, true, false],
                        [true, true, true, false, false, false, true, false],
                        [true, false, true, false, false, false, true, false],
                        [true, false, true, false, false, true, true, true]
                      ]
    Output:
        (int) 254
    Inputs:
        (boolean) g = [
                        [true, true, false, true, false, true, false, true, true, false],
                        [true, true, false, false, false, false, true, true, true, false],
                        [true, true, false, false, false, false, false, false, false, true],
                        [false, true, false, false, false, false, true, true, false, false]
                      ]
    Output:
        (int) 11567

## How this works:

1. The input matrix gets converted into a tuple of tuples to allow for hashing operations
2. The program creates a dictionary, where each key is a combination possible for the current (iteration) row, and the corresponding value is the amount of valid occurances.
3. The program iterates over each row to find each possible row given any of the previous rows, and stores the amount of valid occurances in the dictionary (most row combinations will have 0 valid occurances, depending on how the given matrix looks like)

### Time complexity
Consider the input matrix to be of size m times n
This program has a  time complexity of O(m<sup>2</sup> * 2<sup>n</sup>) (worst case), O(m * 2<sup>n</sup>) (best case), as the rows and columns are swapped. It is possible to vastly reduce the complexity (to O(m<sup>2</sup> * n<sup>2</sup>)) by not looking at all possible combinations per row, but instead per cell / 2 cells, depending on how many adjacent cells are precalculated.

If there is interest in this possible faster solution, let me know. I already know how to program it, but this solution sufficed for the constraints given in the task and was much simpler. The faster solution would allow you to calculate preimages for much bigger sizes of grids (for instance 50⨯50 would not be possible with the current solution).
