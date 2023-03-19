from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean
from chromosome import Chromosome

C = TypeVar('C', bound=Chromosome)  # Typ der Chromosomen


class GeneticAlgorithm(Generic[C]):
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(self, initial_population: List[C], threshold: float, max_generations: int = 100,
                 mutation_chance: float = 0.01, crossover_chance: float = 0.7,
                 selection_type: SelectionType = SelectionType.TOURNAMENT) -> None:
        self._population: List[C] = initial_population
        self._threshold: float = threshold
        self._max_generations: int = max_generations
        self._mutation_chance: float = mutation_chance
        self._crossover_chance: float = crossover_chance
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type
        self._fitness_key: Callable = type(self._population[0]).fitness

    # Das Wahrscheinlichkeitsverteilungsrad verwenden, um 2 Eltern zu wählen
    # Hinweis: funktioniert nicht mit negativen Fitness-Ergebnissen
    def _pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weights=wheel, k=2))

    # num_participants Teilnehmer zufällig wählen und die besten 2 nehmen
    def _pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    # Die Population durch eine neue Generation von Individuen ersetzen
    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        # Weitermachen, bis wir die neue Generation gefüllt haben
        while len(new_population) < len(self._population):
            # Die 2 Eltern wählen
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents: Tuple[C, C] = self._pick_roulette([x.fitness() for x in self._population])
            else:
                parents = self._pick_tournament(len(self._population) // 2)
            # Potenzielles Crossover der 2 Eltern
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        # Wenn wir eine ungerade Zahl haben, ist 1 zu viel und wird entfernt
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population  # Referenz ersetzen

    # Mit der Wahrscheinlichkeit _mutation_chance jedes Individuum mutieren
    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    # Den genetischen Algorithmus max_generations Durchgänge lang
    # ausführen und das beste gefundene Individuum zurückgeben
    def run(self) -> C:
        best: C = max(self._population, key=self._fitness_key)
        for generation in range(self._max_generations):
            # Vorzeitiger Ausstieg, wenn wir threshold erreichen
            if best.fitness() >= self._threshold:
                return best
            print(
                f"Generation {generation} Bester {best.fitness()} Mittelwert {mean(map(self._fitness_key, self._population))}")
            self._reproduce_and_replace()
            self._mutate()
            highest: C = max(self._population, key=self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest  # Neuen Bestwert gefunden
        return best  # In _max_generations gefundener Bestwert
