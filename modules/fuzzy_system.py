import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzySmartHomeSystem:
    def __init__(self):
        # Setup Antecedents and Consequents
        self.temperature = ctrl.Antecedent(np.arange(10, 41, 1), 'temperature')
        self.sunlight = ctrl.Antecedent(np.arange(0, 101, 1), 'sunlight')
        self.ac_speed = ctrl.Consequent(np.arange(0, 101, 1), 'ac_speed')
        self.blinds_open = ctrl.Consequent(np.arange(0, 101, 1), 'blinds_open')

        # Define Membership Functions
        self.temperature['cold'] = fuzz.trimf(self.temperature.universe, [10, 10, 22])
        self.temperature['comfortable'] = fuzz.trimf(self.temperature.universe, [18, 24, 30])
        self.temperature['hot'] = fuzz.trimf(self.temperature.universe, [26, 40, 40])

        self.sunlight['low'] = fuzz.trimf(self.sunlight.universe, [0, 0, 40])
        self.sunlight['medium'] = fuzz.trimf(self.sunlight.universe, [30, 50, 70])
        self.sunlight['high'] = fuzz.trimf(self.sunlight.universe, [60, 100, 100])

        self.ac_speed['low'] = fuzz.trimf(self.ac_speed.universe, [0, 0, 40])
        self.ac_speed['medium'] = fuzz.trimf(self.ac_speed.universe, [30, 50, 70])
        self.ac_speed['high'] = fuzz.trimf(self.ac_speed.universe, [60, 100, 100])

        self.blinds_open['closed'] = fuzz.trimf(self.blinds_open.universe, [0, 0, 40])
        self.blinds_open['partial'] = fuzz.trimf(self.blinds_open.universe, [30, 50, 70])
        self.blinds_open['fully'] = fuzz.trimf(self.blinds_open.universe, [60, 100, 100])

        # Define Control Rules
        rule1 = ctrl.Rule(self.temperature['hot'] & self.sunlight['high'], 
                          (self.ac_speed['high'], self.blinds_open['closed']))
        rule2 = ctrl.Rule(self.temperature['comfortable'], 
                          (self.ac_speed['low'], self.blinds_open['partial']))
        rule3 = ctrl.Rule(self.temperature['cold'], 
                          (self.ac_speed['low'], self.blinds_open['fully']))

        # Control System
        self.system = ctrl.ControlSystem([rule1, rule2, rule3])
        self.simulator = ctrl.ControlSystemSimulation(self.system)

    def evaluate(self, current_temp, current_sunlight):
        self.simulator.input['temperature'] = current_temp
        self.simulator.input['sunlight'] = current_sunlight
        self.simulator.compute()
        return self.simulator.output['ac_speed'], self.simulator.output['blinds_open']
