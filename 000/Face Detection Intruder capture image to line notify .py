import cv2
import face_recognition
from line_notify import LineNotify


img_counter = 0

cap = cv2.VideoCapture(0)
face_locations = []

while True:
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-50] # ปรับค่าเฟรมเรต 
    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1) # ตัวที่ 4 = ความหนาเส้นกรอบ
       
        if cv2.rectangle:
           img_name = "image_{}.jpg".format(img_counter) # jpg
           cv2.imwrite(img_name, frame)
           print("{} written!".format(img_name))
           img_counter += 1 
          
           
           notifying = img_name  # format(img_name)
            
           ACCESS_TOKEN = "IUmNdJYFQuetWIZDUlbvOBS5vSjXZvJOAwlT8Zcmd03"
           notify = LineNotify(ACCESS_TOKEN)
           #notify.send("สวัสดี")  
           
           #notify.send("ผู้บุกรุก",notifying) # ส่งข้อความ + ภาพที่อยู่ในโฟลเดอร์เดียวกันนี้  
       
    frame = cv2.resize(frame, (600 , 450))     
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()