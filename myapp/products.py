from flask import (Blueprint, abort, flash, g, redirect, render_template, request, url_for)
from myapp.auth import login_required
from . import db 
from .models import Product, User

bp = Blueprint('product', __name__)

@bp.route('/')
def index():
    products = db.session.query(
        Product.id,
        Product.name,
        Product.description,
        Product.create.label('created'),
        Product.price,
        Product.user_id,
        User.username
    ).join(User, Product.user_id == User.id).order_by(Product.create.desc()).all()
    
    return render_template('product/index.html', products=products)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = price = float(request.form['price'].replace(',', '.'))
        error = None

        if not name:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            new_product = Product(name=name, description=description, user_id=g.user.id, price=price)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('product.index'))

    return render_template('product/create.html')

def get_product(id, check_author=True):
    product = db.session.query(
        Product.id,
        Product.name,
        Product.description,
        Product.create.label('created'),
        Product.price,
        Product.user_id,
        User.username
    ).join(User, Product.user_id == User.id).filter(Product.id == id).first()
    
    if product is None:
        abort(404, f"Product id {id} doesn't exist.")

    if check_author and product.user_id != g.user.id:
        abort(403)

    return product

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    product = Product.query.get(id)
    
    if product is None:
        abort(404, f"Product id {id} doesn't exist.")

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = price = float(request.form['price'].replace(',', '.'))
        error = None

        if not name:
            error = 'Name is required.'
        elif not price:
            error = 'Price is required.'

        if error is not None:
            flash(error)
        else:
            product.name = name
            product.description = description
            product.price = price
            
            db.session.commit()
            return redirect(url_for('product.index'))

    return render_template('product/update.html', product=product)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    product = Product.query.get(id)

    if product is None:
        abort(404, f"Product id {id} doesn't exist.")

    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('product.index'))