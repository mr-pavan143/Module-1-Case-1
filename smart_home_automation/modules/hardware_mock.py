class SmartHomeHardware:
    def adjust_ac_speed(self, speed):
        print(f"   [Hardware Action] Setting AC Inverter Compressor to: {speed:.1f}% Power")

    def adjust_blinds(self, position):
        print(f"   [Hardware Action] Motorized Blinds Stepper position set to: {position:.1f}% Open")
