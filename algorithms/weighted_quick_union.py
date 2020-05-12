from datetime import datetime
from typing import List, Tuple
from utils import generate_union_commands

"""
Our goal is to write a program to filter out extraneous pairs from the sequence: 
When the program reads a pair p q from the input, it should write the pair to the output only 
if the pairs it has seen to that point do not imply that p is connected to q. If the previous 
pairs do imply that p is connected to q, then the program should ignore the pair p q and proceed 
to read in the next pair. 
"""


class WeightedQuickUnion:
    """This algorithm answers the question: Is there a path between two objects (FINDING ALGORITHM).
    It does not provide the path."""

    _initial_depth = 1

    def __init__(self, components: List[int]):
        self.components = components
        self._initialize_indices_and_depth()

    # M = number of union operations
    _TIME_COMPLEXITY = ""

    # O(n)
    def _initialize_indices_and_depth(self) -> None:
        component_connections = []
        component_depths = []
        for index, c in enumerate(self.components):
            component_connections.append(index)
            component_depths.append(self._initial_depth)
        self.component_connections = component_connections
        self.component_depths = component_depths

    # O(n)
    def connected(self, p: int, q: int) -> bool:
        p_root = self._get_root(i=p)
        q_root = self._get_root(i=q)
        return p_root == q_root

    # O(n)
    def _get_root(self, i: int) -> int:
        parent = self.component_connections[i]
        current = i
        while current != parent:
            current = self.component_connections[parent]
            parent = self.component_connections[current]
        return parent

    # O()
    def union(self, p: int, q: int) -> None:
        if not self.connected(p=p, q=q):
            p_root = self._get_root(i=p)
            q_root = self._get_root(i=q)
            p_depth = self.component_depths[p_root]
            q_depth = self.component_depths[q_root]
            if p_depth < q_depth:
                self.component_connections[p_root] = q_root
                self.component_depths[q_root] += p_depth
                self.component_depths[p_root] = self._initial_depth
            else:
                self.component_connections[q_root] = p_root
                self.component_depths[p_root] += q_depth
                self.component_depths[q_root] = self._initial_depth
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, union({p}, {q})')
            # print(self.components)
            # print(self.component_connections)
        else:
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, {p} and {q} are connected.')


if __name__ == "__main__":
    connections = 100000
    components = list(range(0, connections))
    qf = WeightedQuickUnion(components=components)
    commands = generate_union_commands(connection_count=connections)
    print(f'PROGRAM START')
    start = datetime.now()
    for command in commands:
        qf.union(p=command[0], q=command[1])
    end = datetime.now()
    print(f'PROGRAM END. TIME ELAPSED: {end - start}')
