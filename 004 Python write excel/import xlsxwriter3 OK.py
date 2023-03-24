import xlsxwriter
import pandas as pd
import datetime

time = datetime.datetime.now()
Name = "ราชัย  รักอก"  # สมพร  ทองทรัพย์
# อ่านข้อมูลที่มีอยู่ในไฟล์เดิม
readDataframe = pd.read_excel (r'fruits.xlsx')
 
# สร้างข้อมูลใหม่เป็นข้อมูลของ orange
#newDataframe = pd.DataFrame({'Name' : ['orange'], 'Price':  [50], 'Amount': [27]})
newDataframe = pd.DataFrame({'Date-Time':  time, 'List Name' : Name, 'Subject': ['เข้าอาคาร ศปก.รร.การบิน']}) 


# นำข้อมูล orange ที่สร้างใหม่รวมเข้ากับข้อมูลเก่าที่อ่านจากไฟล์
frames = [readDataframe, newDataframe]
result = pd.concat(frames)
 
# สร้าง Writer เหมือนกับตอนเขียนไฟล์
writer = pd.ExcelWriter('fruits.xlsx', engine='xlsxwriter')
 
# นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
result.to_excel(writer, index = False)
writer.save()