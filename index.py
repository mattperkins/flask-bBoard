from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '316be1e776a2a03baf117defaf3e75e1'

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