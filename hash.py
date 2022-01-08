import hashlib
pw=input("PW>>")
# 入力値をバイト化
b_pw=bytes(pw,"utf-8")
# バイト化したパスワードをSHA256でハッシュ化し、16進数に変換
hashed_pw=hashlib.sha256(b_pw).hexdigest()
print(f"ハッシュ化されたPW：{hashed_pw}")
