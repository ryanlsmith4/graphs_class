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


    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.neighbors.keys())

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # check if vertex is already a neighbor
        if vertex in self.neighbors:
            raise ValueError('Vertex already a neighbor')
        # if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight

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
        # return the weight of the edge from this
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
        # increment the number of vertices
        self.num_vertices += 1
        # create a new vertex
        vertex = Vertex(key)
        # add the new vertex to the vertex dictionary with a list as the value
        # self.vert_list[vertex] = []
        # add the new vertex to the vertex list
        self.vert_list[key] = vertex
        # return the new vertex
        return vertex

    def get_vertex(self, n):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            raise ValueError('Vertex not in graph')

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if f not in self.vert_list or t not in self.vert_list:
            raise ValueError('vertexes not in graph')
        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        else:
           self.vert_list[f].add_neighbor(self.vert_list[t])


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

