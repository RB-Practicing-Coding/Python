import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define the membership functions for temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 15])
temperature['warm'] = fuzz.trimf(temperature.universe, [10, 20, 30])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 40, 40])

# Define the membership functions for fan speed
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define the fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['high'])

# Create the control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_speed_sim = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Test the fuzzy expert system with an example temperature
test_temperature = 15
fan_speed_sim.input['temperature'] = test_temperature

# Perform the calculation
fan_speed_sim.compute()

# Print the result
print(f"Temperature: {test_temperature}°C")
print(f"Fan Speed: {fan_speed_sim.output['fan_speed']:.2f}%")

# Visualize the membership functions and output
temperature.view()
fan_speed.view()
fan_speed_sim.output['fan_speed']
fan_speed.view(sim=fan_speed_sim)

plt.show()
