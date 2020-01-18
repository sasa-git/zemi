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

            # 純粋な二値化
            (ret, th1) = cv2.threshold(gray, 127, 225, cv2.THRESH_BINARY)
            cv2.imshow('binary', th1)

            # ガウス分布による二値化
            th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imshow('binary gaussian', th2)

            # 大津の二値化
            (ret3, th3) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            cv2.imshow('original otsu', th3)

            # ガウスフィルタを通した大津の二値化
            # アルゴリズムが自動的にしきい値を計算し てくれ，二つ目の出力値であるretVal として返してくれます．大津の二値化を使わない場合， retVal の値は入力引数に指定したしきい値と同じ値になる
            blur = cv2.GaussianBlur(gray , (5,5), 0)
            (ret4, th4) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            # cv2.imshow('th4', th4)
            text = 'now threshold: ' + str(ret4)
            vi = cv2.putText(th4,text,(10,10),cv2.FONT_HERSHEY_PLAIN, 1,(255,255,0))
            cv2.imshow('gaussian otsu', vi)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()