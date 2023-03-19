from __future__ import annotations
from typing import TypeVar, List, Optional, Tuple, Dict
from dataclasses import dataclass
from mst import WeightedPath, print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from Algorithmen.Suche.generic_search import PriorityQueue

V = TypeVar('V')  # Typ der Knoten im Graphen


@dataclass
class DijkstraNode:
    vertex: int
    distance: float

    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool:
        return self.distance == other.distance


def dijkstra(wg: WeightedGraph[V], root: V) -> Tuple[List[Optional[float]], Dict[int, WeightedEdge]]:
    first: int = wg.index_of(root)  # Den Startindex finden
    # Die Entfernungen sind zunächst unbekannt
    distances: List[Optional[float]] = [None] * wg.vertex_count
    distances[first] = 0  # Die Wurzel ist 0 von der Wurzel entfernt
    path_dict: Dict[int, WeightedEdge] = {}  # Wie wir zu jedem Knoten gelangten
    pq: PriorityQueue[DijkstraNode] = PriorityQueue()
    pq.push(DijkstraNode(first, 0))

    while not pq.empty:
        u: int = pq.pop().vertex  # Den nächstgelegenen Knoten erforschen
        dist_u: float = distances[u]  # Sollten wir bereits gesehen haben
        # Alle Kanten/Knoten vom fraglichen Knoten aus betrachten
        for we in wg.edges_for_index(u):
            # Die alte Entfernung zu diesem Knoten
            dist_v: float = distances[we.v]
            # Keine alte Entfernung oder kürzeren Pfad gefunden
            if dist_v is None or dist_v > we.weight + dist_u:
                # Entfernung zu diesem Knoten aktualisieren
                distances[we.v] = we.weight + dist_u
                # Kante auf dem kürzesten Pfad zu diesem Knoten aktualisieren
                path_dict[we.v] = we
                # Diesen Knoten bald erforschen
                pq.push(DijkstraNode(we.v, we.weight + dist_u))

    return distances, path_dict


# Hilfsfunktion, die den Zugriff auf Dijkstra-Ergebnisse erleichtert
def distance_array_to_vertex_dict(wg: WeightedGraph[V], distances: List[Optional[float]]) -> Dict[V, Optional[float]]:
    distance_dict: Dict[V, Optional[float]] = {}
    for i in range(len(distances)):
        distance_dict[wg.vertex_at(i)] = distances[i]
    return distance_dict


# Nimmt ein Dictionary von Kanten zum Erreichen jedes Knotens entgegen
# und gibt eine Liste von Kanten zurück, die von `start` zu `end` führen
def path_dict_to_path(start: int, end: int, path_dict: Dict[int, WeightedEdge]) -> WeightedPath:
    if len(path_dict) == 0:
        return []
    edge_path: WeightedPath = []
    e: WeightedEdge = path_dict[end]
    edge_path.append(e)
    while e.u != start:
        e = path_dict[e.u]
        edge_path.append(e)
    return list(reversed(edge_path))
