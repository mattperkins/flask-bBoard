from flask import Flask, render_template
app = Flask(__name__)

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

 if __name__ == '__main__':
  app.run(debug=True)