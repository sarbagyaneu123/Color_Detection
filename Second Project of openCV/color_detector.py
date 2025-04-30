import cv2
import numpy as np

# Optional: a simple color name matcher
def get_color_name(B, G, R):
    colors = {
        'Red': (255, 0, 0),
        'Green': (0, 255, 0),
        'Blue': (0, 0, 255),
        'White': (255, 255, 255),
        'Black': (0, 0, 0),
        'Yellow': (255, 255, 0),
        'Cyan': (0, 255, 255),
        'Magenta': (255, 0, 255),
        'Gray': (128, 128, 128)
    }
    min_dist = float('inf')
    closest_name = "Undefined"
    for name, value in colors.items():
        dist = np.sqrt((value[0] - B) * 2 + (value[1] - G) * 2 + (value[2] - R) ** 2)
        if dist < min_dist:
            min_dist = dist
            closest_name = name
    return closest_name

# Callback function to handle mouse events
def show_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = frame[y, x]
        color_name = get_color_name(b, g, r)
        text = f'BGR: ({b}, {g}, {r}) {color_name}'
        print(text)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (int(b), int(g), int(r)), 2)

# Initialize webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Detector")
cv2.setMouseCallback("Color Detector", show_color)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Color Detector", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()