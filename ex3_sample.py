"""
DROP TABLE IF EXISTS account;
create table account(
 id varchar(32),
 pw varchar(64) not null,
 salt varchar(20) not null,
 name varchar(32),
 primary key(id)
);
"""

import hashlib
import random
import string

print("###### 登録フォーム #####")
id = input("ID>>")
#ランダムに生成したソルト
salt = "".join(random.choices(string.ascii_letters, k=20))
pw = input("PW>>")
name = input("NAME>>")

# 入力値をバイト化
b_pw = bytes(pw, "utf-8")
b_salt = bytes(salt, "utf-8") 

# ライブラリを使ったハッシュ(ソルト&ストレッチング)
# 引数はハッシュアルゴリズム、PW、ソルト、ストレッチング回数
hashed_pw = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 1000).hex()

from mysql.connector import connection, errorcode

def get_connection():
    return connection.MySQLConnection(user='flask',passwd="pass",host='localhost',db='flaskDB')

conn = get_connection()
cur = conn.cursor()
sql = "INSERT INTO account VALUES( %s , %s , %s , %s)"
data = (id, hashed_pw, salt, name)
try:
      cur.execute(sql, data)
      conn.commit()
      print(name+"さんのアカントを登録しました。")
except Exception as e:
      print("SQL実行に失敗：" , e)

cur.close()
conn.close()

#debug用登録内容の確認
conn = get_connection()
cur = conn.cursor()

sql = "SELECT * FROM account WHERE id = %s AND pw = %s"

try:
      cur.execute(sql, (id, hashed_pw))
except Exception as e:
      print("SQL実行に失敗：" , e)

result = cur.fetchone()

cur.close()
conn.close()

print(f"DBに登録されたデータは \
      \nID:{result[0]} \
      \nPW:{result[1]} \
      \nSALT:{result[2]} \
      \nNAME:{result[3]}")
