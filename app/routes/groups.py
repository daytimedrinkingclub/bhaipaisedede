# app/routes/groups.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.group import Group
from app import db

bp = Blueprint('groups', __name__)

@bp.route('/groups')
@login_required
def groups():
    groups = Group.query.all()
    return render_template('main/groups.html', groups=groups)

@bp.route('/groups/create', methods=['GET', 'POST'])
@login_required
def create_group():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        group = Group(name=name, description=description)
        db.session.add(group)
        db.session.commit()
        flash('Group created successfully')
        return redirect(url_for('groups.groups'))
    return render_template('main/create_group.html')