import cv2
import mediapipe as mp
import time
import random
import math
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
list_fingers = []
times = 0
iter = 0
#Random coordinates
def rand_coord():
    return (random.randint(1,400),random.randint(1,400))
obj1_coord = rand_coord()
panel_1_wid1 = (30,50) 
while True:
    
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) #Only for processing because the function was trained on the RGB format

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h) #So you basically get the normalized value of the x coordinate as well as the y coordinate as lm.x and lm.y
                # print(id, cx, cy) #Basically pick coordinates from mediapipe and fill the image with cv2)
                if id ==4 or id == 8:
                    list_fingers.append((id,cx,cy))
                    # print(list_fingers)
                    if abs(cx-obj1_coord[0]) <= 20 and abs(cy-obj1_coord[1]) <= 20:
                        cv2.circle(img, (cx, cy), 5, (128, 0, 128), cv2.FILLED) # Add this if you want continous size decrease for pinching landmark : max(abs(cx-obj1_coord[0]),abs(cy-obj1_coord[1]))
                    else:
                        cv2.circle(img, (cx, cy), 5, (128, 0, 128), cv2.FILLED)
                else:
                    cv2.circle(img, (cx, cy), 5, (58, 100, 18), cv2.FILLED)
                # cv2.line(img, (cx,cy), (0,0), (255,100,100))
                
                cv2.circle(img, obj1_coord, 10, (0, 0, 255), cv2.FILLED)
                
            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            if len(list_fingers) > 1:
                cv2.line(img, (list_fingers[0][1], list_fingers[0][2]), (list_fingers[1][1], list_fingers[1][2]), (100,50,170)) 
                finger_distance_1 = math.sqrt(((list_fingers[0][1]-list_fingers[1][1])**2 + (list_fingers[0][2]-list_fingers[1][2])**2))
                print(finger_distance_1)
                if finger_distance_1 <= 30:
                    if math.sqrt(((list_fingers[0][1]-obj1_coord[0])**2 + (list_fingers[0][2]-obj1_coord[1])**2)) <= 20 or math.sqrt(((list_fingers[1][1]-obj1_coord[0])**2 + (list_fingers[1][2]-obj1_coord[1])**2)) <= 20:
                        obj1_coord = (int((list_fingers[0][1]+list_fingers[1][1])/2),int((list_fingers[0][2]+list_fingers[1][2])/2))
                list_fingers = []
                iter = 0
                
    iter += 1   #To take care of indexing for the line
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    img_new = cv2.flip(img, 1)
    cv2.imshow("Image", img_new)

    cv2.waitKey(1)
