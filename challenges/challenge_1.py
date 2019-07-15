
from graph import Graph , Vertex

# Challenge 1: Create the graph

g = Graph()

# Add your friends
g.add_vertex("Friend 1")
g.add_vertex("Friend 2")
g.add_vertex("Friend 3")
g.add_vertex("Friend 4")
# g.add_vertex("Friend 5")
# g.add_vertex("Friend 6")
# g.add_vertex("Friend 7")
# g.add_vertex("Friend 8")
# g.add_vertex("Friend 9")
# g.add_vertex("Friend 10")
# g.add_vertex("Friend 11")

# Add connections (non weighted edges for now)
g.add_edge("Friend 1", "Friend 2")
g.add_edge("Friend 1", "Friend 3")
g.add_edge("Friend 1", "Friend 4")
g.add_edge("Friend 2", "Friend 1")
g.add_edge("Friend 2", "Friend 3")
g.add_edge("Friend 2", "Friend 4")
g.add_edge("Friend 3", "Friend 1")
g.add_edge("Friend 3", "Friend 2")
g.add_edge("Friend 3", "Friend 4")
g.add_edge("Friend 4", "Friend 1")
g.add_edge("Friend 4", "Friend 2")
g.add_edge("Friend 4", "Friend 3")

# g.add_edge("Friend 4", "Friend 5")
# g.add_edge("Friend 5", "Friend 6")
# g.add_edge("Friend 6", "Friend 7")
# g.add_edge("Friend 7", "Friend 8")
# g.add_edge("Friend 8", "Friend 9")
# g.add_edge("Friend 9", "Friend 10")
# g.add_edge("Friend 10", "Friend 1")
# g.add_edge("Friend 1", "Friend 3")
# g.add_edge("Friend 1", "Friend 4")
# g.add_edge("Friend 1", "Friend 5")
# g.add_edge("Friend 1", "Friend 6")
# g.add_edge("Friend 1", "Friend 7")
# g.add_edge("Friend 1", "Friend 8")
# g.add_edge("Friend 1", "Friend 9")
# g.add_edge("Friend 2", "Friend 1")
# g.add_edge("Friend 2", "Friend 2")
# # g.add_edge("Friend 2", "Friend 3")
# g.add_edge("Friend 2", "Friend 4")
# g.add_edge("Friend 2", "Friend 5")
# g.add_edge("Friend 2", "Friend 6")
# g.add_edge("Friend 2", "Friend 7")
# g.add_edge("Friend 2", "Friend 8")
# g.add_edge("Friend 2", "Friend 9")
# g.add_edge("Friend 2", "Friend 10")







# Challenge 1: Output the vertices & edges
# Print vertices
print("The vertices are: ", g.get_vertices(), "\n")

# print("The edges are: ")
print(g.num_vertices)
for v in g:
    for w in v.get_neighbors():
        
        print("( %s , %s )" % (v.get_id(), w.get_id()))
print(g)
