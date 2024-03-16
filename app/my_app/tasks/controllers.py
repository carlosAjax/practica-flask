from flask import Blueprint,render_template

taskRoute = Blueprint('task',__name__,url_prefix='/task')

@taskRoute.route('/home')
def home():
    return render_template('tienda/tasks/home.html')

@taskRoute.route('/products')
def products():
    return render_template('tienda/tasks/products.html')

@taskRoute.route('/single')
def singleProducts():
    return render_template('tienda/tasks/single-products.html')

@taskRoute.route('/store')
def storeCar():
    return render_template('tienda/tasks/store.html')


