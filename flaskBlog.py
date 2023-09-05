from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9ebcf1af1b9a9c10d1acb0f9a52c7a8'

posts = [{'author':'Brock Houston',
          'title':'Thin AI ChatGPT Apps',
          'content':'First post content',
          'datePosted':'August 30, 2023'},

        {'author':'Savannah Thomson',
          'title':'How Flossing Can Save Your Life',
          'content':'Second post content',
          'datePosted':'August 31, 2023'},]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'about')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)


if __name__ == "__main__":
    app.run(debug = True)
