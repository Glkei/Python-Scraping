import datetime
import urllib.request
import csv
import time
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


    print('....OK csv already saved....')

else :
    print("can not connet at this...")

