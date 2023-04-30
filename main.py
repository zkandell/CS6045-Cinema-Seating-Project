from cinema_greedy import Cinema_Greedy
from cinema_greedy_shapes import Cinema_Greedy_Shapes
import time

# Cinema being tested is Tillburg_4 0.7
fname = 'test_cinema.txt'

# Simple example cinema from the paper
#fname = 'simple_cinema.txt'

print('Greedy Algorithm: ')
test = Cinema_Greedy(fname)
start = time.time()
test.seat_greedy()
end = time.time()
greedytime = end - start
test.analyze_results()
test.print_results()
print('Greedy time: ' + str(greedytime))

print('')

print('Greedy Shapes: ')
shapetest = Cinema_Greedy_Shapes(fname)
start = time.time()
shapetest.seat_greedy()
end = time.time()
shapetime = end - start
shapetest.analyze_results()
shapetest.print_results()
print('Shape time: : ' + str(shapetime))