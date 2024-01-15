import cv2       #image processing module
import pickle    #used to save the position of the parking spaces

width,height=107,48

try:
    with open('CarParkPos', 'rb') as f:          #code snippet to keep the previously drawn boxes in poslist
        posList=pickle.load(f)
except:
    posList = []

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:               #used to create boxes on left click of mouse
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:              #used to delete boxes on right click of the mouse
        for i, pos in enumerate(posList):             #enumeratre is used to go through the poslist to delete the boxes
            x1,y1 = pos
            if x1<x1+width and y1<y<y1+height:
                posList.pop(i)

    #with open('CarParkPos', 'wb') as f:
        pickle.dump(posList,f)


while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)


    cv2.imshow("Image",img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)

