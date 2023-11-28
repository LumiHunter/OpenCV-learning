import cv2

img = cv2.imread('DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    
    # If we've waited at least 1ms AND we've pressed the ESC
    if cv2.waitKey(1) & 0XFF == 27:
        break
        
cv2.destroyAllWindows()