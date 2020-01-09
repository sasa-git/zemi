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