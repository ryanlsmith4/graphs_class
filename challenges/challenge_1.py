
from graph import Graph, Vertex
import sys

def challenge_1():
    vertex_list = []
    edges = []
    counter = 0
    with open(sys.argv[1], 'r') as f:
        #graph_data = f.readlines()
        for line in f:
            x = line.strip('()\n').split(',')
            if counter == 1:
                vertex_list = x
            counter += 1
            if counter > 2:
                edges.append(x)
        # print(vertex_list)
           
    g = Graph()
        # # Add your friends
    for vertex in vertex_list:
        g.add_vertex(vertex)
    # g.add_vertex("Friend 1")
    # g.add_vertex("Friend 2")
    # g.add_vertex("Friend 3")

    # # ...  add all 10 including you ...
    # # Add connections (non weighted edges for now)
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])


    # # Challenge 1: Output the vertices & edges
    # # Print vertices
    # print("# The vertices are: ", g.get_vertices(), "\n")
    print("# Vertices: {}".format(len(edges)))
    print("Edges: {} ".format(len(vertex_list)))
    print("Edge List: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s, %s )" % (v.get_id(), w.get_id(), v.get_edge_weight(w)  ))
    # print(g)

if __name__ == "__main__":


    challenge_1()
