
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

companies = []


def is_valid_password(password):
    if len(password) < 6:
        return False

    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    has_special = any(char in special_chars for char in password)

    return has_letter and has_digit and has_special



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        if not login:
            flash("Логін не може бути порожнім!")
            return redirect(url_for('register'))

        if not is_valid_password(password):
            flash("Пароль має бути від 6 символів, містити літеру, цифру та спецзнак.")
            return redirect(url_for('register'))

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        session['user_id'] = 1
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/')
def index():
    return "Головна сторінка. Перейдіть на <a href='/register'>Реєстрацію</a>"



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Ви вийшли з системи")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)