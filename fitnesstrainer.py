from tkinter.constants import COMMAND
import cv2 as cv
import pywhatkit as kit
import mediapipe as mp
import tkinter as tk
import math
import numpy as np
mpdraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()
def rightarm():
    count=0
    dir=0
    cx3=0
    cy3=0
    cx2=0
    cy2=0
    cx1=0
    cy1=0
    

    cap=cv.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        img_rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results=pose.process(img_rgb)
        if results.pose_landmarks:
            mpdraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
            
            
            for id, lm in enumerate(results.pose_landmarks.landmark):
                if id==12:
                    h, w, c = frame.shape 
                    
                    print(id, lm)
                    cx1, cy1 = int( lm.x * w), int(lm.y * h)
                    cv.circle(frame, (cx1,cy1), 5, (0, 255, 0), cv.FILLED)  
                    cv.circle(frame, (cx1,cy1), 10, (255,0, 0))  
                    
                    
                    
                elif id==14:
                        h, w, c = frame.shape 
                    
                        print(id, lm)
                        cx2, cy2 = int( lm.x * w), int(lm.y * h)
                        cv.circle(frame, (cx2,cy2), 5, (0, 255, 0), cv.FILLED)
                        cv.circle(frame, (cx2,cy2), 10, (255,0, 0)) 
                        
                        
                        
                elif id==16:
                        h, w, c = frame.shape 
                        
                    
                        
                        cx3, cy3 = int( lm.x * w), int(lm.y * h)
                        cv.circle(frame, (cx3,cy3), 5, (0, 255, 0), cv.FILLED) 
                        cv.circle(frame, (cx3,cy3), 10, (255,0, 0)) 
                        
                        
                angle = math.degrees(math.atan2(cy1 - cy2, cx1 - cx2) -
                                math.atan2(cy3 - cy2, cx3 - cx2))
                
                inter=np.interp(angle,(170,40),(0,100)) 
                bar=np.interp(angle,(170,40),(650,100))
                print(count)  
                if inter==100:
                    if dir==0:
                        count=count+0.5
                        dir=1
                if inter==0:
                    if dir==1:
                        count=count+0.5
                        dir=0
                
                cv.rectangle(frame,(500,300),(635,450),(153,102,180),cv.FILLED)      
                cv.putText(frame,str(int(count)),(550,430),cv.FONT_HERSHEY_SIMPLEX,3,(0,255,0),5)
                cv.line(frame,(cx2,cy2),(cx1,cy1),(255,255,255),3)
                cv.line(frame,(cx3,cy3),(cx2,cy2),(255,255,255),3)
                cv.putText(frame, str(int(angle)), ( 50,   50),
                            cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv.rectangle(frame,(110,100),(225,650),(0,255,0) )
                cv.rectangle(frame,(110,int(bar)),(225,650),(255,0,0),cv.FILLED)
                cv.imshow("img",frame)
                
        
        if cv.waitKey(1)==27: 
            break
    cv.destroyAllWindows()
    cap.release()
def leftarm():
    count=0
    dir=0
    cx3=0
    cy3=0
    cx2=0
    cy2=0
    cx1=0
    cy1=0
    

    cap=cv.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        img_rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results=pose.process(img_rgb)
        if results.pose_landmarks:
            mpdraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
            
            
            for id, lm in enumerate(results.pose_landmarks.landmark):
                if id==11:
                    h, w, c = frame.shape 
                    
                    print(id, lm)
                    cx1, cy1 = int( lm.x * w), int(lm.y * h)
                    cv.circle(frame, (cx1,cy1), 5, (0, 255, 0), cv.FILLED)  
                    cv.circle(frame, (cx1,cy1), 10, (255,0, 0))  
                    
                    
                    
                elif id==13:
                        h, w, c = frame.shape 
                    
                        print(id, lm)
                        cx2, cy2 = int( lm.x * w), int(lm.y * h)
                        cv.circle(frame, (cx2,cy2), 5, (0, 255, 0), cv.FILLED)
                        cv.circle(frame, (cx2,cy2), 10, (255,0, 0)) 
                        
                        
                        
                elif id==15:
                        h, w, c = frame.shape 
                        
                    
                        
                        cx3, cy3 = int( lm.x * w), int(lm.y * h)
                        cv.circle(frame, (cx3,cy3), 5, (0, 255, 0), cv.FILLED) 
                        cv.circle(frame, (cx3,cy3), 10, (255,0, 0)) 
                        
                        
                angle = math.degrees(math.atan2(cy3 - cy2, cx3 - cx2) -
                                math.atan2(cy1 - cy2, cx1 - cx2))
                
                inter=np.interp(angle,(170,40),(0,100))  
                bar=np.interp(angle,(170,40),(650,100))
                print(count)  
                if inter==100:
                    if dir==0:
                        count=count+0.5
                        dir=1
                if inter==0:
                    if dir==1:
                        count=count+0.5
                        dir=0
                
                cv.rectangle(frame,(500,300),(635,450),(153,102,180),cv.FILLED)      
                cv.putText(frame,str(int(count)),(550,430),cv.FONT_HERSHEY_SIMPLEX,3,(0,255,0),5)
                cv.line(frame,(cx2,cy2),(cx1,cy1),(255,255,255),3)
                cv.line(frame,(cx3,cy3),(cx2,cy2),(255,255,255),3)
                cv.putText(frame, str(int(angle)), ( 50,   50),
                            cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv.rectangle(frame,(110,100),(225,650),(0,255,0) )
                cv.rectangle(frame,(110,int(bar)),(225,650),(255,0,0),cv.FILLED)
                cv.imshow("img",frame)
                
        
        if cv.waitKey(1)==27: 
            break
    cv.destroyAllWindows()
    cap.release()
def pushup():
    mp_drawing = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    counter = 0
    stage = 0
    create = 0  
     
    def findPosition(image ):
        arr = []
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                arr.append([id, cx, cy])
        return arr
    cap = cv.VideoCapture(0)
    with mpPose.Pose(min_detection_confidence=0.7,min_tracking_confidence=0.7) as pose:
        while cap.isOpened():
            success, image = cap.read()
            image = cv.resize(image, (640,480))
            image = cv.cvtColor(cv.flip(image, 1), cv.COLOR_BGR2RGB)
        
     
            results = pose.process(image)
        
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            arr = findPosition(image )
            if len(arr) != 0:
                cv.circle(image, (arr[12][1], arr[12][2]), 20, (0, 0, 255), cv.FILLED)
                cv.circle(image, (arr[11][1], arr[11][2]), 20, (0, 0, 255), cv.FILLED)
                cv.circle(image, (arr[12][1], arr[12][2]), 20, (0, 0, 255), cv.FILLED)
                cv.circle(image, (arr[11][1], arr[11][2]), 20, (0, 0, 255), cv.FILLED)
                if (arr[12][2] and arr[11][2] >= arr[14][2] and arr[13][2]):
                    cv.circle(image, (arr[12][1], arr[12][2]), 20, (0, 255, 0), cv.FILLED)
                    cv.circle(image, (arr[11][1], arr[11][2]), 20, (0, 255, 0), cv.FILLED)
                    stage = "down"
                if (arr[12][2] and arr[11][2] <= arr[14][2] and arr[13][2]) and stage == "down":
                    stage = "up"
                    counter += 1
                     
                     
                    
            text = "{}:{}".format("Push Ups", counter)
            cv.putText(image, text, (10, 40), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2)
            cv.imshow('MediaPipe Pose', image)
            if cv.waitKey(1)==27: 
                break
            
def playvid():
    def vid( ):
         
        kit.playonyt(str(entry.get()))
        
     
    window=tk.Tk()
    window.geometry("200x100")
    entry= tk.Entry(window, width= 40)
     
    B = tk.Button(window, text ="play video", command=vid)
    
     
    entry.pack()
     
    B.pack()
    
top = tk.Tk()
top.geometry("200x100")  
m=tk.Button(top,text="left Arm",command=leftarm)
B = tk.Button(top, text ="Right Arm", command = rightarm)
n=tk.Button(top,text="pushup",command=pushup)
z=tk.Button(top,text="vid",command=playvid)
m.pack()
n.pack()
z.pack()

B.pack()
top.mainloop()
