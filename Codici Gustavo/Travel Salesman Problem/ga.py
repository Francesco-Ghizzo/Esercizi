import random

class GA(object):
    def __init__(self, obj, n, crossover_probability, mutation_probability):
        self.obj = obj
        self.n = n
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.chromosomes = None

    def set_chromosomes(self, chromosomes):
        chromosomes = tuple(chromosomes)
        assert len(chromosomes) == 4 * self.n
        self.chromosomes = chromosomes

    def gen_random_chromosomes(self, n):
        return tuple(self.obj.gen_random() for _ in range(n))
        
    def set_random_chromosomes(self):
        self.set_chromosomes(self.gen_random_chromosomes(self.n * 4))

    def evolve(self):
        if self.chromosomes is None:
            self.set_random_chromosomes()
        fit = [self.obj.fitness(i) for i in self.chromosomes]
        res1 = sum(fit) / len(fit)
        res2 = max(fit)
        sel = self.obj.select(self.chromosomes, 2 * self.n)
        random.shuffle(sel)
        offsprings = []
        for c1, c2 in zip(sel[::2], sel[1::2]):
            off1 = self.obj.mutation(self.obj.crossover(c1, c2, self.crossover_probability), self.mutation_probability)
            off2 = self.obj.mutation(self.obj.crossover(c2, c1, self.crossover_probability), self.mutation_probability)
            offsprings.append(off1)
            offsprings.append(off2)
        new_chromosomes = sel + offsprings
        assert len(self.chromosomes) == len(new_chromosomes)
        self.chromosomes = new_chromosomes
        return res1, res2
