from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders=orders)

@app.route('/orders/<int:number>')
def show_order(number):
    if number > 0 and number <= len(orders):
        return render_template('order.html', order_num = number, order=orders[number - 1])
    else:
        return 'Order not found'
