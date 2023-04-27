from cinema_greedy import Cinema_Greedy

# A class that represents a greedy search for the best seats in a Cinema
# Inherits from the Cinema class, so it has access to all of the methods in 
#   the Cinema class
# Unlike the Cinema_Greedy class, this class considers different arrangements 
#   than seating an entire group in a row
# For example, a group of 4 could be seated in 2 rows of 2 people next to each 
#   other
class Cinema_Greedy_Shapes(Cinema_Greedy):
    # Create the Cinema
    def __init__(self, fname):
        # Run the Cinema constructor
        super().__init__(fname)

        # Define the shapes that can be used to seat a group
        self.shapes = self.define_shapes()

        # Run the search
        #self.seat_greedy()
        # Analyze the results of the greedy search
        #self.analyze_results()

    # Defines the shapes that can be used to seat a group
    # The shapes are defined as a tuple of tuples that represent the 
    #   coordinates of the seats
    # The coordinates are relative to the back left corner of the shape
    # For example, the shape of a group of 4 could be defined as 
    #   ((0,0), (0,1), (1,0), (1,1))
    # This would represent a 2x2 square of seats
    def define_shapes(self):
        # Create a dictionary to hold the shapes
        shapes = {}

        # Since this project uses a fixed number for the largest group size, 
        #   this will be hard coded
        # This can be changed to be more dynamic if needed
        # No one in the group will be seated alone in their row
        # Shape1 - 1 person, no room for variation
        shapes[1] = [[(0,0)]]

        # Shape2 - 2 people, no room for variation 
        #   (just two people sitting next to each other)
        shapes[2] = [((0,0),(0,1))]

        # Shape3 - 3 people, since no person can be seated alone in their row, 
        #   there is only one shape
        shapes[3] = [((0,0),(0,1),(0,2))]

        # Shape4 - 4 people, there are 2 shapes - all 4 in 1 row, 
        #   or 2 rows of 2
        shapes[4] = [((0,0),(0,1),(0,2),(0,3)),
                     ((0,0),(0,1),(1,0),(1,1))]
        
        # Shape5 - 5 people, 1 row of 5
        # 2 rows - 3 and 2, 2 and 3
        shapes[5] = [((0,0),(0,1),(0,2),(0,3),(0,4)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1)),
                     ((0,0),(0,1),(0,2),(1,1),(1,2)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1))]
        
        # Shape6 - 6 people, 1 row of 6
        # 2 rows - 3 and 3, 4 and 2, 2 and 4
        # 3 rows - 2 and 2 and 2
        shapes[6] = [((0,0),(0,1),(0,2),(0,3),(0,4),(0,5)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(0,2),(0,3),(1,0),(1,1)),
                     ((0,0),(0,1),(0,2),(0,3),(1,1),(1,2)),
                     ((0,0),(0,1),(0,2),(0,3),(1,2),(1,3)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(1,-2),(1,-1),(1,0),(1,1)),
                     ((0,0),(0,1),(1,0),(1,1),(2,0),(2,1)),]
        
        # Shape7 - 7 people, 1 row of 7
        # 2 rows: 5 and 2, 4 and 3, 3 and 4, 2 and 5
        # 3 rows: 3 and 2 and 2, 2 and 3 and 2, 2 and 2 and 3
        shapes[7] = [((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,1),(1,2)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(1,3)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,3),(1,4)),
                     ((0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(1,4)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(1,-2),(1,-1),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(1,-2),(1,-2),(1,-1),(1,0),(1,1)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(2,0),(2,1)),
                     ((0,0),(0,1),(0,2),(1,1),(1,2),(2,0),(2,1)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(2,1),(2,2)),
                     ((0,0),(0,1),(0,2),(1,1),(1,2),(2,1),(2,2)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(2,0),(2,1)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(2,1),(2,2)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(2,-1),(2,0)),
                     ((0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(2,2)),
                     ((0,0),(0,1),(1,1),(1,2),(2,0),(2,1),(2,2)),
                     ((0,0),(0,1),(1,0),(1,1),(2,-1),(2,0),(2,1)),
                     ((0,0),(0,1),(1,-1),(1,0),(2,-1),(2,0),(2,1))]
        
        # Shape8 - 8 people, 1 row of 8
        # 2 rows: 6 and 2, 5 and 3, 4 and 4, 3 and 5, 2 and 6
        # 3 rows: 4 and 2 and 2, 3 and 3 and 2, 3 and 2 and 3, 2 and 3 and 3, 
        #   2 and 4 and 2, 2 and 2 and 4
        # 4 rows: 2 and 2 and 2 and 2
        shapes[8] = [((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,1),(1,2)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,3),(1,4)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,4),(1,5)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)),
                     ((0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3)),             
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(1,3),(1,4)),
                     ((0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(0,2),(1,-2),(1,-1),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(1,2),(1,3),(1,4)),
                     ((0,0),(0,1),(1,-2),(1,-1),(1,0),(1,1),(1,2),(1,3)),
                     ((0,0),(0,1),(1,-3),(1,-2),(1,-1),(1,0),(1,1),(1,2)),
                     ((0,0),(0,1),(1,-4),(1,-3),(1,-2),(1,-1),(1,0),(1,1)),
                     ((0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(2,0),(2,1)),
                     ((0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(2,1),(2,2)),
                     ((0,0),(0,1),(0,2),(0,3),(1,2),(1,3),(2,2),(2,3)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,1),(2,2)),
                     ((0,0),(0,1),(0,2),(1,0),(1,1),(2,0),(2,1),(2,2)),
                     ((0,0),(0,1),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(2,-1),(2,0),(2,1)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(2,1),(2,2)),
                     ((0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(2,2),(2,3)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(1,2),(2,-1),(2,0)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1)),
                     ((0,0),(0,1),(1,-1),(1,0),(1,1),(1,2),(2,1),(2,2)),
                     ((0,0),(0,1),(1,-2),(1,-1),(1,0),(1,1),(2,-2),(2,-1)),
                     ((0,0),(0,1),(1,-2),(1,-1),(1,0),(1,1),(2,-1),(2,0)),
                     ((0,0),(0,1),(1,-2),(1,-1),(1,0),(1,1),(2,0),(2,1)),                   
                     ((0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(2,2),(2,3)),
                     ((0,0),(0,1),(1,0),(1,1),(2,-1),(2,0),(2,1),(2,2)),
                     ((0,0),(0,1),(1,0),(1,1),(2,-2),(2,-1),(2,0),(2,1)),
                     ((0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1))]
        
        # Return the dictionary of shapes
        return shapes

    # Finds valid paths for a group of a given size
    # Returns a list of paths
    # Each path is a list of tuples that represent the coordinates of the seats
    # The coordinates are relative to the back left corner of the shape
    # For example, the path of a group of 4 could be defined as 
    #   ((0,0), (0,1), (1,0), (1,1))
    # This would represent a 2x2 square of seats
    # Uses the shapes dictionary to find possible paths, then checks if they 
    #   are valid
    # Overrides the method in the parent class
    def find_paths(self, group_size):
        # Get the list of shapes for the given group size
        shapes = self.shapes[group_size]

        # Create a list to hold the valid paths
        valid_paths = []

        # Loop through the seats in the Cinema
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                # If the seat is valid, find the rest of the path that starts 
                #   at the seat
                if self.check_valid_seat((i,j)):
                    # Loop through the shapes
                    for shape in shapes:
                        # Create a list to hold the path
                        path = []

                        # Loop through the seats in the shape
                        for seat in shape:
                            # Check if this seat is valid
                            if self.check_valid_seat(\
                                (seat[0] + i, seat[1] + j)):
                                # Add the seat to the path if it is valid
                                path.append((seat[0] + i, seat[1] + j))

                        # If the path is the correct size, add it to the list 
                        #   of paths
                        if len(path) == group_size:
                            # If it is, add it to the list of valid paths
                            valid_paths.append(path)

        # Return the list of valid paths
        return valid_paths