from datetime import datetime
from typing import List
from utils import generate_union_commands

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

    def __init__(self, components: List[int]):
        self.components = components
        self.component_connections = self._initialize_indexed_array(components=components)

    # O(n)
    @staticmethod
    def _initialize_indexed_array(components: list) -> List:
        return list(range(0, len(components)))

    # O(1)
    def connected(self, p: int, q: int) -> bool:
        return self.component_connections[p] == self.component_connections[q]

    # O(n^2)
    def union(self, p: int, q: int) -> None:
        pid = self.component_connections[p]
        qid = self.component_connections[q]

        if not self.connected(p=p, q=q):
            for component in self.components:
                if self.component_connections[component] == pid:
                    self.component_connections[component] = qid
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, union({p}, {q})')
            # print(self.connections)
        else:
            print(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<, {p} and {q} are connected.')


if __name__ == "__main__":
    connections = 100
    components = list(range(0, connections))
    qf = QuickFind(components=components)
    commands = generate_union_commands(connection_count=connections)
    start = datetime.now()
    for command in commands:
        qf.union(p=command[0], q=command[1])
    end = datetime.now()
    print(f'TIME ELAPSED: {end - start}')
