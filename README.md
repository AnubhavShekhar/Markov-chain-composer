# Markov Chain Composer

This project implements a simple Markov chain-based composer using Python. It utilizes a graph data structure to model word sequences and generates compositions based on probability mappings.

## Files

- **graph.py**: Contains classes for implementing the graph data structure used in the composer.
- **compose.py**: Implements the Markov chain composer using the graph structure.

## graph.py

### Classes
- `Vertex`: Represents a vertex in the graph.
- `Graph`: Represents a graph data structure.

### Methods
- `Vertex.add_edge_to(vertex: 'Vertex', weight: int = 0)`: Adds an edge from the current vertex to another vertex with an optional weight.
- `Vertex.increment_edge(vertex: 'Vertex')`: Increments the weight of the edge from the current vertex to another vertex.
- `Vertex.get_probability_mapping()`: Generates probability mapping for neighbouring vertices.
- `Vertex.next_word() -> 'Vertex'`: Chooses the next word based on probability weights of neighbouring vertices.
- `Graph.get_vertex_values() -> set`: Gets the values of all vertices in the graph.
- `Graph.add_vertex(value: str)`: Adds a vertex to the graph.
- `Graph.get_vertex(value: str) -> Vertex`: Gets a vertex by its value. If the vertex does not exist, creates it.
- `Graph.get_next_word(current_vertex: Vertex) -> Vertex`: Gets the next word vertex based on the current vertex.
- `Graph.generate_probability_mappings()`: Generates probability mappings for all vertices in the graph.

## compose.py

### Functions
- `get_words_from_text(text_path: str) -> List[str]`: Reads words from a text file and preprocesses them.
- `make_graph(words: List[str]) -> Graph`: Creates a graph representation based on a list of words.
- `compose(g: Graph, words: List[str], length: int = 50) -> List[str]`: Composes a sequence of words based on a graph representation.
- `main() -> None`: Main function to orchestrate the composition process.

## Usage
1. Ensure Python is installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory.
4. Run `python compose.py` to compose a sequence of words.

## Dependencies
- Python 3.x
