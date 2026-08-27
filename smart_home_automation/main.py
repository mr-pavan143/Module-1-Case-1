import time
from modules.fuzzy_system import FuzzySmartHomeSystem
from modules.hardware_mock import SmartHomeHardware

def main():
    print("==========================================================")
    print("Starting Soft Computing Fuzzy Logic Intelligent Controller")
    print("==========================================================")
    
    controller = FuzzySmartHomeSystem()
    appliances = SmartHomeHardware()
    
    scenarios = [
        {"time": "06:30 AM", "temp": 14, "sunlight": 12, "desc": "Cold morning sunrise"},
        {"time": "01:00 PM", "temp": 37, "sunlight": 95, "desc": "Intense hot mid-day solar glare"},
        {"time": "05:00 PM", "temp": 24, "sunlight": 48, "desc": "Comfortable room temp with overcast light"},
        {"time": "09:30 PM", "temp": 28, "sunlight": 0,  "desc": "Warm humid summer evening nightfall"}
    ]
    
    for cycle in scenarios:
        print(f"\n⏰ Time: {cycle['time']} | Context: {cycle['desc']}")
        print(f"   Sensors Input -> Temperature: {cycle['temp']}°C | Sunlight: {cycle['sunlight']}%")
        
        ac_command, blinds_command = controller.compute_actions(cycle['temp'], cycle['sunlight'])
        appliances.adjust_ac_speed(ac_command)
        appliances.adjust_blinds(blinds_command)
        time.sleep(0.2)

if __name__ == "__main__":
    main()
