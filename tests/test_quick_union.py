import unittest
from algorithms.quick_union import QuickUnion


class TestQuickUnion(unittest.TestCase):
    def test_algorithm_returns_expected_result(self):
        connections = 10
        components = list(range(0, connections))
        qf = QuickUnion(components=components)
        commands = [[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [5, 0], [7, 2], [6, 1], [7, 3]]
        expected_tree = [1, 8, 1, 8, 3, 0, 5, 1, 8, 8]
        for command in commands:
            qf.union(p=command[0], q=command[1])
        self.assertEqual(expected_tree, qf.component_connections)


if __name__ == "__main__":
    unittest.main()
