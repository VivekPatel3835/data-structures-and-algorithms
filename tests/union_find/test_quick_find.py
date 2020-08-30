import unittest
from src.algorithms.dynamic_connectivity.union_find.quick_find import QuickFind


class TestQuickFind(unittest.TestCase):
    def test_algorithm_returns_expected_result(self):
        connections = 10
        components = list(range(0, connections))
        qf = QuickFind(components=components)
        commands = [[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [8, 9], [5, 0], [7, 2], [6, 1], [1, 0], [6, 7]]
        expected_tree = [1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
        for command in commands:
            qf.union(p=command[0], q=command[1])
        self.assertEqual(expected_tree, qf.component_connections)
