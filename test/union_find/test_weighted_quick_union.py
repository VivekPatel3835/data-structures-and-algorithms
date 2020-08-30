import unittest
from src.algorithms.dynamic_connectivity.weighted_quick_union import WeightedQuickUnion


class TestWeightedQuickUnion(unittest.TestCase):
    def test_algorithm_returns_expected_result_with_no_path_compression(self):
        connections = 10
        components = list(range(0, connections))
        qf = WeightedQuickUnion(components=components)
        commands = [[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [5, 0], [7, 2], [6, 1], [7, 3]]
        expected_tree = [6, 2, 6, 4, 6, 6, 6, 2, 4, 4]
        for command in commands:
            qf.union(p=command[0], q=command[1])
        self.assertEqual(expected_tree, qf.component_connections)

    def test_algorithm_returns_expected_result_with_path_compression(self):
        connections = 10
        components = list(range(0, connections))
        qf = WeightedQuickUnion(components=components, path_compression=True)
        commands = [[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [5, 0], [7, 2], [6, 1], [7, 3]]
        expected_tree = [6, 2, 6, 4, 6, 6, 6, 6, 4, 4]
        for command in commands:
            qf.union(p=command[0], q=command[1])
        self.assertEqual(expected_tree, qf.component_connections)
