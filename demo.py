from Cinema import Cinema_Greedy
from Cinema import Cinema_Greedy_Shapes

def simplebasedemo():
    fname = 'simple_cinema.txt'
    test = Cinema_Greedy(fname)
    test.seat_greedy()
    test.analyze_results()
    test.print_results()

def largebasedemo():
    fname = 'test_cinema.txt'
    test = Cinema_Greedy(fname)
    test.seat_greedy()
    test.analyze_results()
    test.print_results()

def simpleshapedemo():
    fname = 'simple_cinema.txt'
    shapetest = Cinema_Greedy_Shapes(fname)
    shapetest.seat_greedy()
    shapetest.analyze_results()
    shapetest.print_results()

def largeshapedemo():
    fname = 'test_cinema.txt'
    shapetest = Cinema_Greedy_Shapes(fname)
    shapetest.seat_greedy()
    shapetest.analyze_results()
    shapetest.print_results()

def modsimpleshapedemo():
    fname = 'simple_cinema.txt'
    test = Cinema_Greedy(fname)
    test.groups = [5,5]
    shapetest = Cinema_Greedy_Shapes(fname)
    shapetest.groups = [5,5]
    test.seat_greedy()
    test.analyze_results()
    test.print_results()
    shapetest.seat_greedy()
    shapetest.analyze_results()
    shapetest.print_results()

def largeshapecompdemo():
    fname = 'test_cinema.txt'
    test = Cinema_Greedy(fname)
    shapetest = Cinema_Greedy_Shapes(fname)
    test.seat_greedy()
    test.analyze_results()
    test.print_results()
    shapetest.seat_greedy()
    shapetest.analyze_results()
    shapetest.print_results()
    print("People seated by base algorithm: ", test.num_occupied)
    print("People seated by shape algorithm: ", shapetest.num_occupied)

def worseshapedemo():
    fname = 'TestCinemas/Real/Spuimarkt_2/0.9.txt'
    test = Cinema_Greedy(fname)
    shapetest = Cinema_Greedy_Shapes(fname)
    test.seat_greedy()
    test.analyze_results()
    test.print_results()
    shapetest.seat_greedy()
    shapetest.analyze_results()
    shapetest.print_results()
    print("People seated by base algorithm: ", test.num_occupied)
    print("People seated by shape algorithm: ", shapetest.num_occupied)

# Run the demo

# Benchmark algorithm demo
simplebasedemo()
largebasedemo()

# Shape algorithm demo
simpleshapedemo()
largeshapedemo()

# Comparison of algorithms
largeshapecompdemo()
modsimpleshapedemo()
worseshapedemo()