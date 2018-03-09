import numpy as np
import math

class DogSimulation:
    def __init__(self, velocity=2, process_var=2, measurement_var=2, x0=0):
        self.x = x0
        self.mean_vel = velocity
        self.velocity = velocity
        self.process_var = math.sqrt(process_var)
        self.measurement_var = math.sqrt(measurement_var)
        self.time = 0

    def tick(self):
        self.velocity = np.random.normal(self.mean_vel, self.process_var)

        self.x    += self.velocity
        self.time += 1

        return np.random.normal(self.x, self.measurement_var)

"""
dog = DogSimulation()

for i in range(100):
    print(f"Time = {i}: measurement = {dog.tick()} meters, actual pos = {dog.x},  velocity = {dog.velocity}")
"""