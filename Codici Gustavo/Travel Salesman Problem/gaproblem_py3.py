import abc
import random
import sys

import boundedtree


if sys.version_info.major == 3:
    xrange = range


class GAProblem(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fitness(self, chromosome):
        pass

    @abc.abstractmethod
    def crossover_func(self, chromosome1, chromosome2):
        pass

    @abc.abstractmethod
    def mutation_func(self, chromosome):
        pass

    def crossover(self, chromosome1, chromosome2, probability):
        assert len(chromosome1) == len(chromosome2)
        if random.random() < probability:
            res = self.crossover_func(chromosome1, chromosome2)
        else:
            res = chromosome1
        return tuple(res)

    def mutation(self, chromosome, probability):
        if random.random() < probability:
            return self.mutation_func(chromosome)
        else:
            res = chromosome
        return tuple(res)

    def select2(self, chromosomes, d, n):
        res = []
        count = 0
        bt = boundedtree.BoundedTree()
        soma = 0
        for c, w in d:
            bt.append(c, w)
            soma += w
        for _ in xrange(n):
            c, w = bt.pop(random.uniform(0, soma))
            res.append(c)
            soma -= w
        return res

    def select(self, chromosomes, n):
        chromosomes = list(chromosomes)
        ELITISM = 8
        
        res1 = []
        ind_rm = []
        d = sorted([(self.fitness(c), i) for i, c in enumerate(chromosomes)], reverse=True)
        for i in d:
            if len(res1) >= ELITISM:
                break
            pop1 = chromosomes[i[1]]
            if pop1 not in res1:
                res1.append(pop1)
                ind_rm.append(i[1])
        for i in reversed(sorted(ind_rm)):
            chromosomes.pop(i)
        d = [(c, self.fitness(c)) for c in chromosomes]
        res = self.select2(chromosomes, d, n - len(res1))
        return res1 + res
