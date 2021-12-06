import cv2 as cv
import mediapipe as mp
import os
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
counter = 0
stage = None
create = None
 
def findPosition(image, draw=True):
  lmList = []
  if results.pose_landmarks:
      mp_drawing.draw_landmarks(
         image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
      for id, lm in enumerate(results.pose_landmarks.landmark):
          h, w, c = image.shape
          cx, cy = int(lm.x * w), int(lm.y * h)
          lmList.append([id, cx, cy])
          
  return lmList
cap = cv.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as pose:
  while cap.isOpened():
    success, image = cap.read()
    image = cv.resize(image, (640,480))
     
    
     
    image = cv.cvtColor(cv.flip(image, 1), cv.COLOR_BGR2RGB)
     
     
    results = pose.process(image)
     
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    arr = findPosition(image, draw=True)
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
        counter2 = str(int(counter))
        print(counter)
        os.system("echo '" + counter2 + "' | festival --tts")
    text = "{}:{}".format("Push Ups", counter)
    cv.putText(image, text, (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv.imshow('MediaPipe Pose', image)
     
    key = cv.waitKey(1) & 0xFF
     
    if key == 27:
      break
     
cv.destroyAllWindows()