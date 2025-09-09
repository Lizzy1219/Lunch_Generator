from flask import Flask, render_template
from random import randint

app = Flask(__name__)

food = [
    '漢堡', '披薩', '壽司', '三明治' ,'沙拉' ,'便當', '麵線', '乾麵', '燒烤', '火鍋',
    '海鮮', '咖啡廳', '麵包', '自助餐', '義大利麵', '素食', '炸雞', '水餃', '排餐', '滷肉飯',
    '炒飯', '炒麵', '健康餐', '雞胸肉', '水煎包', '韓式料理', '泰式料理', '拉麵', '燒臘', '茶葉蛋',
    '丼飯', '河粉', '稀飯', '蛋餅', '滷味', '鹹酥雞', '咖哩', '蛋包飯', '肉粽', '湯麵',
    '煎餃', '肉包', '飯糰', '燉飯', '蔥油餅', '鐵板燒', '麻辣燙', '永和豆漿', '雞排', '海南雞飯'
]

@app.route("/index")
def index():
    return render_template("index.html", food = food)

@app.route("/lottery")
def lottery():
    num = randint(0, 49)
    return render_template("index.html", food = food, ans = food[num])

app.run()