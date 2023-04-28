from Cinema import Cinema

# A class that represents a greedy search for the best seats in a Cinema
# Inherits from the Cinema class, so it has access to all of the methods in 
#   the Cinema class
# Methods unique to the Greedy search are defined in this class
# The Greedy search finds the best seats for the given group size at the moment
class Cinema_Greedy(Cinema):
    # Create the Cinema
    def __init__(self, fname):
        # Run the Cinema constructor
        super().__init__(fname)
        # Run the greedy search
        #self.seat_greedy()
        # Analyze the results of the greedy search
        #self.analyze_results()

    # Runs a greedy search to find the best seats for the given group size at 
    #   the moment
    # Returns a list of seats to put that group in
    # Also marks the seats as occupied (content of the seat is 2)
    def seat_greedy_single_group(self, group_size):
        # Find all valid paths of seats that are connected to each other
        paths = self.find_paths(group_size)

        # Find the path with the minimum degree
        path = self.min_path_degree(paths)

        # If there are no valid paths, return None
        if path == None:
            return None
        
        # Mark the seats in the path as occupied
        for i in range(0, len(path)):
            self.layout[path[i][0]][path[i][1]] = 2

        # Return the path
        return path
    
    # Runs a greedy search for all groups in the Cinema
    # Returns a list of lists of seats to put each group in
    # Also marks the seats as occupied (content of the seat is 2)
    def seat_greedy(self):
        # Create a list to hold the seats for each group
        self.seating = []

        # Loop through the groups in the Cinema
        for i in range(0, len(self.groups)):
            # Run the greedy search for each group
            self.seating.append(self.seat_greedy_single_group(self.groups[i]))

        # Return the list of seats for each group
        return self.seating