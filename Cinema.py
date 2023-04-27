import numpy as np

# The Cinema class represents the Cinema and all of the information about it
# The class is initialized with the name of the file that contains the Cinema 
#   information
class Cinema:
    def __init__(self, file):
        self.file = self.read_file(file)

        # The layout of the cinema, represented by a numpy array
        self.layout = self.cinema_layout(self.file)

        # The total number of available seats in the cinema 
        #   (represented by 1s in the layout)
        self.num_seats = np.sum(self.layout)
        
        # The size of the largest individual group that the seating algorithm 
        #   will consider
        # For this project, this is a hard-coded value of 8, but it could be 
        #   changed to be a variable
        # The larger this is, however, the more complex the problem becomes, 
        #   and the longer it takes to solve
        self.max_group_size = 8

        # The list of groups, represented by a list of integers
        self.groups = self.get_groups(self.file)

        # The total number of groups
        self.num_groups = len(self.groups)

        # The total number of people that want to attend
        self.num_people = sum(self.groups)

        # The list of all possible edges in the graph
        self.edges = self.generate_edges()

        # The weights of the edges in the graph
        self.weights = self.generate_weights()

        # The adjacency list for the graph (a dictionary where the keys are 
        #   the seats and the values are the seats that are connected to the 
        #   key)
        self.adjacency_list = self.generate_adjacency_list()


    def read_file(self, fname):
        # Read the file and break it into lines
        with open(fname) as f:
            content = f.readlines()

        # Remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        return content

    # Constructs the cinema from the content of the file
    # The first two lines of the file give the height and width of the cinema
    # The rest of the file (minus the last line) gives the layout of the cinema
    # 0s represent non-existent seats (for example, an aisle) and 1s represent 
    #   available seats
    # The layout is stored in a numpy array
    # While not represented here, occupied seats are represented by 2s once 
    #   they are assigned
    def cinema_layout(self, content):
        # Grab the first two lines of the file, the height and width of the 
        # Cinema
        h = int(content[0])
        w = int(content[1])

        # Create a numpy array of zeros with the dimensions of the Cinema
        cinema = np.zeros((h,w), dtype=int)

        # Loop through all but the last line of the file, and fill that matrix 
        #   with the values
        for i in range(2, len(content)-1):
            for j in range(0, len(content[i])):
                cinema[i-2][j] = int(content[i][j])

        return cinema

    # Turns the groups notation into a list of integers that represent the 
    #   groups directly
    # In the file, the last line gives the number of groups of each size 
    #   (for example, 0 2 0 means no groups of size 1 or 3, with 2 groups of 
    #   size 2)
    # This function turns that into a list of integers, where each integer 
    #   represents a group of that size
    def get_groups(self, content):
        # Grab the last line of the file, the number of groups of each size
        groups = content[len(content)-1]

        # Split the string into a list of strings, each string is a number
        groups = groups.split()

        # Convert the list of strings into a list of integers
        groups = [int(i) for i in groups]

        # Create a new list to hold the groups
        groups_list = []

        # Loop through the list of integers, and add the number of groups of 
        #   each size to the groups list
        for i in range(0, len(groups)):
            for j in range(0, groups[i]):
                groups_list.append(i+1)

        # Sort the groups list from largest to smallest (so that the largest 
        #   groups are assigned first later on)
        groups_list.sort(reverse=True)

        # Return the list of groups
        return groups_list

    # Generates the list of all possible edges in the graph
    # An edge is a tuple of two seats, where the seats are represented by a 
    #   tuple of their coordinates
    # A seat can be connected to any other seat that is directly above, below, 
    #   left, right, or diagonal of it
    # A seat can also be connected to any other seat within two seats of it 
    #   horizontally
    def generate_edges(self):
        # Create an array to hold the edges
        edges = []

        # Define the offsets for the seats that can be connected to a seat
        offsets = np.array([[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [-1,1], 
                            [1,-1], [1,1], [0,2], [0,-2]])
        
        # Loop through the seats in the Cinema
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                # Loop through the offsets
                for k in range(0, len(offsets)):
                    # Calculate the coordinates of the seat that the current 
                    #   seat is connected to
                    x = i + offsets[k][0]
                    y = j + offsets[k][1]

                    # If the seat is within the bounds of the Cinema, 
                    #   add the edge to the list
                    if x >= 0 and x < len(self.layout) and y >= 0 \
                        and y < len(self.layout[i]):
                        edges.append(((i,j),(x,y)))

        # Convert the list of edges into a numpy array
        edges = np.array(edges)
        return edges
    
    # Generates the weights of the edges in the graph
    # The weight of an edge is 1 if they have the same y coordinate, and 0 if 
    #   they have different y coordinates
    def generate_weights(self):
        # Create an array to hold the weights
        weights = []

        # Loop through the edges
        for i in range(0, len(self.edges)):
            # If the y coordinates of the two seats are the same, add 1 to the 
            #   weights list
            if self.edges[i][0][0] == self.edges[i][1][0]:
                weights.append(1)
            # If the y coordinates of the two seats are different, add 0 to 
            #   the weights list
            else:
                weights.append(0)

        # Convert the list of weights into a numpy array
        weights = np.array(weights)
        return weights
    
    # Creates an adjacency list for the graph
    def generate_adjacency_list(self):
        # Create a dictionary to hold the adjacency list
        adjacency_list = {}
        
        # Loop through the seats in the Cinema
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                # Create a list to hold the seats that are connected to the 
                #   current seat
                adjacency = []
                
                # Loop through the edges
                for k in range(0, len(self.edges)):
                    # If the current seat is one of the seats in the edge, add 
                    #   the other seat to the adjacency list
                    if (i,j) == tuple(self.edges[k][0]):
                        adjacency.append(tuple(self.edges[k][1]))
                    elif (i,j) == tuple(self.edges[k][1]):
                        adjacency.append(tuple(self.edges[k][0]))

                    # Remove duplicates from the adjacency list
                    adjacency = list(set(adjacency))

                # Add the adjacency list for the current seat to the adjacency 
                #   list
                adjacency_list[(i,j)] = adjacency
        return adjacency_list
    
    # Returns the degree of a seat (number of seats that are connected to it)
    def get_degree(self, seat):
        return len(self.adjacency_list[seat])
    
    # Returns the degree of a path (number of seats that are connected to it)
    def get_path_degree(self, path):
        degrees = 0
        for seat in path:
            degrees += self.get_degree(seat)
        return degrees

    # Prints the layout of the cinema
    def print_cinema(self):
        print(self.layout)

    # Returns the seat with the minimum degree of any seat in the list of 
    #   seats given to it
    def min_seat_degree(self, seats):
        # Return None if the list of seats is empty
        if len(seats) == 0:
            return None
        
        # Set the minimum degree to the degree of the first seat in the list
        min_degree = self.get_degree(seats[0])

        # Loop through the seats in the list
        for i in range(1, len(seats)):
            # If the degree of the current seat is less than the minimum 
            #   degree, set the minimum degree to the degree of the current 
            #   seat
            if self.get_degree(seats[i]) < min_degree:
                min_degree = self.get_degree(seats[i])
                index = i

        # Return the seat with the minimum degree
        return seats[index]

    
    # Returns the path with the minimum degree in the list of paths given to it
    # If there are multiple paths with the same degree, it returns the first 
    #   one in the list
    def min_path_degree(self, paths):
        # Return None if the list of paths is empty
        if len(paths) == 0:
            return None
        
        # Calculate the degree of each path
        path_degrees = []
        for i in range(0, len(paths)):
            path_degrees.append(self.get_path_degree(paths[i]))

        # Set the minimum degree to the degree of the first path in the list
        min_degree = path_degrees[0]
        index = 0

        # Loop through the paths in the list
        for i in range(1, len(paths)):
            # If the degree of the current path is less than the minimum 
            #   degree, set the minimum degree to the degree of the current 
            #   path
            if path_degrees[i] < min_degree:
                min_degree = path_degrees[i]
                index = i
        # Return the path with the minimum degree
        return paths[index]

    # Checks if the given seat is too close to an occupied seat
    # If one of the seats in the adjacency list of the given seat is occupied, 
    #   return true
    def check_close(self, seat):
        # Loop through the adjacency list of the given seat
        for i in range(0, len(self.adjacency_list[seat])):
            # Get the coordinates of the seat in the adjacency list
            x = self.adjacency_list[seat][i][0]
            y = self.adjacency_list[seat][i][1]
            # If the seat is occupied, return true
            if self.layout[x][y] == 2:
                return True
        return False

    # Returns if the given seat is valid or not
    # Invalid seats are seats that are outside the Cinema, not accessible, 
    #   already occupied, or too close to an occupied seat
    def check_valid_seat(self, seat):
        # If the seat is outside the Cinema, return false
        if seat[0] < 0 or seat[0] >= len(self.layout) or seat[1] < 0 \
            or seat[1] >= len(self.layout[0]):
            return False
        
        # If the seat is not accessible, return false
        if self.layout[seat[0]][seat[1]] == 0:
            return False
        
        # If the seat is too close to an occupied seat, return false
        if self.check_close(seat):
            return False
        
        # If the seat is already occupied, return false
        if self.layout[seat[0]][seat[1]] == 2:
            return False
        
        # Otherwise, return true
        return True

    # Finds all valid paths of seats that are connected to each other
    # The paths must be of the given group size, inside the Cinema, and not 
    #   contain any invalid seats (content of the seat is 0)
    # The paths also must not be too close to seats that are already occupied
    # Returns a list of paths, where each path is a list of seats
    # This only considers paths contained within a single row
    def find_paths(self, group_size):
        # Create a list to hold the paths
        paths = []

        # Loop through the seats in the Cinema
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                # If the seat is valid, find the rest of the path that starts 
                #   at the seat
                if self.check_valid_seat((i,j)):
                    # Create a list to hold the seats in the current path
                    path = [(i,j)]
                    # Moving to the right, check that all seats in the path 
                    #   are valid

                    for k in range(1, group_size):
                        if self.check_valid_seat((i,j+k)):
                            path.append((i,j+k))
                        else:
                            break

                    # If the path is the correct size, add it to the list of 
                    #   paths
                    if len(path) == group_size:
                        paths.append(path)

        # Return the list of paths
        return paths

    # Analyzes the results of seating the groups in the Cinema
    # This has to be called after the groups have been seated
    # For that reason, this is only called in the constructor in the child 
    #   classes; this class has no seating algorithm
    def analyze_results(self):
        # Calculate the number of groups that were seated
        self.num_seated_groups = 0

        for i in range(0, len(self.seating)):
            if self.seating[i] != None:
                self.num_seated_groups += 1

        # Calculate the number of seats that were occupied
        self.num_occupied = 0

        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[i])):
                if self.layout[i][j] == 2:
                    self.num_occupied += 1

        # Calculate the percentage of groups that were seated
        self.percent_seated = round(((self.num_seated_groups / len(self.groups)) * 100), 2)

        # Calculate the percentage of seats that were occupied
        self.percent_occupied = round(((self.num_occupied / self.num_seats) * 100), 2)

        # Calculate the percentage of people who wanted to attend that were 
        #   seated
        self.percent_people_seated = round(((self.num_occupied / self.num_people) * 100), 2)
    
    # Prints the results of seating the groups in the Cinema
    # This has to be called after the groups have been seated
    # For that reason, this is only called in the constructor in the child 
    #   classes; this class has no seating algorithm
    def print_results(self):
        # Print the Cinema
        self.print_cinema()

        # Print the groups
        print('Total Groups: ' + str(len(self.groups)))

        # Print the number of groups that were seated
        print('Seated Groups: ' + str(self.num_seated_groups))

        # Print the percentage of groups that were seated
        print('Seated Groups (%): ' + str(self.percent_seated) + '%')

        # Print the number of total possible seats
        print('Total Seats: ' + str(self.num_seats))

        # Print the number of seats that were occupied
        print('Occupied Seats: ' + str(self.num_occupied))

        # Print the number of people who wanted to attend
        print('Tickets Purchased: ' + str(self.num_people))

        # Print the percentage of seats that were occupied
        print('Occupied Seats (%): ' + str(self.percent_occupied) + '%')

        # Print the percentage of people who wanted to attend that were seated
        print('Seated People (%): ' + str(self.percent_people_seated) + '%')