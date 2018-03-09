from gaussian import Gaussian
from dogsim import DogSimulation
from matplotlib import pyplot

x   = Gaussian(0, 20**2) # Initial dog position, is zero but with a high variance

sensor_var = 1
model_var  = 20

process_model = Gaussian(2, model_var)

dog = DogSimulation(velocity=2, process_var=process_model.variance, measurement_var=sensor_var, x0=x.mean)

errors = []

for i in range(100):
    z = dog.tick()
    prior = x + process_model
    likelihood = Gaussian(z, sensor_var)
    x = prior * likelihood
    errors.append((dog.x, z, x.mean))
    print(f"Time = {i}: x = {round(dog.x, 3)}, z = {round(z, 3)}, prediction = prior(mean={round(prior.mean, 3)}, variance={round(prior.variance, 3)}), "
          f"update = posterior(mean={round(x.mean, 3)}, variance={round(x.variance, 3)})")

print(f"Final estimate: {x.mean}, actual pos: {dog.x}")
pyplot.plot(errors)
pyplot.show()