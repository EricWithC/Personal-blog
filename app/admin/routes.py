from flask import render_template, flash, redirect, url_for
from app import db
from app.admin import bp
from app.admin.forms import PostForm, TagForm
from app.models import Post, Tag

@bp.route('/admin_area')
def admin_area():
    return render_template('admin/index.html', title='Admin')

@bp.route('/admin_area/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    form.tags.choices = [(tag, tag.name) for tag in Tag.query.all()]
    print(form.tags.data)
    print(form.tags.choices)
    if form.validate_on_submit():
        print(form.tags.data)
        post = Post(title=form.title.data, body=form.body.data, tags=form.tags.data)
        db.session.add(post)
        db.session.commit()
        flash('You published a new post!')
        return redirect(url_for('main.index'))

    return render_template('admin/create_post.html', form=form)

@bp.route('/admin_area/create_tag', methods=['GET', 'POST'])
def create_tag():
    form = TagForm()
    if form.validate_on_submit():
        tag = Tag(name=form.name.data)
        db.session.add(tag)
        db.session.commit()
        flash('You published a new tag!')
        return redirect(url_for('main.index'))

    return render_template('admin/create_tag.html', form=form)