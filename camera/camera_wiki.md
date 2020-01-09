## openCVについて

[日本語Wiki](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_image_display/py_image_display.html)


## ord()について

https://python.civic-apps.com/char-ord/

`ord("q")`でアスキーコードを返す

```py
>>> ord("a")
97
```

ユニコードオブジェクトの場合は、ユニコードを整数で返す。(python2)

```py
>>> ord(u"あ")
12354
>>> hex(ord(u"あ"))
0x3042
>>> u"\u3042" == u"あ"
True
```

python3の場合は、文字列がはじめからユニコード文字列なので、uを付けなくてもよい。

```py
>>> ord("あ")
12354
```

`chr()`でアスキーコード→文字へ

```py
>>> chr(97)
'a'
```

ユニコードはunichr(python2)

```py
>>> unichr(12354)
u"\u3042" 
```

python3でははじめから文字列がユニコードなのでunichr関数は存在せずに、chr関数で文字コードから文字を得られる。（出力結果はpython2と違うが同値）

```py
>>> chr(12354)
"あ" 
```

## waitKey(0) についてる0xFFって何？
https://www.it-swarm.net/ja/python/cv2waitkey%EF%BC%881%EF%BC%89%E3%81%AE0xff%E3%81%AF%E4%BD%95%E3%81%A7%E3%81%99%E3%81%8B%EF%BC%9F/824142736/

NumLockがアクティブになっている場合は、ord（ 'q'）が異なる数値を返す可能性があることに注意することも重要です（他のキーでも発生する可能性があります）。たとえば、cを押すと、コードは次のようになります。

```py
key = cv2.waitKey(10) 
print(key) 
```

返却値

```py
1048675 when NumLock is activated 
99 otherwise
```

これらの2つの数値を2進数に変換すると、次のことがわかります。

```py
1048675 = 100000000000001100011
99 = 1100011
```

ご覧のとおり、最後のバイトは同じです。 NumLockの状態が原因で残りが発生するため、この最後のバイトだけを取得する必要があります。したがって、以下を実行します。

```py
key = cv2.waitKey(33) & 0b11111111  
# 0b11111111 is equivalent to 0xFF
```

キーの値は同じままであるため、質問などの任意のキーと比較できます

```py
if key == ord('q'):
```

## その他役立ちそうな参考サイト

[OpenCVインストール](https://qiita.com/takahiro_itazuri/items/a67dd3bb7f5f88ca9dd8#compile-and-install-opencv)

[人の顔識別](https://www.pc-koubou.jp/magazine/19205)

[顔認識2](https://kokensha.xyz/raspberry-pi/raspberry-pi-opencv-video-face-detection/)

[ラズパイカメラで遊ぼう](http://blog.livedoor.jp/victory7com/archives/27752962.html)

## おまけ camera-test.pyの解説

```py
import picamera
import picamera.array
import cv2

# カメラ初期化 PiCamera()で生成したオブジェクトをcamera変数で扱う
with picamera.PiCamera() as camera:
    # カメラの画像をリアルタイムで取得するための処理
    with picamera.array.PiRGBArray(camera) as stream:
        # 解像度の設定
        camera.resolution = (320,240)
        
        while True:
             # カメラから映像を取得する（OpenCVへ渡すために、各ピクセルの色の並びを"BGR"の順番にする）
            camera.capture(stream, 'bgr', use_video_port=True)
            # カメラから取得した映像を表示する 第一引数でウィンドウの名前を指定
            cv2.imshow('frame', stream.array)

            # cv2.waitKey() はキーボード入力を処理する関数です．引数は入力待ち時間でミリ秒単位で指定します．この関数は，指定された時間だけキーボード入力を受け付けます．入力待ちの間に何かのキーを打てば，プログラムはそれ以降の処理を実行します．引数に 0 を指定した時は，何かしらのキーを打つまでキー入力を無期限で待ち続けます．以下で説明しますが，特定のキー入力のみを待つ(例えば a のみを待つ)ことも可能です．
            # & 0xFFについては## waitKey(0) についてる0xFFって何？ 参照
            # ord('q')でqをアスキーコードに変換
            if cv2.waitKey(1) & 0xFF == ord('q'):
                # while を抜ける
                break
            # カメラから読み込んだ映像を破棄する
            # seek(0) ファイルの先頭に移動
            stream.seek(0)
            # ストリームのサイズを、指定された size バイト (または size が指定されていない場合、現在位置) に変更
            stream.truncate()

        # imshowで出した画面を消去
        cv2.destroyAllWindows()
```