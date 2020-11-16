from flask import Flask, render_template
import random

app = Flask(__name__)

# 랜덤으로 로또를 추출하는 함수
@app.route("/")
@app.route("/randomLotto")
def randomLotto():
    lotto = sorted(random.sample(range(1, 46), 6))
    return render_template("index.html", variable=lotto)

# TOP10으로 로또를 추출하는 함수
@app.route("/")
@app.route("/top10Lotto")
def top10Lotto():
    top10_list = [34, 43, 27, 17, 18, 39, 12, 14, 40, 1]
    lotto_top10 = sorted(random.sample(top10_list, 6))
    return render_template("index.html", variable=lotto_top10)

# 로또 1등 판매점 지도로 연결하는 코드
@app.route("/lotto_store")
def lotto_store():
    return render_template("lotto_store.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')