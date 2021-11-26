import cv2 as cv
import mediapipe as mp
import math
mpdraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()
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
        #mpdraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
         
        
        for id, lm in enumerate(results.pose_landmarks.landmark):
            if id==12:
                h, w, c = frame.shape 
                
                print(id, lm)
                cx1, cy1 = int( lm.x * w), int(lm.y * h)
                cv.circle(frame, (cx1,cy1), 5, (0, 255, 0), cv.FILLED)    
                
                
                
            elif id==14:
                    h, w, c = frame.shape 
                
                    print(id, lm)
                    cx2, cy2 = int( lm.x * w), int(lm.y * h)
                    cv.circle(frame, (cx2,cy2), 5, (0, 255, 0), cv.FILLED)
                    
                    
                     
            elif id==16:
                    h, w, c = frame.shape 
                    
                
                     
                    cx3, cy3 = int( lm.x * w), int(lm.y * h)
                    cv.circle(frame, (cx3,cy3), 5, (0, 255, 0), cv.FILLED) 
                    
                    
            angle = math.degrees(math.atan2(cy1 - cy2, cx1 - cx2) -
                             math.atan2(cy3 - cy2, cx3 - cx2))
            print(angle)   
            cv.imshow("img",frame)
            
    
    if cv.waitKey(1)==27: 
        break
cv.destroyAllWindows()
cap.release()