import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables
temperature = ctrl.Antecedent(np.arange(15, 36, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(30, 91, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define fuzzy membership functions
temperature['low'] = fuzz.trimf(temperature.universe, [15, 15, 25])
temperature['medium'] = fuzz.trimf(temperature.universe, [20, 25, 30])
temperature['high'] = fuzz.trimf(temperature.universe, [25, 35, 35])

humidity['low'] = fuzz.trimf(humidity.universe, [30, 30, 60])
humidity['medium'] = fuzz.trimf(humidity.universe, [40, 60, 80])
humidity['high'] = fuzz.trimf(humidity.universe, [60, 90, 90])

fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define the fuzzy rules
rule1 = ctrl.Rule(temperature['high'] & humidity['high'], fan_speed['high'])
rule2 = ctrl.Rule(temperature['low'] & humidity['low'], fan_speed['low'])
rule3 = ctrl.Rule(temperature['medium'] & humidity['medium'], fan_speed['medium'])
rule4 = ctrl.Rule(temperature['low'] & humidity['high'], fan_speed['low'])
rule5 = ctrl.Rule(temperature['high'] & humidity['low'], fan_speed['high'])

# Create the control system and simulation
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# Simulate for a specific input
fan_sim.input['temperature'] = 15  # example temperature in °C
fan_sim.input['humidity'] = 30     # example humidity in %

# Compute the result
fan_sim.compute()
print(f"Fan Speed: {fan_sim.output['fan_speed']:.2f}%")
