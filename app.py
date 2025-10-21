from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '':
            return redirect(url_for('index'))
        else:
            session['username'] = username
            return redirect(url_for('index'))
        if __name__ == '__main__':
            app.run(debug=True)
            if __name__ == '__main__':
                app.run(debug=False)
                return redirect(url_for('index'))
            return redirect(url_for('index'))
        return redirect(url_for('index'))
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)