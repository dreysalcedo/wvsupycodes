#imports
import cv2
import numpy as np
import time
#initialize
net= cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')#models
classes = []
with open('coco.names', 'r') as f:#dataset
    classes= f.read().splitlines()
#load 
cap = cv2.VideoCapture(0);  
#img = cv2.imread('image.jpg')
#initialize fps  
starting_time = time.time()
frame_id = 0
font = cv2.FONT_HERSHEY_PLAIN

while True:  
    _, frame = cap.read()#for webcam
    frame_id += 1
    height, width, _ = frame.shape
    #extract the data
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)    
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)
    #parameters
    boxes = [] 
    confidences = []
    class_ids = []
    #values
    for output in layerOutputs:
        for detection in output:
            scores= detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                
                boxes.append([x,y,w,h])
                confidences.append(float(confidence)) 
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes,confidences, 0.5, 0.4)        
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    
    #identify each object
    if len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h = boxes[i]#extract data from the boxes from the location and size
            label = str(classes[class_ids[i]]) 
            confidence = str(round(confidences[i],2))      
            color = colors [i]
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
            cv2.putText(frame, label + " " + confidence, (x, y+20), font, 2 , (255,255,255), 2)
            
    elapsed_time = time.time() - starting_time 
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS: " + str(fps), (10, 30), font, 2 , (255,255,255), 2)
    cv2.imshow('Image', frame)  
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows