# Particle Swarm Optimization (PSO)
Particle Swarm Optimization (PSO) is a heuristic optimization method aimed at finding global minimums or maximums.
Its operation is inspired by the behavior of flocks of birds or schools of fish in which the movement of each individual
(direction, speed, acceleration ...) is the result of combining the individual decisions of each with the behavior of
the rest.

## How can I use this code?
It's really easy you need to find the pso.py file and run it.
You can replace the objective function by your own objective function.

```python
# objective Function
def sphere(x):
    total = 0
    for i in range(len(x)):
        total += x[i] ** 2
    return total
```
If you replace the objective function with your own objective function you will need to change the setting values.
```python
# settings
num_dimensions = 2
bounds = [(-10, 10), (-10, 10)]
minimize(sphere, num_dimensions, bounds, num_particles=15, max_iter=30, verbose=True)
```
And that's it let's minimize functions. Enjoy this repository.

