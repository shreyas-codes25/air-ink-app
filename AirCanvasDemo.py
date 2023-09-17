import numpy as np
import cv2
import hand_tracking_module as hand_tracking
import time


def process_image(img, shape):
    img = cv2.resize(img, shape)
    img = img / 255.
    return img


def airCanvas():    
    labels = [' ', ' ', ' ', ' ', '', ' ', ' ', ' ']
    labels_copy = labels.copy()
    actual_label = ""
    nn_prediction = ""
    draw_finished = False
    first_frame = True
    correct = 0 
    draw_color = (0, 0, 255)
    xp, yp = 0, 0
    count = 0
    end_time = 0
    i_count=0
    start_time = time.time()
    
    #Get capture and set config
    url=0
    cap = cv2.VideoCapture(url)
    cap.set(3, 1288)
    cap.set(4, 728)

    
    hand_detector = hand_tracking.handDetector()
    
    final_img = cv2.imread("imgs/final.jpeg")
    header_img = cv2.imread("imgs/header.jpeg")
    img_canvas = np.zeros((720, 1280, 3), np.uint8)
    
    while True: 
        _, frame = cap.read()
          
    
        if _:
            if (draw_finished or first_frame):
                # Get random class to draw
                idx_label = np.random.randint(0, len(labels_copy))
                actual_label = labels_copy[idx_label]
    
                if first_frame:
                    first_frame = False
                if draw_finished:
                    draw_finished = False
    
            frame = cv2.flip(frame, 1)
            frame = hand_detector.find_hands(frame)
            lm_list = hand_detector.find_position(frame)
    
            if len(lm_list) != 0:
                xp, yp = 0, 0
                x1, y1 = lm_list[8][1:]
                x2, y2 = lm_list[12][1:]
    
                fingers = hand_detector.fingers_up()
    
                # If pointer and middle fingers are up, we can select rubber, pencil or send draw to NN
                if fingers[1] and fingers[2]:
    
                    if y1 < 125:
                        if 1060 < x1 < 1170:
                            draw_color = (0, 255, 0)#Green
                        elif 960 < x1 < 999:
                            draw_color = (0,0,255)#RED
                        elif 850 < x1 < 930:
                            draw_color = (255,255,255)#White
                        elif 780 < x1 < 830:
                            draw_color = (255,255,0)#Cyan
                        elif 730 < x1 < 760:
                            draw_color = (255,0,255)#Purple
                        elif 640 < x1 < 680:
                            draw_color = (0,255,255)#Yellow

                        elif 1190 < x1 < 1280:
                            draw_color = (0, 0, 0)#Eraser
    
                        elif 10 < x1 < 200 and (end_time - start_time) > 5:
                            name = str(i_count)+'.png'
                            img_name = name
                            # saves the image as a png file
                            cv2.imwrite(img_name, img_canvas)
                            i_count+= 1
                            draw_finished = True
    
                    cv2.rectangle(frame, (x1, y1 - 25), (x2, y2 + 25), draw_color,cv2.FILLED)
                    #cv2.line(img_canvas,(xp,yp),(x1,y1),draw_color)
                # If pointer finger is up and middle finger down, can draw/erase
                if fingers[1] and not fingers[2]:
                    cv2.circle(frame, (x1, y1), 6, (0, 0, 255), cv2.FILLED)
    
                    if xp == 0 and yp == 0:
                        xp, yp = x1, y1
                    #eraser
                    if draw_color == (0, 0, 0):
                        cv2.line(frame, (xp, yp), (x1, y1), draw_color, 225)
                        cv2.line(img_canvas, (xp, yp),(x1, y1), draw_color, 225)
                    else:
                        if fingers[1] and fingers[3]:
                            for time2 in range(1):
                                cv2.circle(img_canvas,(x1,y1),20,draw_color)
                                continue
                                pass

                        if fingers[1] and fingers[4] and not fingers[3]:
                            for time1 in range(1):
                                cv2.rectangle(img_canvas,(xp, yp), (x1+30, y1+30),draw_color)
                                continue                    
                                pass
                                #time.sleep(0.1)
                               
    
                        elif fingers[1] and not fingers[2] and not fingers[4] and not fingers[3]:
                            #for time1 in range(1):
                                cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, 20)
                            
    
                    xp, yp = x1, y1
    
            img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
            _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
            img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
            frame = cv2.bitwise_and(frame, img_inv)
            frame = cv2.bitwise_or(frame, img_canvas)
    
            frame[0:125, 0:1280] = header_img
        
            cv2.namedWindow("Air Canvas", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Air Canvas', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  
            cv2.imshow("Air Canvas", frame)
            key = cv2.waitKey(1)
            if key == ord('x') or key == 27:
                count+=8
                cv2.destroyAllWindows()    
            if draw_finished and (end_time - start_time) > 5:
                processed_img = process_image(img_inv, (28, 28))
               
                
                                                
                img_canvas = np.zeros((720, 1280, 3), np.uint8)
                start_time = time.time()
                labels_copy.remove(actual_label)
                count += 1
    
            if count >= 8:
                break
    
        end_time = time.time()
    cap.release()
    cv2.destroyAllWindows()
    

def startApp():
    airCanvas()
airCanvas()