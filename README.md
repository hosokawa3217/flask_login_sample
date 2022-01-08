### ログイン処理


問2：登録フォームにID、PW、名前を入力し、登録ボタンを押すとDBにその情報を登録するアプリケーションを作成せよ。
      なお、ソルトはIDを使用すること。ストレッチング回数は任意とする。
      テーブルは自分で作成すること。(SQLも提出すること)

#### 問2 table
```
~$ mysql -h localhost -u flask -ppass flaskDB

mysql> create table account(
id varchar(32)    ->  id varchar(32),
    ->  pw varchar(64) not null,
    ->  name varchar(32),
    ->  primary key(id)
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql> \q
```

#### 問3 table
登録フォームにID、PW、名前を入力し、登録ボタンを押すとDBにその情報を登録するアプリケーションを作成せよ。
なお、ソルトは20文字のランダムな文字列を使い、登録の際に生成したソルトもDBに一緒に登録すること。
(ストレッチング回数は任意)
テーブルは自分で作成すること。(SQLの提出は不要)

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