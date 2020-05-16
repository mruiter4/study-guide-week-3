from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

@app.route('/save-name')
def save_users_name():
    """get user name from for and save in session"""
    user_name = request.args.get("name")
    session['name'] = user_name

    return redirect('/form')

@app.route('/form')
def show_form():
    """show the html form"""

    return render_template('form.html')

@app.route('/results')
def show_results():
    """show results"""
    messages = {'cheery':'This is a cheery message :)',
                'dreary': 'This is a dreary message :(',
                'honest': 'This is an honest message :|'}

    message_choice = request.args.get("message_type")

    if message_choice in messages:
        message = messages[message_choice]
    else:
        message=""

    return render_template('results.html',
                            message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
