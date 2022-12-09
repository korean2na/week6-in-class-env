from . import bp as app
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.blog.models import User, Post
from flask_login import current_user, login_required

@app.route('/posts')
@login_required
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html.j2', posts=all_posts)

@app.route('/posts/<id>')
@login_required
def post_by_id(id):
    post = Post.query.get(id)
    return render_template('post-single.html.j2', post=post)

@app.route('/create-post', methods=['POST'])
@login_required
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    new_post = Post(title=title, body=body, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash('Post created successfully', 'success')
    return redirect(url_for('blog.posts'))
