"""
This file holds utility functions that create the base data to be used with algorithms
"""
from random import randint
from typing import List


def generate_union_commands(connection_count: int) -> List[List]:
    """
    Generates a 2d array with where p,q in each inner array are the index
    positions that union should be performed on.
    :param connection_count:
    :return commands:
    """
    commands = []
    for i in range(0, connection_count):
        p = randint(0, connection_count - 1)
        q = randint(0, connection_count - 1)

        # prevents union to itself or union command that has already been issued
        while p == q or [p, q] in commands:
            p = randint(0, connection_count - 1)
        commands.append([p, q])
    return commands
