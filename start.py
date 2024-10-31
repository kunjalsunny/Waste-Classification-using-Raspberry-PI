# import os
# import cv2
# import time
# import RPi.GPIO as GPIO
# from predict import Predict
# # from proximity_class import Proximity
# from stepper_class import Stepper
# 
# GPIO.setmode(GPIO.BOARD)
# proxPin = 16
# GPIO.setup(proxPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# predictor = Predict()
# motor = Stepper((12, 16, 18, 22),1,3,100)
# motor.drop()
# 
# def startCam():
#     cam = cv2.VideoCapture(0)
#     cv2.namedWindow("test")
# 
#     # Creating a directory to store the captured images
#     output_dir = 'captured_images'
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#         
#     image_count = 0
#     while image_count < 31:
#         check, frame = cam.read()
# 
#         cv2.imshow("test", frame)
# #         predictor.inference(frame)
#         global direction
#         direction = predictor.inference(frame)
#         
#         cv2.putText(frame, f'Direction: {direction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# 
#         # Save the captured image
#         image_count += 1
#         image_filename = os.path.join(output_dir, f'image_{image_count}.jpg')
#         cv2.imwrite(image_filename, frame)
#         time.sleep(1)
# 
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         
#     cam.release()
#     cv2.destroyAllWindows()
# 
# #proximity sensor trigger
# try:
#     while True:
#         proxState=GPIO.input(proxPin)
#         if proxState == 1:
#             print('Ready...')
#         else:
#             print('Object Detected...')
#             startCam()
#             motor = Stepper((12, 16, 18, 22),(0x01, 0x02, 0x04, 0x08),direction,3,100)
#             motor.drop()
#             time.sleep(.5)
#             motor.destroy()
# except KeyboardInterrupt:
#     GPIO.cleanup()
#         
#
import os
import cv2
import time
import RPi.GPIO as GPIO
from predict import Predict
from stepper_class import Stepper

GPIO.setmode(GPIO.BOARD)
proxPin = 16
GPIO.setup(proxPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
predictor = Predict()
motor = Stepper((12, 16, 18, 22), 1, 3, 100)

def startCam():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    # Creating a directory to store the captured images
    output_dir = 'captured_images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    image_count = 0
    while image_count < 31:
        check, frame = cam.read()

        cv2.imshow("test", frame)
        direction = predictor.inference(frame)
        cv2.putText(frame, f'Direction: {direction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Save the captured image
        image_count += 1
        image_filename = os.path.join(output_dir, f'image_{image_count}.jpg')
        cv2.imwrite(image_filename, frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cam.release()
    cv2.destroyAllWindows()

try:
    while True:
        proxState = GPIO.input(proxPin)
        if proxState == 1:
            print('Ready...')
        else:
            print('Object Detected...')
#             startCam()
            motor.drop()
            time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
