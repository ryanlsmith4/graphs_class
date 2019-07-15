#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    # def __str__(self):
    #     return self.id

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.neighbors.keys())

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # TODO check if vertex is already a neighbor
        if vertex in self.neighbors:
            raise ValueError('Vertex already a neighbor')
        # TODO if not, add vertex to neighbors and assign weight.
        else:
            # print('Here {}'.format(vertex))
            self.neighbors[vertex] = weight
            # return self

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        # return the neighbors
        if len(self.neighbors) != 0:
            print(len(self.neighbors))
            return self.neighbors.keys()
        else:
            print(self.id)
            raise ValueError('No neighbors')

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this
        # vertext to the given vertex.
        if vertex in self.neighbors:
            return self.neighbors[vertex]
        else:
            raise ValueError('Vertex not in Graph')


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_list = {}
        # self.vert_list = []
        self.num_vertices = 0

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_list.values())

    def __str__(self):
        res = ''
        for k in self.vert_list:
            for d in self.vert_list[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # TODO increment the number of vertices
        self.num_vertices += 1
        # TODO create a new vertex
        vertex = Vertex(key)
        # TODO add the new vertex to the vertex dictionary with a list as the value
        # self.vert_list[vertex] = []
        # TODO add the new vertex to the vertex list
        self.vert_list[key] = vertex
        # TODO return the new vertex
        return vertex

    def get_vertex(self, n):
        """return the vertex if it exists"""
        # TODO return the vertex if it is in the graph
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            raise ValueError('Vertex not in graph')

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f not in self.vert_list or t not in self.vert_list:
            raise ValueError('vertexes not in graph')

        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the add_neighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        else:
           self.vert_list[f].add_neighbor(self.vert_list[t])


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()


# Driver code


if __name__ == "__main__":

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

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            
            print("( %s , %s )" % (v.get_id(), w.get_id()))
    print(g)
