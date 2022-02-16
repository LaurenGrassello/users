from flask import Flask, redirect, render_template, request
# import the class from friend.py
from user import Users


app = Flask(__name__)



@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = Users.get_all()
    print(users)
    return render_template("index.html", all_users = Users.get_all())


@app.route('/create_user')
def create_user():
    # Users.update(request.form)
    return render_template('create.html')


@app.route('/user_complete', methods=['Post'])
def user_saved():
    Users.create_user(request.form)
    return redirect ('/')


if __name__ == "__main__":
    app.run(debug=True)