import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
#TODO make this all page with functions
while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    
    # by default the frame will be encoded in ints
    frame = frame.astype(np.float32) / 255
    
    # Our operations on the frame come herecb
    # take the image and turn it into grayscale,
    # so it will be easier to process
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.flip(gray, 1)
    cv2.imshow('frame gray',img)

    
    #TODO blur the image before thresholding
    # the kernel i apply will sharpen the edges in the frame
    kernel = np.array(
        [
            [0,-1,0],
            [-1,5,-1],
            [0,-1,0]
        ]
    )   
    #! mutex
    
    #img = cv2.filter2D(img, -1, kernel)
    #img = cv2.blur(img,ksize=(20,20))
    #! mutex
    #cv2.imshow('frame kernel', img)
    
    
    # gamma correction:
    #! mutex
    g = 1.1
    img = np.power(img, g)
    cv2.imshow('frame gamma', img)
    #! mutex
    
    
    # erosion:
    #! mutex
    ekernel = np.ones(shape=(5,5), dtype=np.uint8)
    img = cv2.erode(img, ekernel, iterations=2)
    img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,ekernel)
    cv2.imshow('frame erode', img)
    #! mutex

    # the threshold takes image that its values are normalized betwin [0, 255]
    img *= 255
    img = img.astype(np.float32)
    #TODO find a better way to make the shadow of my self to not appear at the img after thresholding
    #TODO maybe by blending multiple thresholded images
    #? maybe i dont need to thresh hold
    #! mutex    
    _, img = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE,ekernel)
    #! mutex

    
    # Display the resulting frame
    cv2.imshow('frame',img)
    wk = cv2.waitKey(1)
    if wk & 0xFF == ord('q') or wk & 0xFF == ord('Q') or wk & 0xFF == 27:
        break
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

