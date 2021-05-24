from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from app.main import bp
from app.models import Post, Tag

@bp.route('/')
@bp.route('/index')
def index():
    posts = Post.query.order_by(Post.published.desc()).all()

    return render_template('index.html', title='Home', posts=posts)