import random
from collections import Sized

from elem import Elem


class List(Sized):

    def __init__(self, n: int, view: 'View'):
        self.view = view
        sorted_array = []
        for i in range(1, n+1):
            sorted_array.append(i)

        self.array = []

        for i in range(0, n):
            rand_elem = random.choice(sorted_array)
            sorted_array.remove(rand_elem)
            self.array.append(Elem(rand_elem, self))

        self.high_lighted1 = -1
        self.high_lighted2 = -1
        self.comparisons = 0
        self.mutations = 0

    def __getitem__(self, item):
        return self.array[item]

    def __len__(self):
        return len(self.array)

    def swap(self, index1, index2):
        if index1 != index2:
            self.mutations += 1
            self.array[index1], self.array[index2] = self.array[index2], self.array[index1]
            self.view.update(self, False, index1, index2)

    def copy(self):
        copy = List(0, self.view)
        copy.array = self.array.copy()
        copy.high_lighted1 = self.high_lighted1
        copy.high_lighted2 = self.high_lighted2
        copy.comparisons = self.comparisons
        copy.mutations = self.mutations
        return copy

