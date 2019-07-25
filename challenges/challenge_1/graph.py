#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""
from queue import *

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
        # if len(self.neighbors.keys()) != 0:
        #     # print('\n')
        return self.neighbors.keys()
        # else:
        #     # print(self.id)
        #     raise ValueError('No neighbors')
        # return  self.neighbors.keys()

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
        self.vert_dict = {}
        # self.vert_dict = []
        self.num_vertices = 0

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())

    def __str__(self):
        res = ''
        for k in self.vert_dict:
            for d in self.vert_dict[str(k)]:
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
        # self.vert_dict[vertex] = []
        # add the new vertex to the vertex list
        self.vert_dict[key] = vertex
        # return the new vertex
        return vertex

    def get_vertex(self, vertex):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if vertex in self.vert_dict:
            return self.vert_dict[vertex]
        else:
            raise ValueError('Vertex not in graph')

    def add_edge(self, from_vert, to_vert, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if from_vert not in self.vert_dict or to_vert not in self.vert_dict:
            raise ValueError('vertexes not in graph')
        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        else:
           self.vert_dict[from_vert].add_neighbor(self.vert_dict[to_vert], cost)


    def get_vertices(self):
        """return all the vertices in the graph"""
        return str(self.vert_dict.keys())

    def bfs(self, vert, n):
        """Perform breadth first search to get the single shortest path
        Return all nodes found at the `n`th level
        to a node in a graph parts of this code were contributed by Neelam yaday"""
        # Make sure the input node is actually in the graph
        if vert not in self.vert_dict:
            raise ValueError('Vert not in graph')
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.vert_dict))
        # dictionary for keeping track of the distance from the inital vert
        distance_dict = {}
        # create a queue for keeping track of neighbors
        queue = Queue()
        queue.put(vert)
        visited[vert] = True
        # Run breadth_first_search starting from the input node and going `n` levels deep
        while len(queue) <= n:
            s = queue.get()
            if s not in distance_dict:
                distance_dict[s] = 1
            else:
                distance_dict[s] += 1
            print(s, end=" ")
            # get all adjacent vertices of the dequed vertex s. 
            # if a adjacent has not been visited, then mark it visited and enque it
            for i in vert.neighbors:
                if visited[i] == False:
                    queue.put(i)
                    visited[i] = True
        return distance_dict

    def dfs(self, vert):
        pass






        # friend 1, friend 2, friend 3, friend 4, friend 5

