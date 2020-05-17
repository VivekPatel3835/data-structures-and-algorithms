"""
This file holds utility functions that create the base data to be used with algorithms
"""
from random import randint
from typing import List
from io import open


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


def read_union_commands(file_path: str) -> int or [int, int]:
    """
    Reads union commands from a test data file. The first line in the file is the total number of commands. The
    remainder of the file issues commands in the format P Q
    """
    file = open(file=file_path, mode='r', encoding='utf-8')
    for index, line in enumerate(file):
        if index == 0:
            yield int(line.strip('\n'))
        else:
            values = line.strip('\n').split(" ")
            yield [int(values[0]), int(values[1])]
    yield None
