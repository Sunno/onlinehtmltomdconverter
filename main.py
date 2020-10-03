from flask import Flask, render_template, request
from markdownify import markdownify as md


app = Flask('HTML to MD')


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {}
    if request.method == 'POST':
        context['converted'] = md(request.form['html'])
        context['html'] = request.form['html']
    return render_template('home.html', **context)
