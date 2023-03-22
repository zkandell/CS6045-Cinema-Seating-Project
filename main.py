from Theatres import Theatre_Greedy
from Theatres import Theatre_Greedy_Shapes

# Theatre being tested is Tillburg_4 0.7
fname = 'test_theatre.txt'

# Simple example theatre from the paper
#fname = 'simple_theatre.txt'

test = Theatre_Greedy(fname)
test.seat_greedy()
test.analyze_results()
test.print_results()

shapetest = Theatre_Greedy_Shapes(fname)
shapetest.seat_greedy()
shapetest.analyze_results()
shapetest.print_results()