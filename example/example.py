import cv2
from sfps import SFPS


sfps = SFPS(nframes=7, interval=1)

cap = cv2.VideoCapture("gta.mp4")
while cap.isOpened():
    hasFrame, frame = cap.read()
    if hasFrame:

        # Do your things
        #  - Detect
        #  - Track
        #  - ...

        # Calculate and add frame rate
        fps_str = sfps.fps(format_spec='.2f')
        cv2.putText(frame, fps_str, (15, 30), 
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        # Diplay
        cv2.imshow("SFPS - Smooth FPS", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
