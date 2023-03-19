from __future__ import annotations
from typing import TypeVar, Generic, List, Callable, Set, Deque, Dict, Any, Optional, Protocol
from heapq import heappush, heappop 

T = TypeVar('T')
C = TypeVar('C', bound='Comparable')

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...
    def __lt__(self, other: Any) -> bool:
        ...
    def __gt__(self, other: Any) -> bool:
        return (not self < other) and self != other
    def __le__(self, other: Any) -> bool:
        return self < other or self == other
    def __ge__(self, other: Any) -> bool:
        return not self < other

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    @property
    def empty(self) -> bool:
        return not self._container
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()
    def __repr__(self) -> str:
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()
    @property
    def empty(self) -> bool:
        return not self._container
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.popleft()
    def __repr__(self) -> str:
        return repr(self._container)

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    @property
    def empty(self) -> bool:
        return not self._container
    def push(self, item: T) -> None:
        heappush(self._container, (item))

    def pop(self) -> T:
        return heappop(self._container)
    def __repr__(self) -> str:
        return repr(self._container)

def dfs(inital: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    # frontier bezeichnet, wohin wir noch gehen müssen
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(inital, None))
    # explored bezeichnet, wo wir schon gegangen sind
    explored: Set[T] = {inital}

    # weitersuchen, solange es noch etwas zu endecken gibt
    while not frontier.empty:
        curent_node: Node[T] = frontier.pop()
        current_state: T = curent_node.state
        # prüfen, ob das Ziel erreicht wurde
        if goal_test(current_state):
            return curent_node
        # Prüfen wohin wir gehen können und noch nicht gesucht haben
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, curent_node))
    return None # Alles durchsucht, aber nie das Ziel gefunden

def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

def bfs(iniial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(iniial, None))
    explored: Set[T] = {iniial}

    while not frontier.empty:
        curent_node: Node[T] = frontier.pop()
        current_state: T = curent_node.state
        if goal_test(current_state):
            return curent_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, curent_node))
    return None

def astar(inital: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(inital, None, 0.0, heuristic(inital)))
    explored: Dict[T, float] = {inital: 0.0}

    while not frontier.empty:
        curent_node: Node[T] = frontier.pop()
        current_state: T = curent_node.state
        if goal_test(current_state):
            return curent_node
        for child in successors(current_state):
            new_cost: float = curent_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, curent_node, new_cost, heuristic(child)))
    return None