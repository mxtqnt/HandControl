import cv2
import mediapipe as mp

vid = cv2.VideoCapture(0)
vid.set(3, 1280)
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands= 2, min_detection_confidence= 0.7, min_tracking_confidence= 0.6 )
mpdraw = mp.solutions.drawing_utils
while True :
    _, frame = vid.read()
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = Hands.process(RGBframe)
    if result.multi_hand_landmarks:
        for handLm in result.multi_hand_landmarks :
            mpdraw.draw_landmarks(frame, handLm, mphands.HAND_CONNECTIONS,
                                  mpdraw.DrawingSpec(color=(255, 0, 255), circle_radius=7,
                                                     thickness=cv2.FILLED),
                                  mpdraw.DrawingSpec(color=(255, 255, 255), thickness=2)
                                  )
            for id, lm in enumerate(handLm.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 4 :
                    pass
                if id == 8 :
                    pass
    cv2.imshow("video", frame)
    cv2.waitKey(1)