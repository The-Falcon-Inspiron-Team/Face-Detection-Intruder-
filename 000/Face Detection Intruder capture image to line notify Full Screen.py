import cv2
import face_recognition
from line_notify import LineNotify
import numpy as np
import datetime

img_counter = 0

clock = datetime.datetime.now()

cap = cv2.VideoCapture(1)
face_locations = []
cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)



# ซ้าย บน
angle1 = np.array([
    [(10,10),(50,10)],
    [(10,10),(10,60)]   
                 ])
# ซ้าย ล่าง
angle2 = np.array([
    [(10,425),(50,425)],
    [(10,370),(10,425)]
                  ])
# ขวา ล่าง
angle3 = np.array([
    [(630,425),(630,370)], #   
    [(630,425),(590,425)]  # 
                 ])
# ขวา บน
angle4 = np.array([
    [(590,10),(630,10)], #   
    [(630,10),(630,60)]  # 
                 ])  

while True:
    success, image = cap.read()
    ret, frame = cap.read()
        #อ่านค่าแต่ละเฟรมจากวิดีโอ

    cv2.rectangle(frame, (0, 435), (1500, 730), (96, 96, 96), -1) # 
    #cv2.putText(frame, str(clock.now()), (380, 470), cv2. FONT_HERSHEY_DUPLEX , 0.7,  # ขนาดฟอนต์   (กำลังดี)
    cv2.putText(frame,"The Falcon Inspiron Team.", (453, 452), cv2. FONT_HERSHEY_COMPLEX_SMALL , 0.55,
        (255, 255, 255), 1) 
    cv2.putText(frame, str(clock.now()), (454, 472), cv2. FONT_HERSHEY_COMPLEX_SMALL, 0.75,  # ขนาดฟอน ต์            
        (255, 255, 0), 1)  # สี + ความหนาอักษร
        #แสดงผลลัพท์ Video

    rgb_frame = frame[:, :, ::-50] # ปรับค่าเฟรมเรต 
    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1) # ตัวที่ 4 = ความหนาเส้นกรอบ
       
        if cv2.rectangle:

            cv2.polylines(frame,angle1,1,(0,0,255),3)
            cv2.polylines(frame,angle2,0,(0,0,255),3)
            cv2.polylines(frame,angle3,0,(0,0,255),3)
            cv2.polylines(frame,angle4,0,(0,0,255),3) 

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.circle(frame, (15,460), 10, (0,0,255), -1)
            cv2.putText(frame, " Pass screening.",(28,468), font, 0.8,(0,255,255),2) 

            


            img_name = "image_{}.jpg".format(img_counter) # jpg
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1 
          
           
            notifying = img_name  # format(img_name)
            
            ACCESS_TOKEN = "IUmNdJYFQuetWIZDUlbvOBS5vSjXZvJOAwlT8Zcmd03"
            notify = LineNotify(ACCESS_TOKEN)
            #notify.send("สวัสดี")  
           
            notify.send("ผู้บุกรุก",notifying) # ส่งข้อความ + ภาพที่อยู่ในโฟลเดอร์เดียวกันนี้  
    #cv2.imshow("Image", image)   
    #frame = cv2.resize(frame, (600 , 450))     
    cv2.imshow('Image', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()