from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '316be1e776a2a03baf117defaf3e75e1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utc)
  content = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"

posts = [
 # dictionary 1
 {
  'author': 'DORMshed',
  'title': 'Insert One',
  'Content': 'Lorem Ipsum',
  'date_posted': 'September 22, 2018'
 },
 # dictionary 2
 {
  'author': 'DORMshed',
  'title': 'Insert Two',
  'Content': 'Lorem Ipsum',
  'date_posted': 'September 21, 2018'
 }
]

@app.route("/")
@app.route("/home")
def home():
 return render_template('home.html', posts=posts, title='Latest')

@app.route("/about")
def about():
 return render_template('about.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
 form = RegistrationForm()
 if form.validate_on_submit():
  flash(f'Account successfully created for {form.username.data}!', 'success')
  return redirect(url_for('home'))
 return render_template('signup.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
 form = LoginForm()
 if form.validate_on_submit():
   if form.email.data == 'admin@blog.com' and form.password.data == 'password':
    flash('You have been logged in!', 'success')
    return redirect(url_for('home'))
   else:
    flash('Login failed! Please review your username and password', 'danger')
 return render_template('login.html', title='Login', form=form)




 if __name__ == '__main__':
  app.run(debug=True)