# CS6045-Cinema-Seating-Project

This code requires numpy to be installed in order to run. 

To recreate the data used to analyze these formulas, run TestAllCinemas.py. For a general demonstration of the algorithm and its and outputs, run Demo.py. 

Data for cinema layouts taken from https://github.com/maxstoll94/master-thesis-phase-2. 

Cinema layout file overview

Cinema files are formatted like this:

2
7
1110111
1110111
0 2 0 0 0 0 0 0

Here is what each of the lines means:

Line 1: The number of rows in the cinema
Line 2: The number of seats in each row
Line 3 through second-last line: The layout of seats in the cinema. 1s represent open seats, 0s represent spaces that are not seats (usually aisles)
Last line: The groups that need to be seated. This will seat groups of up to 8 people, and each number represents the number of groups of that size that wish to be seated - for example, in the above, 2 groups of 2 are being seated, with no groups of other sizes. 



The final result of the Greedy and Greedy Shapes algorithm is a numpy array that looks like this:

[[2 2 1 0 1 2 2]
 [1 1 1 0 1 1 1]]
 
 This works the same way as in the cinema layout file, with 2s representing occupied seats.
