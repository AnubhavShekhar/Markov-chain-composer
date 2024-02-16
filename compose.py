import os
import re
import string
import random
from typing import List
from graph import Graph

def get_words_from_text(text_path: str) -> List[str]:
    """
    Read words from a text file and preprocess them.

    Args:
        text_path (str): The path to the text file.

    Returns:
        List[str]: List of preprocessed words.
    """
    with open(text_path, "rb") as f:
        text = f.read().decode("utf-8")
        text = re.sub(r'\[(.+)\]', " ", text)
        text = " ".join(text.split()).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    words = words[:1000]

    return words

def make_graph(words: List[str]) -> Graph:
    """
    Create a graph representation based on a list of words.

    Args:
        words (List[str]): The list of words.

    Returns:
        Graph: The graph representation.
    """
    g = Graph()
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mappings()

    return g

def compose(g: Graph, words: List[str], length: int = 50) -> List[str]:
    """
    Compose a sequence of words based on a graph representation.

    Args:
        g (Graph): The graph representation.
        words (List[str]): The list of words.
        length (int, optional): The length of the composition. Defaults to 50.

    Returns:
        List[str]: The composed sequence of words.
    """
    composition = []
    word = g.get_vertex(random.choice(words))
    
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main() -> None:
    """Main function to orchestrate the composition process."""
    words = get_words_from_text('Projects/Markov_chain_composer/graph-composer/texts/hp_sorcerer_stone.txt')
    g = make_graph(words)

    # words = []
    # artist = "artist_name"
    # print(os.listdir(file_path))
    # for song in os.listdir(file_path):
    #     if song == '.DS_Store':
    #         continue
    #     print(song)
    #     words.extend(get_words_from_text(file_path))

    composition = compose(g, words, 100)
    print(" ".join(composition))

if __name__ == "__main__":
    main()
