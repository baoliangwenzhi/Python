# -*- encoding=UTF-8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'


@app.route('/inde3/')
@app.route('/')
def index():
    return "Hello World"


@app.route('/profile/<int:uid>/', methods=['get','post'])
def profile(uid):
    colors = ('red', 'green')
    infos = {'nowcoder':'abc','google':'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)


if __name__ == '__main__':
    app.run(debug=True)
