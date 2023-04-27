from cinema_greedy_shapes import Cinema_Greedy_Shapes

if __name__ == '__main__':
    # Cinema being tested is Tillburg_4 0.7
    #fname = 'test_cinema.txt'

    # Simple example Cinema from the paper
    fname = 'simple_cinema.txt'

    # Run the Greedy Search
    test = Cinema_Greedy_Shapes(fname)
    print(test.layout)
    test.seat_greedy()
    test.analyze_results()
    test.print_results()