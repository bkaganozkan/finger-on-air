import cv2
import mediapipe as mp
import serial
import time
ser = serial.Serial('COM3', 9600) 

time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def is_finger_open(finger_points):
    return finger_points[0].y < finger_points[1].y

while True:
    
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    handTimeCount = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_points = [hand_landmarks.landmark[i] for i in [8, 7, 6]]
            middle_finger_points = [hand_landmarks.landmark[i] for i in [12, 11, 10]]
            ring_finger_points = [hand_landmarks.landmark[i] for i in [16, 15, 14]]

            handTimeCount += 1
            
            if is_finger_open(index_finger_points):
                cv2.putText(img, "Index Finger: Open", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)
                ser.write(bytes([11]))
            else:
                cv2.putText(img, "Index Finger: Closed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2)
                ser.write(bytes([10]))

            if is_finger_open(middle_finger_points):
                cv2.putText(img, "Middle Finger: Open", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)
                ser.write(bytes([21]))
            else:
                cv2.putText(img, "Middle Finger: Closed", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2)
                ser.write(bytes([20]))

            if is_finger_open(ring_finger_points):
                cv2.putText(img, "Ring Finger: Open", (50, 150), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)
                ser.write(bytes([31]))

            else:
                cv2.putText(img, "Ring Finger: Closed", (50, 150), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2)
                ser.write(bytes([30]))

            ser.flush()
            time.sleep(.001)
            
            
    if handTimeCount == 0:        
        ser.write(b"q")
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ser.close()
cap.release()
cv2.destroyAllWindows()
