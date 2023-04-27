# Import os module to be able to look through folders and files
import os
import time

# Import from Cinema.py
from Cinema import Cinema_Greedy
from Cinema import Cinema_Greedy_Shapes

def TestCinemaFile(cinemafilename):
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
    return [cinemafilename, basetest.num_occupied, shapetest.num_occupied, greedytime, shapetime]

def TestCinemaFolder(foldername):
    # Create a list to hold the results
    results = []
    # Go through all files in the folder
    for filename in os.listdir(foldername):
        filepath = os.path.join(foldername, filename)
        # If the file is a text file
        if filename.endswith(".txt"):
            print("Testing: ", filename)
            print(TestCinemaFile(filepath))
            results.append(TestCinemaFile(filepath))
            print("\n")
        # If this is a folder
        elif os.path.isdir(filepath):
            print("Testing folder: ", filename)
            TestCinemaFolder(filepath)
            print("\n")
    
# Run the test
results = TestCinemaFolder('TestCinemas/Real')
print(results)
# Write the results to a file
with open('TestCinemas/Real/results.txt', 'w') as f:
    for item in results:
        try:
            f.write("%s\n" % item)
        except:
            print("Error writing to file")
            print(item)