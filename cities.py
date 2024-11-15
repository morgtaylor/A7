
#edge class to hold individ city & distance data
class Edge:
    def __init__(self, startCity, endCity, distance):
        self.startCity = startCity
        self.endCity = endCity
        self.distance = distance

    #method to format edge as a string to print in readable format
    def __repr__(self): 
        return f"Edge({self.startCity}, {self.endCity}, {self.distance})"

#graph class to hold all cities data
class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []

    #method to format graph as a string to print in readable format
    def __repr__(self): 
        return f"Graph({self.n} cities, {len(self.edges)} edges)"

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
    #create edge with above values
    edge = Edge(startCity, endCity, distance)
    #add edge to graph
    graph.edges.append(edge)

print(graph)
for edge in graph.edges:
    print(edge)