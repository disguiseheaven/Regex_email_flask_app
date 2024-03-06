from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def home_page():
    return(render_template("home.html"))

@app.route('/regex_match', methods=['GET', 'POST'])
def regex_matching():
    matches = []
    if request.method == 'POST':
        pattern = request.form['pattern']
        string = request.form['string']

        matches = re.findall(pattern, string)

    return render_template('regex_pattern.html', matches=matches)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


@app.route("/email_valid", methods = ['POST', 'GET'])
def email_validation():
    error_message = None
    if request.method == 'POST':
        email = request.form['email']
        if is_valid_email(email):
            return render_template('email.html', valid_email=email)
        else:
            error_message = "Invalid email address"
    return render_template('email.html', error_message=error_message) 


if __name__ == '__main__':
    app.run(debug=True)