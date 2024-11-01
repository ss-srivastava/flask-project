from flask import Flask, render_template


# Create a Flask Instance
app=Flask(__name__)

#create a route decorator
@app.route('/')
def home():
   friend_list=['ram', 'ritik','siddharth','juhi','vinayak','juhi richhariya',96 ,99.02]
   f_list=['ram', 'ritik','siddharth','juhi','vinayak','juhi richhariya']
   return render_template('index.html',list=friend_list, user='satyam srivastava',f_list=f_list)
   # return '<h1> hello world this is the home page </h1>'

@app.route('/user/<username>')
def user(username):
   name="this is <strong>bold</strong> text"
   return render_template('user.html',u=name, username=username)
   # return '<h1>Hello {}</h1>'.format(username)

@app.route('/<username>')
def users(username):
   return '<h1>Hello this is the second {} </h1>'.format(username)

#Create custom error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
   return render_template('500.html'), 500



