import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# กำหนดตัวแปร Fuzzy
temperature = ctrl.Antecedent(np.arange(15, 36, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(30, 91, 1), 'humidity')
light = ctrl.Antecedent(np.arange(0, 101, 1), 'light')

fan = ctrl.Consequent(np.arange(0, 101, 1), 'fan')
misting = ctrl.Consequent(np.arange(0, 101, 1), 'misting')
led = ctrl.Consequent(np.arange(0, 101, 1), 'led')

# ฟังก์ชันสมาชิก (Membership Functions)
temperature['low'] = fuzz.trimf(temperature.universe, [15, 15, 25])
temperature['medium'] = fuzz.trimf(temperature.universe, [20, 25, 30])
temperature['high'] = fuzz.trimf(temperature.universe, [25, 35, 35])

humidity['low'] = fuzz.trimf(humidity.universe, [30, 30, 60])
humidity['medium'] = fuzz.trimf(humidity.universe, [40, 60, 80])
humidity['high'] = fuzz.trimf(humidity.universe, [60, 90, 90])

light['low'] = fuzz.trimf(light.universe, [0, 0, 50])
light['medium'] = fuzz.trimf(light.universe, [25, 50, 75])
light['high'] = fuzz.trimf(light.universe, [50, 100, 100])

fan['low'] = fuzz.trimf(fan.universe, [0, 0, 50])
fan['medium'] = fuzz.trimf(fan.universe, [25, 50, 75])
fan['high'] = fuzz.trimf(fan.universe, [50, 100, 100])

misting['low'] = fuzz.trimf(misting.universe, [0, 0, 50])
misting['medium'] = fuzz.trimf(misting.universe, [25, 50, 75])
misting['high'] = fuzz.trimf(misting.universe, [50, 100, 100])

led['low'] = fuzz.trimf(led.universe, [0, 0, 50])
led['medium'] = fuzz.trimf(led.universe, [25, 50, 75])
led['high'] = fuzz.trimf(led.universe, [50, 100, 100])

# กำหนดกฎควบคุม (Rules)
rule1 = ctrl.Rule(temperature['high'] & humidity['high'] & light['high'], (fan['high'], misting['low'], led['low']))
rule2 = ctrl.Rule(temperature['high'] & humidity['high'] & light['low'], (fan['high'], misting['low'], led['high']))
rule3 = ctrl.Rule(temperature['high'] & humidity['low'] & light['high'], (fan['high'], misting['high'], led['low']))
rule4 = ctrl.Rule(temperature['high'] & humidity['low'] & light['low'], (fan['high'], misting['high'], led['high']))
rule5 = ctrl.Rule(temperature['low'] & humidity['high'] & light['high'], (fan['low'], misting['low'], led['low']))
rule6 = ctrl.Rule(temperature['low'] & humidity['high'] & light['low'], (fan['low'], misting['low'], led['high']))
rule7 = ctrl.Rule(temperature['low'] & humidity['low'] & light['high'], (fan['low'], misting['high'], led['low']))
rule8 = ctrl.Rule(temperature['low'] & humidity['low'] & light['low'], (fan['low'], misting['high'], led['high']))

# สร้างระบบควบคุมและการจำลอง
control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
simulation = ctrl.ControlSystemSimulation(control_system)

# ทดสอบระบบควบคุมด้วยค่าอินพุต
simulation.input['temperature'] = 28  # ตัวอย่างอุณหภูมิ (°C)
simulation.input['humidity'] = 20     # ตัวอย่างความชื้น (%)
simulation.input['light'] = 90        # ตัวอย่างแสง (%)

# คำนวณผลลัพธ์
simulation.compute()

# แสดงผลลัพธ์
print(f"Fan Speed: {simulation.output['fan']:.2f}%")
print(f"Misting System: {simulation.output['misting']:.2f}%")
print(f"LED Lights: {simulation.output['led']:.2f}%")

# แสดงกราฟฟังก์ชันสมาชิก
fan.view(sim = simulation)
misting.view(sim = simulation)
led.view(sim = simulation)

plt.show()

