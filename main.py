from cinema_greedy import Cinema_Greedy
from cinema_greedy_shapes import Cinema_Greedy_Shapes

# Cinema being tested is Tillburg_4 0.7
fname = 'test_cinema.txt'

# Simple example cinema from the paper
#fname = 'simple_cinema.txt'

test = Cinema_Greedy(fname)
test.seat_greedy()
test.analyze_results()
test.print_results()

shapetest = Cinema_Greedy_Shapes(fname)
shapetest.seat_greedy()
shapetest.analyze_results()
shapetest.print_results()