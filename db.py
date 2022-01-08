


from mysql.connector import connection, errorcode
import hashlib

# IDとPWを元にログインの判定
def login(id, pw):
    # IDを元にDBからソルトを取得する
    salt = search_salt(id)

    # 対象のIDが存在しない
    if salt == None:
        return None # ログイン失敗

    # PWハッシュ
    b_pw = bytes(pw, "utf-8")
    b_salt = bytes(salt, "utf-8")
    hashed_pw = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 2560).hex()

    # IDとハッシュPWを使ってDB問い合わせ
    result = search_account(id, hashed_pw)

    return result

# ソルト取得処理
def search_salt(id):
    conn = get_connection()
    cur = conn.cursor()

    sql = "SELECT salt FROM account WHERE id = %s"

    try:
        cur.execute(sql, (id,))
    except Exception as e:
        print("SQL実行に失敗：" , e)

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return result[0]

    return None

# ユーザ情報取得処理
def search_account(id, pw):
    conn = get_connection()
    cur = conn.cursor()

    sql = "SELECT id, name FROM account WHERE id = %s AND pw = %s"

    try:
        cur.execute(sql, (id,pw))
    except Exception as e:
        print("SQL実行に失敗：" , e)

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result

# DBとのコネクションを取得
def get_connection():
    return connection.MySQLConnection(user='flask',passwd="pass",host='localhost',db='flaskDB')
