import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320,240)
        
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)

            gray = cv2.cvtColor(stream.array, cv2.COLOR_RGB2GRAY)
            cv2.imshow('gray', gray)

            (ret, th1) = cv2.threshold(gray, 127, 225, cv2.THRESH_BINARY)
            cv2.imshow('th1', th1)

            th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imshow('th2', th2)

            th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imshow('th3', th3)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()