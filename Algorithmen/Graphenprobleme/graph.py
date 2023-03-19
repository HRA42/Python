from typing import TypeVar, Generic, List
from edge import Edge

V = TypeVar('V')  # Typ der Knoten im Graphen


class Graph(Generic[V]):
    def __init__(self, vertices: List[V]) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) # Anzahl der Knoten
    
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) # Anzahl der Kanten
    
    # Einen Knoten zum Graphen hinzufügen und seinen Index zurück geben
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # leere Liste zum Speichern von Kanten hinzufügen
        return self.vertex_count - 1 # Index des hinzugefügten Knotens zurückgeben
    
    # Dies ist ein ungerichteter Graph,
    # also fügen wir stets Kanten in beide Richtungen hinzu
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())
    
    # Eine Kante mithilfe von Knotenindizes hinzufügen (Hilfsmethode)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)
    
    # Eine Kante durch Nachschlagen der Knotenindizes hinzufügen (Hilfsmethode)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Den Knoten an einem bestimmten Index finden
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]
    
    # Den Index eines Knotens im Graphen finden
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)
    
    # Die Knoten finden, mit denen ein Knoten an einem bestimmten Index verbunden ist
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Den Index eines Knotens nachschlagen und seine Nachbarn finden (Hilfsmethode)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))
    
    # Alle Kanten zurückgeben, die mit einem Knoten an einem bestimmten Index verknüpft sind
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]
    
    # Den Index eines Knotens nachschlagen und seine Kanten zurückgeben (Hilfsmethode)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Die wohl formatierte Ausgabe eines Graphen ermöglichen
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc
