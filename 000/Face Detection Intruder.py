
import cv2
import face_recognition
import requests
from playsound import playsound
import glob
""" 
-------------------------------------------------------------------------------------------------------
url = 'https://notify-api.line.me/api/notify'          
token = 'IUmNdJYFQuetWIZDUlbvOBS5vSjXZvJOAwlT8Zcmd03'  # โทเคน Line Notify

headers = {
            'content-type':
            'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+token
           }

-------------------------------------------------------------------------------------------------------
# """


cap = cv2.VideoCapture(0)
face_locations = []

while True:
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-50] # ปรับค่าเฟรมเรต 
    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1) # ตัวที่ 4 = ความหนาเส้นกรอบ
        #msg = "ผู้บุกรุกห้องเซิร์ฟเวอร์"
        #r = requests.post(url, headers=headers , data = {'message':msg})
        #print(r.text)
    
    def create_playlist(path):
                for song in glob.glob(path):
                    if cv2.rectangle:
                       print("Playing...",song)
                       playsound(song)
                    create_playlist("C:/Users/PC310165/Music/Pan_ka.mp3")


    frame = cv2.resize(frame, (600 , 450))     
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()