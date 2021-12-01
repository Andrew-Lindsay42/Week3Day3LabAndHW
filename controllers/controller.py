from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders=orders)

@app.route('/orders/<int:number>')
def order(number):
    number -= 1
    return render_template('order.html', order_num = number + 1, order=orders[number])
