from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# In-memory vote counters
votes = {
    "Cats": 0,
    "Dogs": 0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        choice = request.form.get('vote')
        if choice in votes:
            votes[choice] += 1
            session['voted_for'] = choice
            return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    voted_for = session.get('voted_for')
    if not voted_for:
        return redirect(url_for('index'))
    return render_template('result.html', voted_for=voted_for)

if __name__ == '__main__':
    app.run(debug=True)
