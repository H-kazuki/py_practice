import requests #html取得のライブラリ
from bs4 import BeautifulSoup #html解析ライブラリ
import calendar #カレンダーライブラリ
import datetime #現在の日時取得のライブラリ
import sqlite3 #データベース


#日付を格納する空リスト
dayDate = []
#天気を格納する空リスト
weatherDate = []


#今日の年月日の文字列取得
today = str(datetime.date.today())
#上記の文字列をリスト化
todayls = today.split("-")
#上記のリスト内の文字列の年月日を数字へ
todayls = [int(i) for i in todayls]
#カレンダーを表示
calendar.prmonth(todayls[0], todayls[1], w = 7, l = 2)
#今日の日付を表示



#ホームページを指定
load_url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
#上記のURLを取得
html = requests.get(load_url)
#htmlを解析する
soup = BeautifulSoup(html.content, "html.parser")

#今日と明日の日付をリスト化
for element in soup.find_all(class_ = "date"):
    dayDate.append(element.text)
#今日と明日の天気をリスト化
for element in soup.find_all(class_ = "pict"):
    weatherDate.append(element.text)

print("ﾟ･:,｡ﾟ･:,｡★ﾟ･:,｡ﾟ･:,｡☆ﾟ･:,｡ﾟ･:,｡★ﾟ･:,｡ﾟ･:,｡☆ﾟ･:,｡ﾟ･:,｡★ﾟ･:,｡ﾟ･:,｡☆")
print("　")
print("今日は" + dayDate[0])
print("●天気は" + weatherDate[0])
print("　")
print("明日は" + dayDate[1])
print("●天気は" + weatherDate[1])
print("　")
print("ﾟ･:,｡ﾟ･:,｡★ﾟ･:,｡ﾟ･:,｡☆ﾟ･:,｡ﾟ･:,｡★ﾟ･:,｡ﾟ･:,｡☆ﾟ･:,｡ﾟ･:,｡★ﾟ･:,｡ﾟ･:,｡☆")
print("　")


#ここより下は予定管理の機能

dbname = 'test.db'
conn = sqlite3.connect(dbname)

#sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

x = 0
while x == 0:
    print("数字で選択して下さい")
    print("　")
    menuSelect = int(input("1.予定の確認　　2．予定の登録　　3.予定の削除　　4.終了:"))
    if menuSelect == 1: #登録済みの予定確認
        selectSql = "select * from todo"
        cur.execute(selectSql)
        planList = cur.fetchall()
        print("------------------------------------------------------------------------")
        for plan in planList:
            print("------------------------------------------------------------------------")
            print("　")
            print("●予定ID：" + str(plan[0]))
            print("●" + plan[1] + "月" + plan[2] + "日" + "  " + plan[3])
            print("●予定：" + plan[4])
            print("　")
            print("------------------------------------------------------------------------")

        print("------------------------------------------------------------------------")

         
    elif menuSelect == 2: #予定の登録
        y = 0
        while y == 0:
            print("予定を入力して下さい")
            month= input("「月」を入力:")
            day = input("「日」を入力:")
            time = input("時間帯を入力(例  14：05):")
            plans = input("予定を入力:")
            z = 0
            while z == 0:
                print("下記の内容で間違いないでしょうか？")
                print("----------------------------------------------------")
                print("　")
                print(month + "月" + day + "日" + " " + time)
                print("予定：" + plans)
                print("　")
                print("----------------------------------------------------")
                inpAlright = int(input("(数字で選択して下さい)　1.はい　　2．いいえ:"))
                if inpAlright == 1:
                    #入力した内容を”test”データベースへ入れる
                    inputSql = 'insert into todo(month, day, time, plans) values(?, ?, ?, ?)'
                    cur.execute(inputSql,(month, day, time, plans))
                    print("　")
                    print("上記の内容で登録しました")
                    #処理終了　while y ループを抜けるため、yに1を代入
                    y = 1
                    #while z　ループを抜ける
                    break
                        
                elif inpAlright == 2:
                    print("　")
                    print("もう一度入力して下さい")
                    break
                        
                else:
                    print("　")
                    print("正しく入力されていません")



    elif menuSelect == 3: #予定の削除
        print("　")
        deleteId = input("削除する予定を予定IDで選んで下さい:")
        i = 0
        while i == 0:
            print("　")
            print("本当に削除しますか？")
            delAlright = int(input("(数字で選択して下さい)　1.はい　　2．いいえ:"))
            if delAlright == 1:
                deletSql = "delete from todo where id = ?"
                cur.execute(deletSql, deleteId)
                break

            elif delAlright == 2:
                break

            else: 
                print("　")
                print("正しく入力されていません")



    elif menuSelect == 4: #終了
        break
            

    else:
        print("　")
        print("正しく入力されていません")


conn.commit()
conn.close()