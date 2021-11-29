import cv2 as cv
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
 
top = tk.Tk()
top.geometry("200x100")  
B = tk.Button(top, text ="Right Arm", command = rightarm)

B.pack()
top.mainloop()