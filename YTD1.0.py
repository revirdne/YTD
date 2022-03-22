import tkinter as tk
from youtube_transcript_api import YouTubeTranscriptApi
import datetime
 
# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('300x200')
# 画面タイトル
baseGround.title('Youtube Transcript Downloader')
 
# ラベル
label1 = tk.Label(text='youtube url')
label1.place(x=30, y=30)
 
label2 = tk.Label(text='file name')
label2.place(x=30, y=70)
 
label3 = tk.Label(text='timing')
label3.place(x=210, y=70)

label4 = tk.Label(text='.lrc')
label4.place(x=157, y=92)

# テキストボックス
textBox1 = tk.Entry(width=40)
# テキストボックスの値をセット
textBox1.insert(tk.END,'')
textBox1.place(x=30, y=50)
 
# テキストボックス
textBox2 = tk.Entry()
# テキストボックスの値をセット
textBox2.insert(tk.END,'')
textBox2.place(x=30, y=90)

# テキストボックス
textBox3 = tk.Entry(width=10)
# テキストボックスの値をセット
textBox3.insert(tk.END,'0')
textBox3.place(x=210, y=90)
 
def val():
    # Intvarオブジェクトの値を取得
    url = textBox1.get()[32:]
    file = textBox2.get()
    n = float(textBox3.get())

    transcript_list = YouTubeTranscriptApi.list_transcripts(url)

    try:
        transcript = transcript_list.find_manually_created_transcript(['ja','en'])
    except:
        print('字幕が見つかりませんでした')
        #transcript = transcript_list.find_generated_transcript(['ja','en']) #自動翻訳

    file = open(file + '.lrc', mode='w', encoding='utf_8')

    for d in transcript.fetch():
        m , s = (divmod(float(d['start']),60))
        text = '[' + str(int(m)) + ':' + (('{:.02f}'.format(s+n)).zfill(5)).replace('.',':') + ']' + d['text'] +'\n'
        #print('[' + str(int(m)) + ':' + (('{:.02f}'.format(s+n)).zfill(5)).replace('.',':') + ']'+ d['text'])
        file.write(text)
    
# ボタンの作成と配置
button = tk.Button(baseGround,
                text = 'OK',
                # クリック時にval()関数を呼ぶ
                command = val
                ).place(x=30, y=120)
 
baseGround.mainloop()