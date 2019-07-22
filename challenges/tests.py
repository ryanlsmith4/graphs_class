from graph import Graph, Vertex
import unittest

class GraphTest(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        vertex = Vertex('test') 
        isinstance(vertex, Vertex)
        isinstance(graph, Graph)
  

    def test_add_vertex(self):
        graph = Graph()
        vertex = Vertex('test') 
        graph.add_vertex(vertex)
        assert graph.num_vertices == 1

    def test_add_edge(self):
        graph = Graph()
        a = Vertex('A')
        b = Vertex('B')
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, b)
        a.add_neighbor(b)
        assert b in a.get_neighbors() 