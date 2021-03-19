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
    a = 10/0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_view = cv2.flip(gray, 1)
    cv2.imshow('frame gray',img_view)

    
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
    img_view = cv2.filter2D(img_view, -1, kernel)
    #! mutex
    cv2.imshow('frame kernel', img_view)
    
    
    # gamma correction:
    #! mutex
    g = 0.1
    img_view = np.power(img_view, g)
    cv2.imshow('frame gamma', img_view)
    #! mutex
    
    
    

    # the threshold takes image that its values are normalized betwin [0, 255]
    img_view *= 255
    img_view = img_view.astype(np.float32)
    #TODO find a better way to make the shadow of my self to not appear at the img after thresholding
    #TODO maybe by blending multiple thresholded images
    #! mutex
    _, img_view = cv2.threshold(img_view, 150, 255, cv2.THRESH_BINARY)
    #! mutex

    
    # Display the resulting frame
    cv2.imshow('frame',img_view)
    wk = cv2.waitKey(1)
    if wk & 0xFF == ord('q') or wk & 0xFF == ord('Q') or wk & 0xFF == 27:
        break
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

