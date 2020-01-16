# openCVについて

**ちゃんとしたWikiの方に移動しました**
[リンクはこちら](https://github.com/sasasoni/zemi/wiki/OpenCV_wiki)

基本ここでは4.2.0版について説明します

[公式Wiki(4.2.0版)](https://docs.opencv.org/4.2.0/index.html)

[日本語Wiki](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/index.html#)

## openCVとは？
OpenCV（オープンシーヴィ、英語: Open Source Computer Vision Library）とはインテルが開発・公開したオープンソースのコンピュータビジョン向けライブラリ
~~By Wikipedia~~

OpenCVはC++で記述されたライブラリ
opencv-pythonはそれをpythonで使用できるようにするバインディングライブラリ(要するにC++で書かれたopenCVをPythonで使えるようになるもの)[*](https://teratail.com/questions/165179)


## インストール方法
主に二つある
- 割と楽なpip を使った方法(多分楽)
    - [公式ドキュメント(英語だけど確実)](https://pypi.org/project/opencv-python/)

    - [ブログ 丁寧な説明で有益なテクニックも書かれてる](http://asukiaaa.blogspot.com/2018/07/pythonopencvraspi.html)

    >必要なプログラムがOSにインストールされていない場合、`import cv2`を実行したときに下記のようなエラーが出ます。
    >```py
    >>>> import cv2
    >Traceback (most recent call last):
    >File "<stdin>", line 1, in <module>
    >File "/usr/local/lib/python3.5/dist-packages/cv2/>__init__.py", line 3, in <module>
    >    from .cv2 import *
    >ImportError: libQtTest.so.4: cannot open shared >object file: No such file or directory
    >>>>
    >```
    >こうなったときは「debian [エラーになったライブラリ名]」で検索>して、出てきたパッケージをインストールすることで解決できます。


- ソースコードをダウンロードしてビルドする方法(時間かかるけど学びが大きい)
    - [公式ドキュメント(英語だけど確実)](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)
    - [qiita(シンプル、ほぼ公式の日本語版)](https://qiita.com/hidakanoko/items/3f2f6ae9b5af2b06eec6)

    - [qiita(ちょっと独特,中級者向け)](https://qiita.com/takahiro_itazuri/items/a67dd3bb7f5f88ca9dd8#finish-installing-opencv-on-your-rasberry-pi)

    - [ブログ(ちょっとpyenv使用,中級者向け)](https://zv-louis.hatenablog.com/entry/2018/05/08/063000)


    いくつかの方法みて試行錯誤するのもいいかも。後順番は割と大事

    そしてとにかくググること！！

### その他先人達の知恵
[makeで苦戦した先人](https://hakengineer.xyz/2018/01/24/post-950/)

[pipで苦戦した先人](https://qiita.com/XM03/items/48463fd910470b226f22)

[pipで楽を追求した先人(しかし筆者の環境では躓いた)](https://qiita.com/masaru/items/658b24b0806144cfeb1c)

## インストールされてるかの確認

これが動けばとりあえずインストールできてる

```py
import cv2
cv2.version
```

## 実際に試してみたインストール方法

pipを使ったインストールを試してみました。
OSのバージョンの違い、OpenCVのバージョンの違いで必ずしもこれで成功するとは限りません！
失敗したら笑いましょう。

### バージョン確認

```
-> % lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 9.11 (stretch)
Release:	9.11
Codename:	stretch
```

早速公式ドキュメントを参考にインストールしてみましょう

```
$ pip install opencv-python
$ pip install opencv-contrib-python
```

⚠️注意⚠️

`pip install`でエラーが起きたら

```
-> % pip install opencv-python
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: opencv-python in /usr/local/lib/python3.5/dist-packages (3.4.4.19)
Requirement already satisfied: numpy>=1.12.1 in /usr/lib/python3/dist-packages (from opencv-python) (1.12.1)
WARNING: You are using pip version 19.3; however, version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

こんなのが出たら、pipのバージョンが違うので怒られてます。最後の行の通りに +sudo をつけて`sudo pip install --upgrade pip`を打ってみましょう。
sudoつけてなかったら多分許可がありません的なので怒られると思います

早速やってみるぞ〜

```
-> % python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.5/dist-packages/cv2/__init__.py", line 3, in <module>
    from .cv2 import *
ImportError: libhdf5_serial.so.100: cannot open shared object file: No such file or directory
```

ドキュメント通りにやったら怒られました。最後の行をみてみると、`libhdf5_serial.so.100`てのがなさそうです。
`libhdf5-100`でググると、[こんなサイトを見つけました](https://qiita.com/atuyosi/items/5f73baa08c3408f248e8)
どうやら`apt install`でインストールが必要なライブラリがあるそうです。

`apt search`でライブラリを探してみます

```
-> % sudo apt search libhdf5-100
ソート中... 完了
全文検索... 完了
libhdf5-100/oldstable 1.10.0-patch1+docs-3+deb9u1 armhf
  Hierarchical Data Format 5 (HDF5) - runtime files - serial version
```

`libhdf5-100/oldstable`てのがライブラリにあるそうです。これをインストールしてみます。

`sudo apt install libhdf5-100/oldstable -y` (-yコマンドがあれば一発でインストールしてくれます)

さあできるかな？？

```
-> % python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.version
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cv2.cv2' has no attribute 'version'
>>> cv2.__version__
'3.4.4'
```

**できたあああああああ**

## その他役立ちそうな参考サイト

[OpenCVインストール](https://qiita.com/takahiro_itazuri/items/a67dd3bb7f5f88ca9dd8#compile-and-install-opencv)

[人の顔識別](https://www.pc-koubou.jp/magazine/19205)

[顔認識2](https://kokensha.xyz/raspberry-pi/raspberry-pi-opencv-video-face-detection/)

[ラズパイカメラで遊ぼう](http://blog.livedoor.jp/victory7com/archives/27752962.html)

[色々なフィルター](https://news.mynavi.jp/article/zeropython-34/)

[(Wiki)動画の扱い方](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_video_display/py_video_display.html)

[(Wiki)画像を扱う](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_image_display/py_image_display.html)

[OpenCVを使わずに画像処理にチャレンジ！](https://qiita.com/secang0/items/1229212a37d8c9922901)

# おまけ camera-test.pyの解説

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

## ord()/chr()について

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