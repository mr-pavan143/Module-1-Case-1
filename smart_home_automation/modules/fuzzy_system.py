import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

class FuzzySmartHomeSystem:
    def __init__(self):
        self.temperature = ctrl.Antecedent(np.arange(10, 41, 1), 'temperature')
        self.sunlight = ctrl.Antecedent(np.arange(0, 101, 1), 'sunlight')
        self.ac_speed = ctrl.Consequent(np.arange(0, 101, 1), 'ac_speed')
        self.blinds_open = ctrl.Consequent(np.arange(0, 101, 1), 'blinds_open')
        self._setup_membership_functions()
        self._setup_rules()

    def _setup_membership_functions(self):
        self.temperature['cold'] = fuzzy.trapmf(self.temperature.universe, [10, 10, 15, 22])
        self.temperature['comfortable'] = fuzzy.trimf(self.temperature.universe, [18, 23, 27])
        self.temperature['hot'] = fuzzy.trapmf(self.temperature.universe, [25, 30, 40, 40])

        self.sunlight['dim'] = fuzzy.trapmf(self.sunlight.universe, [0, 0, 20, 45])
        self.sunlight['moderate'] = fuzzy.trimf(self.sunlight.universe, [30, 50, 70])
        self.sunlight['bright'] = fuzzy.trapmf(self.sunlight.universe, [60, 80, 100, 100])

        self.ac_speed['off'] = fuzzy.trapmf(self.ac_speed.universe, [0, 0, 10, 25])
        self.ac_speed['low'] = fuzzy.trimf(self.ac_speed.universe, [15, 40, 65])
        self.ac_speed['high'] = fuzzy.trapmf(self.ac_speed.universe, [55, 80, 100, 100])

        self.blinds_open['closed'] = fuzzy.trapmf(self.blinds_open.universe, [0, 0, 15, 35])
        self.blinds_open['partial'] = fuzzy.trimf(self.blinds_open.universe, [25, 50, 75])
        self.blinds_open['open'] = fuzzy.trapmf(self.blinds_open.universe, [65, 85, 100, 100])

    def _setup_rules(self):
        rule1 = ctrl.Rule(self.temperature['hot'] & self.sunlight['bright'], (self.ac_speed['high'], self.blinds_open['closed']))
        rule2 = ctrl.Rule(self.temperature['comfortable'] & self.sunlight['moderate'], (self.ac_speed['low'], self.blinds_open['partial']))
        rule3 = ctrl.Rule(self.temperature['cold'], (self.ac_speed['off'], self.blinds_open['open']))
        rule4 = ctrl.Rule(self.temperature['hot'] & self.sunlight['dim'], (self.ac_speed['high'], self.blinds_open['open']))

        self.home_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
        self.simulator = ctrl.ControlSystemSimulation(self.home_control)

    def compute_actions(self, current_temp, current_sunlight):
        self.simulator.input['temperature'] = current_temp
        self.simulator.input['sunlight'] = current_sunlight
        self.simulator.compute()
        return self.simulator.output['ac_speed'], self.simulator.output['blinds_open']
