import hashlib
pw = input("PW>>")
salt = input("Salt>>")
# 入力値をバイト化
b_pw = bytes(pw, "utf-8")
b_salt = bytes(salt, "utf-8") 

# ライブラリを使ったハッシュ(ソルト&ストレッチング)
# 引数はハッシュアルゴリズム、PW、ソルト、ストレッチング回数
hashed_pw = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 1000).hex()

print(f"ハッシュ化されたPW:{hashed_pw}")
