from modules.fuzzy_system import FuzzySmartHomeSystem
from modules.hardware_mock import SmartHomeHardware

def main():
    print("Initializing Smart Home System...")
    fuzzy_sys = FuzzySmartHomeSystem()
    hardware = SmartHomeHardware()

    # Simulate sensor data
    temp, light = 32, 85
    print(f"\n[Sensors] Temperature: {temp}°C, Sunlight: {light}%")

    ac_out, blinds_out = fuzzy_sys.evaluate(temp, light)
    
    hardware.adjust_ac_speed(ac_out)
    hardware.adjust_blinds(blinds_out)

if __name__ == "__main__":
    main()
