"""
use flaskDB;
DROP TABLE IF EXISTS account;
create table account(
 id varchar(32),
 pw varchar(64) not null,
 salt varchar(20) not null,
 name varchar(32),
 primary key(id)
);
insert into account values("hosokawa", "b2ea30c8186d1e551d857d0d40e7e6e10e19c7dd540519478ea4e2a3d511a2dc","kmrsmtCDmGKIfFRz7Fde", "細川");
insert into account values("takahashi", "a52f8e280c28c90fa289b5a596398b6c36ff1aa01faf9df02f248a22a24be04f","oz8ywexdbVUIX9jNE8kK", "高橋");
insert into account values("takada", "2bb9d9ad9a1aac7e678b94625109ff7fa4e8de127279b96a6f8cbae56a953b68","uJpZeg3iLU2DfmnO9DkG", "髙田");

password:morijyobi
"""

from flask import Flask, render_template, request, redirect, session
import random
import string
import db
from datetime import timedelta   


app = Flask(__name__)
#Flaskクラスのインスタンスに秘密鍵(256桁のランダムな英文字列)を設定.
app.secret_key = "".join(random.choices(string.ascii_letters, k=256))

@app.route("/")
def top_page():
    return render_template("index.html")

@app.route("/home", methods=['POST'])
def home():
    id = request.form.get("id")
    pw = request.form.get("pw")

    # ログイン認証業務ロジック
    result = db.login(id, pw)

    if result != None:
        session["user"] = True  # セッションにキー：user、バリュー：Trueを格納します。
        session.permanent = True    # セッションの有効期限有効化
        app.permanent_session_lifetime = timedelta(minutes=30) # 有効期限の値の設定
        return render_template("home.html")
    else:
        return render_template("index.html")

@app.route("/home", methods=['GET'])
def home_get():
    # セッションにログイン情報があるか確認
    if "user" in session:
        return render_template("home.html")
    else:
        return render_template("index.html")


@app.route("/menu")
def menu():
    if "user" in session:
        return render_template("menu.html")
    else:
        return render_template("index.html")

@app.route("/logout")
def logout():
    session.pop("user", None)    # セッションの削除
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)