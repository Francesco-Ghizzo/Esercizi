import itertools
import math
import operator
import random

import gaproblem

class TSP(gaproblem.GAProblem):
    def __init__(self, points):
        self.points = points
        self.distance = {}
        for a, b in itertools.combinations(range(len(self.points)), 2):
            d = self.distance_fn(self.points[a], self.points[b])
            self.distance[(a, b)] = self.distance[(b, a)] = d

    def gen_random(self):
        perm = list(range(len(self.points)))
        random.shuffle(perm)
        return tuple(perm)

    square_list = classmethod(lambda cls, l: [i * i for i in l])
    distance2 = classmethod(lambda cls, a, b: sum(cls.square_list(map(operator.sub, a, b))))
    distance_fn = classmethod(lambda cls, a, b: math.sqrt(cls.distance2(a, b)))
    rotate_left = classmethod(lambda cls, l, i=1: l[i:] + l[:i])

    def calc_distance(self, chromosome):
        assert len(chromosome) == len(self.points)
        j1 = chromosome
        j2 = self.rotate_left(j1)
        return sum(map(self.distance.__getitem__, zip(j1, j2)))

    @classmethod
    def recomb1(cls, chromosome1, chromosome2):
        if chromosome1 == chromosome2:
            return chromosome1
        else:
            d = dict((i, c) for c, i in enumerate(chromosome1))
            clen = len(chromosome1)
            res = [None] * clen
            used = set()
            
            c0 = random.choice([c for c, (i1, j1) in enumerate(zip(chromosome1, chromosome2)) if i1 != j1])
            while c0 not in used:
                used.add(c0)
                res[c0] = chromosome1[c0]
                c0 = d[chromosome2[c0]]
            for c, i in enumerate(res):
                if res[c] is None:
                    res[c] = chromosome2[c]
            return res

    @classmethod
    def recomb2(cls, chromosome1, chromosome2):
        l1 = len(chromosome1)
        p1 = random.randint(0, l1)
        p2 = random.randint(p1, l1)
        zz = set(chromosome1[:p1] + chromosome1[p2:])
        xx = tuple(i for i in chromosome2 if i not in zz)
        return chromosome1[:p1] + xx + chromosome1[p2:]

    @classmethod
    def calc_new_pos(cls, pos, clen):
        n = clen >> 1
        tot = (n * (n + 1))
        n2 = 0
        if clen & 1 == 0:
            tot -= 1
            n2 = 1

        r = random.randrange(tot) + 1 + n2
        s = ((r & 1) << 1) - 1
        z = ((r + 1) >> 1)
        np = int(math.ceil((math.sqrt(1 + 8 * z) - 1) / 2))
        return (pos + s * (1 + n - np)) % clen

    @classmethod
    def mutation1(cls, chromosome):
        chromosome = list(chromosome)
        i = random.randrange(len(chromosome))
        chromosome.insert(cls.calc_new_pos(i, len(chromosome)), chromosome.pop(i))
        return tuple(chromosome)

        chromosome = list(chromosome)
        i = random.randrange(len(chromosom))
        rr = random.randrange(2)
        r1 = random.randrange((z * (z + 1)) >> 1) + 1
        
        z = i if rr == 0 else (len(chromosome) - i - 1)
        r2 = int(math.ceil((math.sqrt(1 + 8 * r1) - 1) / 2))
        r3 = z + 1 - r2
        to_p = i + (-r3 if rr == 0 else r3)
        chromosome.insert(to_p, chromosome.pop(i))
        return chromosome

    @classmethod
    def mutation3(cls, chromosome):
        chromosome = list(chromosome)
        i = random.randrange(len(chromosome))
        pos = cls.calc_new_pos(i, len(chromosome))
        i, pos = sorted([i, pos])
        chromosome = chromosome[:i] + chromosome[i:pos][::-1] + chromosome[pos:]
        return tuple(chromosome)

    def fitness(self, chromosome):
        d = self.calc_distance(chromosome)
        return 10000. / (d if d else 1)

    def crossover_func(self, chromosome1, chromosome2):
        return [self.recomb1, self.recomb2][random.randrange(2)](chromosome1, chromosome2)

    def mutation_func(self, chromosome):
        return [self.mutation1, self.mutation3][random.randrange(2)](chromosome)
