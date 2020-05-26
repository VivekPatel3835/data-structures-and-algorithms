from datetime import datetime
from typing import List
from src.utils import generate_union_commands, read_union_commands

"""
Our goal is to write a program to filter out extraneous pairs from the sequence: 
When the program reads a pair p q from the input, it should write the pair to the output only 
if the pairs it has seen to that point do not imply that p is connected to q. If the previous 
pairs do imply that p is connected to q, then the program should ignore the pair p q and proceed 
to read in the next pair. 
"""


class QuickUnion:
    """This algorithm answers the question: Is there a path between two objects (FINDING ALGORITHM).
    It does not provide the path."""

    def __init__(self, components: List[int]):
        self.components = components
        self.component_connections = self._initialize_indexed_array()
        self.component_count = len(components)

    # M = number of union operations
    _TIME_COMPLEXITY = "M * N"

    # O(n)
    def _initialize_indexed_array(self) -> List:
        return list(range(0, len(self.components)))

    # O(n)
    def connected(self, p: int, q: int) -> bool:
        return self._get_root(i=p) == self._get_root(i=q)

    # O(n)
    def _get_root(self, i: int) -> int:
        parent = self.component_connections[i]
        current = i
        while current != parent:
            current = self.component_connections[parent]
            parent = self.component_connections[current]
        return parent

    # O(1)
    def union(self, p: int, q: int) -> None:
        if not self.connected(p=p, q=q):
            self.component_count -= 1
            self.component_connections[self._get_root(i=p)] = self.component_connections[self._get_root(i=q)]
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, union({p}, {q}). count => {self.component_count}')
            # print(self.components)
            # print(self.component_connections)
        else:
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, {p} and {q} are connected.')


if __name__ == "__main__":
    commands = read_union_commands(file_path="../../tests/test_data/large_union_find.txt")
    connections = next(commands)
    components = list(range(0, connections))
    print(f'PROGRAM START')
    qf = QuickUnion(components=components)
    start = datetime.now()
    command = next(commands)
    while command:
        qf.union(p=command[0], q=command[1])
        command = next(commands)
    end = datetime.now()
    print(f'PROGRAM END. TIME ELAPSED: {end - start}. Component count: {qf.component_count}')
