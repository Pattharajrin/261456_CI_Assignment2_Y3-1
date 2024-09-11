import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# กำหนดตัวแปร Fuzzy
temperature = ctrl.Antecedent(np.arange(15, 41, 1), 'temperature')  # ตัวแปร fuzzy สำหรับอุณหภูมิ (°C)
humidity = ctrl.Antecedent(np.arange(30, 91, 1), 'humidity')    # ตัวแปร fuzzy สำหรับความชื้น (%)
light = ctrl.Antecedent(np.arange(0, 101, 1), 'light')  # ตัวแปร fuzzy สำหรับแสง (%)

# ตัวแปรผลลัพธ์ fuzzy
fan = ctrl.Consequent(np.arange(0, 101, 1), 'fan')      # ตัวแปร fuzzy สำหรับความเร็วพัดลม (%)
misting = ctrl.Consequent(np.arange(0, 101, 1), 'misting')  # ตัวแปร fuzzy สำหรับระบบพ่นหมอก (%)
led = ctrl.Consequent(np.arange(0, 101, 1), 'led')      # ตัวแปร fuzzy สำหรับไฟ LED (%)

# ฟังก์ชันสมาชิก (Membership Functions) สำหรับแต่ละตัวแปร
temperature['low'] = fuzz.trimf(temperature.universe, [15, 15, 28])    # ฟังก์ชันสมาชิก "low" ของอุณหภูมิ
temperature['high'] = fuzz.trimf(temperature.universe, [26, 40, 40])   # ฟังก์ชันสมาชิก "high" ของอุณหภูมิ

humidity['low'] = fuzz.trimf(humidity.universe, [30, 30, 61])      # ฟังก์ชันสมาชิก "low" ของความชื้น
humidity['high'] = fuzz.trimf(humidity.universe, [59, 90, 90])      # ฟังก์ชันสมาชิก "high" ของความชื้น

light['low'] = fuzz.trimf(light.universe, [0, 0, 51])            # ฟังก์ชันสมาชิก "low" ของแสง
light['high'] = fuzz.trimf(light.universe, [49, 100, 100])        # ฟังก์ชันสมาชิก "high" ของแสง

fan['low'] = fuzz.trimf(fan.universe, [0, 0, 50])                # ฟังก์ชันสมาชิก "low" ของความเร็วพัดลม
fan['high'] = fuzz.trimf(fan.universe, [50, 100, 100])            # ฟังก์ชันสมาชิก "high" ของความเร็วพัดลม

misting['low'] = fuzz.trimf(misting.universe, [0, 0, 50])        # ฟังก์ชันสมาชิก "low" ของระบบพ่นหมอก
misting['high'] = fuzz.trimf(misting.universe, [50, 100, 100])    # ฟังก์ชันสมาชิก "high" ของระบบพ่นหมอก

led['low'] = fuzz.trimf(led.universe, [0, 0, 50])                # ฟังก์ชันสมาชิก "low" ของไฟ LED
led['high'] = fuzz.trimf(led.universe, [50, 100, 100])            # ฟังก์ชันสมาชิก "high" ของไฟ LED

# กำหนดกฎควบคุม (Rules)
# ตัวอย่างกฎการควบคุมระบบ Fuzzy สำหรับสภาพอากาศในเรือนกระจก
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
simulation.input['temperature'] = 30  # ตั้งค่าอุณหภูมิ (°C) เพื่อทดสอบ (15-40 °C)
simulation.input['humidity'] = 70     # ตั้งค่าความชื้น (%) เพื่อทดสอบ (30-90 %)
simulation.input['light'] = 90        # ตั้งค่าแสง (%) เพื่อทดสอบ (0-100 %)

# คำนวณผลลัพธ์จากการทดสอบ
simulation.compute()

# แสดงผลลัพธ์
print(f"Fan Speed: {simulation.output['fan']:.2f}%")      # แสดงผลความเร็วพัดลม
print(f"Misting System: {simulation.output['misting']:.2f}%")  # แสดงผลระบบพ่นหมอก
print(f"LED Lights: {simulation.output['led']:.2f}%")      # แสดงผลไฟ LED

# แสดงกราฟฟังก์ชันสมาชิก
fan.view(simulation)         # แสดงกราฟฟังก์ชันสมาชิกของพัดลม
misting.view(simulation)     # แสดงกราฟฟังก์ชันสมาชิกของระบบพ่นหมอก
led.view(simulation)         # แสดงกราฟฟังก์ชันสมาชิกของไฟ LED

# แสดงผลลัพธ์กราฟฟังก์ชันสมาชิก
plt.show()
