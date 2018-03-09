import numpy as np
import matplotlib.pyplot as pyplot

"""
Model constants
"""
initial_weight = 50
gain           = 1 # per day
gain_noise     = 1
epochs         = 250
actual_val = initial_weight
    
""" g-h filter constants """
g = 2/10 # Qué tanto trackea la señal original 0=nada 1=100%, responde a cambios en la señal
h = 0    # Oscilaciones del filtro resultante, responde a cambios en la tasa de cambio de la señal
weight_estimate = 50
gain_estimate   = 1

error_sensor = 0
error_gh     = 0

mms = []
act = []
ghf = []

for i in range(epochs):
    """ Model measurement generation """
    actual_val += gain + np.random.uniform(-gain_noise, gain_noise)
    measurement = np.random.uniform(actual_val-15, actual_val+15)

    mms.append((i, measurement))
    act.append((i, actual_val))

    prediction = weight_estimate + gain_estimate
    residual = measurement - prediction

    weight_estimate = prediction + g*residual
    gain_estimate   += h*residual

    ghf.append((i, weight_estimate))

    error_sensor += abs(measurement - actual_val)
    error_gh     += abs(weight_estimate - actual_val)

    print(f"Epoch {i}: actual weight: {actual_val}, sensor measurement: {round(measurement, 3)}, g-h estimate: {round(weight_estimate, 3)}")

print(f"Final errors: sensor = {round(error_sensor/epochs, 3)}, gh = {round(error_gh/epochs, 3)}")
pyplot.plot(mms, "r")
pyplot.plot(act)
pyplot.plot(ghf, "b")

pyplot.show()