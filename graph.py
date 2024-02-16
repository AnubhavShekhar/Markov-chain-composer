import random
from typing import Dict, List

class Vertex:
    def __init__(self, value: str) -> None:
        """
        Initialize a vertex with a given value.

        Args:
            value (str): The value of the vertex.
        """
        self.value = value
        self.adjacent: Dict['Vertex', int] = {}  # nodes that have an edge from this vertex
        self.neighbours: List['Vertex'] = []
        self.neighbour_weights: List[int] = []

    def add_edge_to(self, vertex: 'Vertex', weight: int = 0) -> None:
        """
        Add an edge from this vertex to another vertex with an optional weight.

        Args:
            vertex (Vertex): The vertex to connect to.
            weight (int, optional): The weight of the edge. Defaults to 0.
        """
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex: 'Vertex') -> None:
        """
        Increment the weight of the edge from this vertex to another vertex.

        Args:
            vertex (Vertex): The vertex whose edge weight is to be incremented.
        """
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_mapping(self) -> None:
        """Generate probability mapping for neighbouring vertices."""
        for vertex, weight in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbour_weights.append(weight)

    def next_word(self) -> 'Vertex':
        """
        Choose the next word based on probability weights of neighbouring vertices.

        Returns:
            Vertex: The next vertex chosen.
        """
        return random.choices(self.neighbours, weights=self.neighbour_weights)[0]
    

class Graph:
    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.vertices: Dict[str, Vertex] = {}

    def get_vertex_values(self) -> set:
        """
        Get the values of all vertices in the graph.

        Returns:
            set: Set of vertex values.
        """
        return set(self.vertices.keys())

    def add_vertex(self, value: str) -> None:
        """
        Add a vertex to the graph.

        Args:
            value (str): The value of the vertex to be added.
        """
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value: str) -> Vertex:
        """
        Get a vertex by its value. If the vertex does not exist, create it.

        Args:
            value (str): The value of the vertex to get.

        Returns:
            Vertex: The vertex object.
        """
        if value not in self.vertices:
            self.add_vertex(value)

        return self.vertices[value]

    def get_next_word(self, current_vertex: Vertex) -> Vertex:
        """
        Get the next word vertex based on the current vertex.

        Args:
            current_vertex (Vertex): The current vertex.

        Returns:
            Vertex: The next word vertex.
        """
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self) -> None:
        """Generate probability mappings for all vertices in the graph."""
        for vertex in self.vertices.values():
            vertex.get_probability_mapping()
