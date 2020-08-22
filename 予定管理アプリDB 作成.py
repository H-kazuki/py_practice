import sqlite3 #DBインポート

dbname = 'test.db'
conn = sqlite3.connect(dbname)


#sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

#todoというtableを作成してみる
createTable = '''create table todo(id INTEGER PRIMARY KEY, month text, day text, time text, plans text)'''
cur.execute(createTable)


#データベースへコミット。これで変更が反映される。
conn.commit()

conn.close()