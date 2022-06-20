import function
import datetime
import urllib.request
import urllib.error
import csv
import time
import os
import uuid
import requests
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
    html_deta = BeautifulSoup(html,"html.parser")
    tag_detas = html_deta.find_all(target_tag,attrs={'class':target_class})
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
            Dir_name = input('\ntype your image directory`s name----->')
            print("\n.......OK done...\n")
            img_save_Dir = f'img/{Dir_name}/'
            os.mkdir(img_save_Dir)

            #画像保存するタグを入力させる。
            img_class = input('type your img class. but you can type nothing------->')
            img_tags = html_deta.find_all('img',attrs={'class':img_class})

            if img_tags :

                print('\nthe your selected image was successful......\n')

                #ダウンロードクールダウン 1sec
                sleep_time = 1

                count = 0

                #ソースを抽出
                for img in img_tags:

                    r = requests.get(img['src'])

                    with open(str(img_save_Dir) + str(uuid.uuid4()) + str('.jpeg'),'wb') as file:
                        file.write(r.content)
                        time.sleep(sleep_time)
                        print(f'DL:---->{img["src"]}\n')


                    count += 1

            print(f'{ count } picture has saved.......bye!!')

        case "n":

            print('......bye')

else :
    print("can not connet at this...")

