

# flaskクラスをインポート
from flask import Flask

# インスタンス化
# __name__：importされてるときは、import名。mainのときは"__main__"
app = Flask(__name__)

# インスタンスのメソッドを使用
# 検索されたら、index関数を実行。
@app.route('/')
def index():
    return "<h1>Hello world!<h1>"

if __name__ == "__main__":
    # サーバーを立ち上げる。(bashでflask run するのと同じ)
    # appインスタンスのrunメソッドを使用。
    app.run(host='0.0.0.0', port=5000)