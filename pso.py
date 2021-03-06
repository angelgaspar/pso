"""
Angel Gaspar
GitHub: angelgaspar
Last update: December 11th, 2020
Python 3.7

Modifications:
   1.-The initial array written by the user was removed.
   2.-The initial positions are initialized within the search range minimum and maximum randomly.
   3.-The first iteration always was -1.00 the problem was fixed.
   4.-More decimals was added.

Original code without my modifications:
Nathan A. Rooy
Simple Particle Swarm Optimization (PSO) with Python
Last update: 2018-JAN-26
Python 3.6

"""

# --- IMPORT DEPENDENCIES ------------------------------------------------------+
from random import random
from random import uniform


# --- MAIN ---------------------------------------------------------------------+
class Particle:
    def __init__(self, bounds):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual

        for i in range(0, num_dimensions):
            self.velocity_i.append(uniform(-1, 1))
            self.position_i.append(uniform(bounds[i][0], bounds[i][1]))

    # evaluate current fitness
    def evaluate(self, cost_function):
        self.err_i = cost_function(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 0.5  # cognitive constant
        c2 = 0.5  # social constant

        for i in range(0, num_dimensions):
            r1 = random()
            r2 = random()

            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]

            # adjust minimum position if necessary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]


def minimize(cost_function, dimensions, bounds, num_particles, max_iter, verbose=False):
    global num_dimensions

    num_dimensions = dimensions
    err_best_g = -1  # best error for group
    pos_best_g = []  # best position for group

    # establish the swarm
    swarm = []
    for i in range(0, num_particles):
        swarm.append(Particle(bounds))

    # begin optimization loop
    i = 1
    while i <= max_iter:

        # cycle through particles in swarm and evaluate fitness
        for j in range(0, num_particles):
            swarm[j].evaluate(cost_function)

            # determine if current particle is the best (globally)
            if swarm[j].err_i < err_best_g or err_best_g == -1:
                pos_best_g = list(swarm[j].position_i)
                err_best_g = float(swarm[j].err_i)

        # cycle through swarm and update velocities and position
        for j in range(0, num_particles):
            swarm[j].update_velocity(pos_best_g)
            swarm[j].update_position(bounds)

        if verbose: print(f'iter: {i:>4d}, best solution: {err_best_g:10.12f}')

        i += 1

    # print final results
    print('\nFINAL SOLUTION:')
    print("\tPositions: ", pos_best_g)
    print("\tBest Solution: ", err_best_g)

    pass


# objective Function
def sphere(x):
    total = 0
    for i in range(len(x)):
        total += x[i] ** 2
    return total


# settings
num_dimensions = 2  # dimensions
bounds = [(-10, 10), (-10, 10)]  # input bounds [(x1_min, x1_max), (x2_min, x2_max), ...]
minimize(sphere, num_dimensions, bounds, num_particles=15, max_iter=30, verbose=True)
