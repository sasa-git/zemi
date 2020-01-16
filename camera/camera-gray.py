import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320,240)
        
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)

            gray = cv2.cvtColor(stream.array, cv2.COLOR_RGB2GRAY)

            cv2.imshow('frame', stream.array)
            cv2.imshow('gray', gray)

            (ret, binary) = cv2.threshold(gray, 127, 225, cv2.THRESH_BINARY)
            cv2.imshow('binary', binary)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()