from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # Variablentyp
D = TypeVar('D') # Domänentyp

# Basisklasse für alle Bedingungen
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables
    # muss von Unterklassen überschrieben werden!
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        pass
    
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Jeder Variablen sollte einer Domäne zugewiesen sein.")
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Jeder Variable in Bedingung nicht in CSP.")
            else:
                self.constraints[variable].append(constraint)
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # Zuordnung vollständig, wenn jede Viariable zugeordnet ist (Abbruchbedingung)
        if len(assignment) == len(self.variables):
            return assignment
        # Alle Variablen holen, die im CSP, aber in keiner Zuordnung sind
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        # Jedem möglichen Domänenwert der ersten nicht zugeordneten Variable holen
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # Wenn wir noch konsistent sind, Rekursion (fortfahren)
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # Wenn wir das Ergebnis nicht gefunden haben, backtracking
                if result is not None:
                    return result
        return None