# app/routes/expenses.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.expense import Expense
from app import db

bp = Blueprint('expenses', __name__)

@bp.route('/expenses')
@login_required
def expenses():
    expenses = Expense.query.all()
    return render_template('main/expenses.html', expenses=expenses)

@bp.route('/expenses/create', methods=['GET', 'POST'])
@login_required
def create_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        group_id = request.form['group_id']
        expense = Expense(amount=amount, description=description, payer_id=current_user.id, group_id=group_id)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added successfully')
        return redirect(url_for('expenses.expenses'))
    return render_template('main/create_expense.html')