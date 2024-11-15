import heapq

# Edge class to hold individ city & distance data
class Edge:
    def __init__(self, startCity, endCity, distance):
        self.startCity = startCity
        self.endCity = endCity
        self.distance = distance

    # Method to format edge as a string to print in readable format
    def __repr__(self): 
        return f"Edge({self.startCity}, {self.endCity}, {self.distance})"

# Graph class to hold all cities data
class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []

    # Method to add an edge to the graph 
    def add_edge(self, startCity, endCity, distance): 
        self.edges.append(Edge(startCity, endCity, distance))
    
    # Implementation of Dijkstra's algorithm
    def dijkstra(self, start):
        # Initialize distances with infinity and set distance to the source to 0
        dist = {i: float('inf') for i in range(self.n)} 
        dist[start] = 0

        # Priority queue to store (distance, vertex) pairs 
        priority_queue = [(0, start)] 
        sptSet = set() # Set to track visited nodes 
        predecessors = {i: None for i in range(self.n)}

        while priority_queue:
            # Get vertex with shortest distance
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node not in sptSet: # If current node has not been visited
                sptSet.add(current_node) # Mark node as visted
                for edge in self.edges: # Update distances of ajdacent nodes
                    if edge.startCity == current_node or edge.endCity == current_node:
                        neighbor = edge.endCity if edge.startCity == current_node else edge.startCity
                        if neighbor not in sptSet: 
                            new_distance = current_distance + edge.distance 
                            if new_distance < dist[neighbor]: 
                                dist[neighbor] = new_distance 
                                predecessors[neighbor] = current_node 
                                heapq.heappush(priority_queue, (new_distance, neighbor)) 

        return dist, predecessors
    
    def print_solution(self, dist):
        for node in range(self.n): 
            print(node, "\t", dist[node])


#open input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

#read first line, convert to integer
n = int(lines[0].strip())

#create graph with n cities
graph = Graph(n)

#read in remaining data and add to edge class
for line in lines[1:]:
    #separate each number in the line
    nums = line.strip().split()
    #assign values to their respective value in edge class
    startCity = int(nums[0])
    endCity = int(nums[1])
    distance = int(nums[2])
    #add edge to graph w/ method in graph class
    graph.add_edge(startCity, endCity, distance)

#Print user prompts
print()
print("Enter a number 0-9, for the following prompts.")
print("Using Dijkstra's we will output the shortest path between the two cities. \n")
start = int(input("Starting City: "))
end = int(input("Destination City: "))

# Find the shortest path using Dijkstra's algorithm 
distances, predecessors = graph.dijkstra(start) 
# Print the shortest distances from the source 
graph.print_solution(distances) 
# Function to get the path from start to end 
def get_path(predecessors, start, end): 
    path = [] 
    current = end 
    while current is not None: 
        path.append(current) 
        current = predecessors[current] 
    path.reverse() 
    return path 
# Retrieve and print the path and total distance 
path = get_path(predecessors, start, end) 
print(f"\nShortest path from city {start} to city {end}: {' -> '.join(map(str, path))}") 
print(f"Total distance: {distances[end]}")