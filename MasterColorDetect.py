import cv2
import numpy as np
import threading

def getBlue(kernel,hsv,frame,copy):
    Blues = 0
    #***********Create filter for blue***********
    # Lower boundary values for HSV
    lower_blue = np.array([110, 70, 30]) 
    # Upper boundary values for HSV
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Use morphology open to rid of false pos and false neg (noise)
    opening_b = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel, iterations = 1)
    # Tracking the color yellow
    _, contours, _ = cv2.findContours(opening_b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #bitwise and the Opening filter with the original frame 
    color_b = cv2.bitwise_and(copy, copy, mask = opening_b) 


    for b_pix, contour in enumerate (contours):
            #get the area of the object
            area = cv2.contourArea (contour)
            if (area > 300):
                    Blues = Blues + 1
                    # Get the x, y, w, h in order to create a rectangle around the yellow object
                    x, y, w, h = cv2.boundingRect(contour)
                    # Create a rectangle around the yellow object 
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # Display the name of the color 
                    cv2.putText(frame, "Blue", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (255, 0, 0) )
   
    return Blues, color_b


def getYellow(kernel,hsv,frame,copy):
    Yellows = 0
    #***********Create filter for yellow***********
    # Lower boundary values for HSV
    lower_yellow = np.array([15, 100, 100]) 
    # Upper boundary values for HSV
    upper_yellow = np.array([30, 255, 255]) 
    # Threshold the HSV image to get only yellow colors
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow) 
    # Use morphology open to rid of false pos and false neg (noise)
    opening_y = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel, iterations = 2) 
    # Tracking the color yellow
    _, contours, _ = cv2.findContours(opening_y, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #bitwise and the Opening filter with the original frame 
    color_y = cv2.bitwise_and(copy, copy, mask = opening_y) 
    

    for y_pix, contour in enumerate (contours):
            #get the area of the object
            area = cv2.contourArea (contour)
            if (area > 300):
                    Yellows = Yellows + 1
                    # Get the x, y, w, h in order to create a rectangle around the yellow object
                    x, y, w, h = cv2.boundingRect(contour)
                    # Create a rectangle around the yellow object 
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    # Display the name of the color 
                    cv2.putText(frame, "Yellow", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 255, 255))
    
    return Yellows, color_y

def getGreen(kernel,hsv,frame,copy):
    Greens = 0
    #***********Create filter for green***********
    # Lower boundary values for HSV
    lower_green = np.array([45, 45, 10]) 
    # Upper boundary values for HSV
    upper_green = np.array([100, 255, 255])
    # Threshold the HSV image to get only green colors
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    # Use morphology open to rid of false pos and false neg (noise)
    opening_g = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations = 1)
    #Tracking the color green
    _, contours, _ = cv2.findContours(opening_g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #bitwise and the Opening filter with the original frame 
    color_g = cv2.bitwise_and(copy, copy, mask = opening_g) 

    for g_pix, contour in enumerate (contours):
            #get the area of the object
            area = cv2.contourArea (contour)
            if (area > 300):
                    Greens = Greens + 1
                    # Get the x, y, w, h in order to create a rectangle around the green object
                    x, y, w, h = cv2.boundingRect(contour)
                    # Create a rectangle around the green object 
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (87, 139, 46), 2)
                    # Display the name of the color 
                    cv2.putText(frame, "Green", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (87, 139, 46) )

    return Greens, color_g

def getRed(kernel,hsv,frame,copy):
    Reds = 0
    #***********Create filter for green***********
    #low and high hsv bouindaries for red 
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = mask1 | mask2
    opening_r = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel, iterations = 2)

    #Tracking the color Red
    _, contours, _ = cv2.findContours(opening_r, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #bitwise and the Opening filter with the original frame 
    color_r = cv2.bitwise_and(copy, copy, mask = opening_r) 

    for r_pix, contour in enumerate (contours):
            #get the area of the object
            area = cv2.contourArea (contour)
            if (area > 300):
                    Reds = Reds + 1
                    # Get the x, y, w, h in order to create a rectangle around the red object
                    x, y, w, h = cv2.boundingRect(contour)
                    # Create a rectangle around the yellow object 
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2,lineType=8)
                    # Display the name of the color 
                    cv2.putText(frame, "Red", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 255) )

    return Reds, color_r


def colors():
    #Create locals 
    Greens = 0
    Yellows = 0
    Blues = 0
    Reds = 0

    #Initialize old variables
    old_G = Greens
    old_Y = Yellows
    old_B = Blues
    old_R = Reds 
    
    #capture video
    cap = cv2.VideoCapture(0)

    while True:
        #**********Initiate the camera******************
        #get the frame 
        global _, frame
        _, frame = cap.read()

        #make a copy of the frame
        global copy
        copy = frame.copy()

        #get HSV
        global hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a kernel (structural element) to use in filter
        global kernel 
        kernel = np.ones((5, 5), np.uint8)

        # keep track of the old values 
        old_G = Greens
        old_Y = Yellows
        old_B = Blues
        old_R = Reds 
        zero = 0


        # Call the functions to pass the necessary arguments 
        Greens, color_g = getGreen(kernel,hsv,frame,copy)
        Yellows, color_y = getYellow(kernel,hsv,frame,copy)
        Reds, color_r = getRed(kernel,hsv,frame,copy)
        Blues, color_b = getBlue(kernel,hsv,frame,copy)

        if(old_G != Greens):
                print "Greens", Greens
        
        if(old_Y != Yellows):
                print "Yellows", Yellows

        if(old_B != Blues):
                print "Blues", Blues

        if(old_R != Reds):
                print "Reds", Reds


	#Masks for all the colors 
        all_colors = color_g + color_y + color_r + color_b

        #Display the videos
        cv2.imshow("Final", frame)
        cv2.imshow("Only Colors", all_colors)

        # Introduce a delay of n milliseconds while rendering images to windows
        key = cv2.waitKey(100)

        #press 'esc' to close window 
        if key == 27:
            break
    
    #close the capturing device
    cap.release()
    
    #close all windows that display opencv material 
    cv2.destroyAllWindows()


if __name__ == "__main__":
    t = threading.Thread(target=colors)
    t.start()
