from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
 return '''
 <div>
  <p>Multi-line inline template</p>
  <h4>This is not ideal!</h4> 
 <div>
 ''' 

@app.route("/about")
def about():
 return "<h1>About!</h1>"

 if __name__ == '__main__':
  app.run(debug=True)