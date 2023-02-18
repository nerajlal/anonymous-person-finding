import cv2
import mediapipe as mp
import mysql.connector


#Database connection here ..... 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pydb",
  charset="utf8"
)
print(mydb)
mycursor = mydb.cursor()


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize the HandTracking model
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Open the video capture device (webcam)
cap = cv2.VideoCapture(0)

# Initialize the hand detection count and previous hand count
count = 0
prev_hands = 0


while cap.isOpened():
    # Read a frame from the video capture device
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
 
    # Convert the image from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Use the HandTracking model to detect hands in the image
    results = hands.process(image)

    # Draw landmarks on the hands in the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Get the number of hands detected in the current frame
        curr_hands = len(results.multi_hand_landmarks)

        # Increment the count if a new hand is detected
        if curr_hands > prev_hands:
            count += curr_hands - prev_hands

        # Update the previous hand count
        prev_hands = curr_hands

        # Add text to the image
        text = f"Hands Detected: {count}"
        cc = count
        cv2.putText(image, text, (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
       # Show the image with landmarks and text
        cv2.imshow("Hand Tracking", image)
        
# Stop the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #Saving count to database        
            sql = ("INSERT INTO pytb1 (count) VALUES({})".format(count))
            print(sql)
            print(cc)
            mycursor.execute(sql)
            print(mycursor.rowcount, "record inserted.")

            break

# Release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()
