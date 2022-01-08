import hashlib
pw = input("PW>>")
salt = input("Salt>>")
# 入力値をバイト化
b_pw = bytes(pw, "utf-8")
b_salt = bytes(salt, "utf-8") 
# パスワードとソルトを文字列結合し、ハッシュ化して16進数に変換
hashed_pw = hashlib.sha256(b_pw + b_salt).hexdigest()

# さらに1000回ハッシュする(ストレッチング)
for _ in range(1000):
      hashed_pw = hashlib.sha256(bytes(hashed_pw, "utf-8")).hexdigest()

print(f"ハッシュ化されたPW:{hashed_pw}")
