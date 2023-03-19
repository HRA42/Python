from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from Algorithmen.Suche.generic_search import PriorityQueue

V = TypeVar('V')  # Typ der Knoten im Graphen
WeightedPath = List[WeightedEdge]  # Typ-Alias für Pfade


def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])


def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    if start > (wg.vertex_count - 1) or start < 0:
        return None
    result: WeightedPath = []  # Enthält den finalen minimalen Spannbaum
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: [bool] = [False] * wg.vertex_count  # Wo wir schon waren

    def visit(index: int):
        visited[index] = True  # Als besucht markieren
        for edge in wg.edges_for_index(index):
            # Alle von hier kommenden Kanten zu pq hinzufügen
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)  # Beim ersten Knoten beginnt alles

    while not pq.empty:  # Weitermachen, solange es Kanten zu verarbeiten gibt
        edge = pq.pop()
        if visited[edge.v]:
            continue  # Niemals erneut besuchen
        # Dies ist bisher die kürzeste Kante, also zur Lösung hinzufügen
        result.append(edge)
        visit(edge.v)  # Besuchen, wo diese Verbindung hinführt

    return result


def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
    print(f"Gesamtgewicht: {total_weight(wp)}")
