from datetime import datetime
from typing import List
from utils import generate_union_commands, read_union_commands

"""
Our goal is to write a program to filter out extraneous pairs from the sequence: 
When the program reads a pair p q from the input, it should write the pair to the output only 
if the pairs it has seen to that point do not imply that p is connected to q. If the previous 
pairs do imply that p is connected to q, then the program should ignore the pair p q and proceed 
to read in the next pair. 
"""


class QuickFind:
    """This algorithm answers the question: Is there a path between two objects.
    It does not provide the path. QuickFind maintains the invariant that p and q are connected if
    and only if id[p] is equal to id[q]. In other words, all sites in a component must have
    the same value in id[]. """

    # M = number of union operations
    _TIME_COMPLEXITY = "M * N"

    def __init__(self, components: List[int]):
        self.components = components
        self.component_connections = self._initialize_indexed_array()
        self.component_count = len(components)

    # O(n)
    def _initialize_indexed_array(self) -> List:
        return list(range(0, len(self.components)))

    # O(1)
    def connected(self, p: int, q: int) -> bool:
        return self.component_connections[p] == self.component_connections[q]

    # O(n)
    def union(self, p: int, q: int) -> None:
        pid = self.component_connections[p]
        qid = self.component_connections[q]

        if not self.connected(p=p, q=q):
            self.component_count -= 1
            for component in self.components:
                if self.component_connections[component] == pid:
                    self.component_connections[component] = qid
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, union({p}, {q}). count => {self.component_count}')
            # print(self.connections)
        else:
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, {p} and {q} are connected.')


if __name__ == "__main__":
    commands = read_union_commands(file_path="../../tests/test_data/large_union_find.txt")
    connections = next(commands)
    components = list(range(0, connections))
    print(f'PROGRAM START')
    qf = QuickFind(components=components)
    start = datetime.now()
    command = next(commands)
    while command:
        qf.union(p=command[0], q=command[1])
        command = next(commands)
    end = datetime.now()
    print(f'PROGRAM END. TIME ELAPSED: {end - start}. Component count: {qf.component_count}')
