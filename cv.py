import cv2,os

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)#horiz flip
    #cv2.imshow('Video',frame) 
    

    #print(frame.shape) op : (480,640,3)
    x1=int(0.5*frame.shape[1]) # mid-pt of horiz axis
    x2=int(frame.shape[1]) # end of horiz axis
    y1=60
    y2=int(0.5*frame.shape[1])

    cv2.rectangle(frame,(x1-1, y1-1), (x2+1, y2+1),(255,255,255),1)
    
    
    ROI = frame[y1:y2, x1:x2]
    cv2.imshow('ROI',ROI)
    #cv2.imshow('Frame',frame)
    grayscale=cv2.cvtColor(ROI,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',frame)
    cv2.imshow('ROI',ROI)
    
    blur=cv2.GaussianBlur(grayscale,(5,5),2)
    #blur=cv2.GaussianBlur(ROI,(5,5),2)
    gaus=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2) #11,2
    
    cv2.imshow('ROI GAUS',gaus)
    
    
#    mode=input('Enter the mode of operation : \nEnter 1 for Training.\nEnter 2 for Testing')
#    if mode==1:
#        mode='train'
#    else:
#        mode='test'
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == 27: # esc key
        break
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite('dataset/test_set'+'A/'+os.listdir('dataset/test_set/A')+'.jpg', roi)

cap.release()
cv2.destroyAllWindows()
