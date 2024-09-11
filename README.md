# 261456_CI_HW2_Y3-1

Computer Assignment 2

Due Date 12 กันยายน 2567 เวลา 23.00 น.

ส่งเป็น pdf file ผ่านระบบที่ exam.cmu.ac.th เท่านั้น ห้ามส่งเป็น e-mail หรือเป็นกระดาษ และแนบ Program มาในภาคผนวก ด้วย ทั้งนี้ ห้าม นศ ทำเรื่องที่ซ้ำกัน

       จงเขียน simulation program สำหรับการทำ fuzzy logic (approximate reasoning) จะใช้ระบบแบบ Mamdani หรือ Takagi & Sugeno แบบใดก็ได้ ให้นักศึกษาแต่ละคนเลือกทำในระบบควบคุมที่ต่างกัน รายงานจะต้องประกอบไปด้วย

       1. ลักษณะการทำงานของระบบ รวมถึง rules ที่ใช้

       2. simulation ของระบบ ผลการทดลอง และวิเคราะห์

       3. โปรแกรม

ตัวอย่างของระบบควบคุมเช่น fuzzy washing machine, fuzzy air conditioner การเดินของหุ่นยนต์ ฯลฯ

หมายเหตุ ควรจะเขียนรายงานให้อยู่ในรูปแบบรายงานที่ดี รวมถึงการวิเคราะห์ที่ดีด้วย

Note: ใช้ library หรือ โปรแกรมสำหรับรูปใดๆ ได้ เฉพาะการบ้านนี้ เท่านั้น และห้ามลอกงานกันมาส่ง มิฉะนั้น จะได้รับ คะแนน 0 ทั้งผู้ให้ลอก และผู้ลอก


เลือกหัวข้อ ระบบควบคุมสภาพอากาศในเรือนกระจก Fuzzy Greenhouse Climate Control

       ลักษณะการทำงาน: ระบบควบคุมสภาพอากาศในเรือนกระจกโดยใช้ Fuzzy Logic เพื่อควบคุมอุณหภูมิ ความชื้น และแสงสว่างให้เหมาะสมกับการเติบโตของพืช
       
       rules ที่ใช้:
       ถ้า อุณหภูมิสูง และ ความชื้นสูง และ แสงมาก → เพิ่ม พัดลม, ลด ระบบพ่นหมอก, ลด ม่านกันแสง
       ถ้า อุณหภูมิสูง และ ความชื้นสูง และ แสงน้อย → เพิ่ม พัดลม, ลด ระบบพ่นหมอก, เพิ่ม ม่านกันแสง
       ถ้า อุณหภูมิสูง และ ความชื้นต่ำ และ แสงมาก → เพิ่ม พัดลม, เพิ่ม ระบบพ่นหมอก, ลด ม่านกันแสง
       ถ้า อุณหภูมิสูง และ ความชื้นต่ำ และ แสงน้อย → เพิ่ม พัดลม, เพิ่ม ระบบพ่นหมอก, เพิ่ม ม่านกันแสง
       ถ้า อุณหภูมิต่ำ และ ความชื้นสูง และ แสงมาก → ลด พัดลม, ลด ระบบพ่นหมอก, ลด ม่านกันแสง
       ถ้า อุณหภูมิต่ำ และ ความชื้นสูง และ แสงน้อย → ลด พัดลม, ลด ระบบพ่นหมอก, เพิ่ม ม่านกันแสง
       ถ้า อุณหภูมิต่ำ และ ความชื้นต่ำ และ แสงมาก → ลด พัดลม, เพิ่ม ระบบพ่นหมอก, ลด ม่านกันแสง
       ถ้า อุณหภูมิต่ำ และ ความชื้นต่ำ และ แสงน้อย → ลด พัดลม, เพิ่ม ระบบพ่นหมอก, เพิ่ม ม่านกันแสง
       
       ระบบควบคุมแบบ: Mamdani
