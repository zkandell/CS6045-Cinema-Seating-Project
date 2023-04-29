# Import os module to be able to look through folders and files
import os
import time

# Import from Cinema.py
from cinema_greedy import Cinema_Greedy
from cinema_greedy_shapes import Cinema_Greedy_Shapes

def TestCinemaFile(cinemafilename, resultfoldername='results'):
    # Greedy algorithm
    basetest = Cinema_Greedy(cinemafilename)

    # Greedy algorithm with shapes
    shapetest = Cinema_Greedy_Shapes(cinemafilename)

    # Run the greedy algorithm
    # Note the start time
    start = time.time()
    basetest.seat_greedy()

    # Note the end time
    end = time.time()
    greedytime = end - start
    basetest.analyze_results()

    # Run the greedy algorithm with shapes
    # Note the start time
    start = time.time()
    shapetest.seat_greedy()

    # Note the end time
    end = time.time()
    shapetime = end - start
    shapetest.analyze_results()

    # Return the results
    return [cinemafilename, basetest.num_occupied, shapetest.num_occupied, 
            greedytime, shapetime, basetest.layout, shapetest.layout]

def TestCinemaFolder(foldername,resultfoldername='results'):
    # Create a list to hold the results
    results = []

    # Go through all files in the folder
    for filename in os.listdir(foldername):
        filepath = os.path.join(foldername, filename)
        # If the file is a text file
        if filename.endswith(".txt"):
            print("Testing: ", filename)
            cinema = TestCinemaFile(filepath, resultfoldername)
            print(cinema)
            results.append(cinema)
            print("\n")
        # If this is a folder
        elif os.path.isdir(filepath):
            print("Testing folder: ", filename)
            TestCinemaFolder(filepath)
            print("\n")
    # Return the results
    return results
    
# Run the test
results = TestCinemaFolder('TestCinemas')
print(results)

# Write the results to a file
with open('results.txt', 'w') as f:
    for item in results:
        try:
            f.write("%s\n" % item)
        except:
            print("Error writing to file")
            print(item)