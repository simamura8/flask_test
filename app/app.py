

# flaskクラスをインポート
from flask import Flask
from flask import render_template

# インスタンス化
# __name__：importされてるときは、import名。mainのときは"__main__"
app = Flask(__name__)

# インスタンスのメソッドを使用
# 検索されたら、index関数を実行。
@app.route('/')
def index():
    # メソッドにtemplatesディレクトリのファイル名を指定してわたす
    return render_template('index.html')

# test
@app.route('/japan/<city>')
# japan/<引数>　でもらい、その引数をhello.htmlにわたす。
def hello(city):
    return render_template('hello.html', city=city)

if __name__ == "__main__":
    # サーバーを立ち上げる。(bashでflask run するのと同じ)
    # appインスタンスのrunメソッドを使用。
    app.run(host='0.0.0.0', port=5000, debug=True)