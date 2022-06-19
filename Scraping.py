import datetime
import urllib.request
import csv
import time
import os
from bs4 import BeautifulSoup

#url接続
url = input("Type Here The Site Domain----->")
html = urllib.request.urlopen(url)

#url接続できたら
if html :

    #-----------------必須入力の入力------------------#

    print("connecting....\n")
    print(".......OK complete....\n")

    target_tag = input('Type your `target tag`. example:) h2,p ------>')

    print("\n.......OK complete....\n")

    target_class = input('Type your `target class`.You can select nothing.if your target has not class,Click Enter.... example:) tag_normal ------>')

    print('\n--------Your Target--------\nTarget Tag：'+ target_tag + '\nTarget Class：' + target_class + '\n----------------------\n')
    print(".......OK complete....\n")

    #----------------------------------------------#

    #指定したタグの情報取得
    deta = BeautifulSoup(html,"html.parser")
    tag_detas = deta.find_all(target_tag,attrs={'class':target_class})
    tag_deta_length = len(tag_detas)

    #csv名にユニークにする
    dt_now = datetime.datetime.now()
    date_name = dt_now.strftime('%Y-%m-%d-%H-%M-%S') + '.csv'


    #csvを新規作成＆書き込み
    with open('csv/' + date_name ,'w',encoding="utf_8") as csv_file:
        fieldnames = ['id','comment']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(tag_deta_length):
            TAG = tag_detas[i].getText()
            print(str(i) +' | '+ TAG + '\n')
            writer.writerow({'id':i,'comment':TAG})

    YorN = input('do you want to save image too? (Y/n)----->')

    match YorN:
        case "Y":
            #ディレクトリ作成させ、そこに動画を保存させる。
            Dir_name = input('type your image directory`s name----->')
            print("\n.......OK done...\n")
            os.mkdir('img/'+ Dir_name)

            #画像保存するタグを入力させる。
            img_class = input('type your img class. but you can type nothing------->')
            img_detas = deta.find_all('img',attrs={'class':img_class})

            if img_detas :

                print('\nthe your selected image was successful......\n')

                #イメージのダウンロードリンク格納用のリスト変数
                img_deta = []

                #ダウンロードクールダウン 1sec
                sleep_time = 1

                #For文の繰り返し回数を数える i++
                i = 0;

                #画像の繰り返し保存を実行する　&&　サーバーへの負担を軽減するためにクールダウンを設定
                for img_deta in img_detas:

                    #ソースを抽出
                    img_src = img_detas.append(img_deta.get('src'))
                    fileName = os.path.basename(img_src)

                    #クールダウン
                    time.sleep(sleep_time)

                    #ファイル名と拡張子の抽出
                    # basename,extension = os.path.splitext(fileName)

                    #ファイル保存用名変数を作成
                    # img_fileName = str(i) + '.' + extension

                    #画像をダウンロード
                    download_img(url,fileName)

                    i += 1

        case "n":

            print('....OK all is already done..... and csv already saved....check it!!')

else :
    print("can not connet at this...")

