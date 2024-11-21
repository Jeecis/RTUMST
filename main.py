import random
import heapq

#Sorry guyyys I am sick today :(
#I hope you will like my implementation of Prims algorithm

class Graph:
    def __init__(self):
        self.adjacency_list={}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node]=[]

    def add_edge(self, from_node, to_node, cost):
        self.add_node(from_node)
        self.add_node(to_node)

        #We append nodes and cost to both nodes since this is not a directed graph
        self.adjacency_list[from_node].append((to_node,cost))
        self.adjacency_list[to_node].append((from_node, cost))

    def get_neighbours(self, node):
        return self.adjacency_list.get(node,[])

    def __str__(self):
        return str(self.adjacency_list)

def initialize_graph(filename):
    graph = Graph()
    with (open(filename, 'r') as file):
        for line in file:
            entry = line.split(" ")
            from_building = entry[0]
            to_building = entry[1]
            cost = int(entry[2])

            graph.add_edge(from_building,to_building,cost)
    return graph

def dijkstraMST(currect_graph):
    # Initialize a dictionary to track visited nodes
    visited = set()

    # Create a new Graph instance to hold the MST
    mst_graph = Graph()

    # Start with a random node
    start = random.choice(list(currect_graph.adjacency_list.keys()))
    visited.add(start)
    priority_queue = []

    #Append random nodes neighbours to priority queue
    for neighbor, cost in currect_graph.get_neighbours(start):
        heapq.heappush(priority_queue, (cost, start, neighbor))

    while priority_queue:
        cost, from_node, to_node =heapq.heappop(priority_queue)

        if to_node in visited:
            continue

        mst_graph.add_edge(from_node,to_node,cost)
        visited.add(to_node)

        # Append our latest nodes neighbours to priority queue
        for neighbor, cost in currect_graph.get_neighbours(to_node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost, to_node, neighbor))

    return mst_graph

def main():
    graph =initialize_graph("rtu_network.txt")
    mst_graph =dijkstraMST(graph)

    print(mst_graph)

if __name__ == '__main__':
    main()