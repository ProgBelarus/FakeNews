from datetime import datetime
from app import db, bcrypt  # app/__inti__.py
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    roles = db.relationship('Role', secondary='user_roles')
    evals = db.relationship('Evaluation', backref='user', lazy=True)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    @classmethod
    def create_user(cls, user, email, password):
        user = cls(user_name=user,
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        return user

    def __repr__(self):
        return 'User: {} with password {}'.format(self.user_email, self.user_password)

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    @classmethod
    def create_role(cls, name):
        role = cls(name=name)
        db.session.add(role)
        db.session.commit()
        return role

    def __repr__(self):
        return '{}'.format(self.name)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))