from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

posts = [
    {
        'author':'Twitter',
        'title': 'Tweet 01',
        'content': 'Twitter is X',
        'date_posted': 'Jan 18,2020'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="about")

if __name__ == '__main__':
    app.run(debug=True)