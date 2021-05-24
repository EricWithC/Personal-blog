import click
from app import db
from app.models import User

def register(app):
    @app.cli.command('create-user')
    @click.option('--username', '-u', prompt='Your username')
    @click.option('--email', '-e', prompt='Your email')
    @click.password_option()
    def create_user(username, email, password):
        """Create a new User"""
        user = User(username=username, email=email)
        if password:
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
        else:
            raise RuntimeError('Passwords not matching')