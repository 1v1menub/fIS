from clogin import *
import sys

@app.route('/')
def home():
    return '<div><a href="/adduser"><button> add user </button></a><a href="/validateuser"><button> validate user </button></a></div>'

@app.route("/adduser")
def adduser():
    return render_template("index.html")

@app.route("/validateuser")
def validateuser():
    return render_template("validate.html")

@app.route("/useradd", methods=['POST'])
def useradd():
    username = request.form["username"]
    password = request.form["password"]
    entry = usuario(username, password)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")

@app.route("/userval", methods=['POST'])
def userval():
    username = request.form['username']
    print(username, file=sys.stderr)
    password = request.form['password']
    print(password, file=sys.stderr)
    message = None
    result = []
    for result in db.engine.execute("SELECT * FROM usuario WHERE username="+"'"+username+"'"):
        print(result, file=sys.stderr)
        print(result[1], file=sys.stderr)
        if(result[1] == password):
            message = 'Valid user'
            print(message, file=sys.stderr)
        else:
            message = 'Invalid user'
            print(message, file=sys.stderr)
    if(len(result) == 0):
        message = 'Invalid user'
    return render_template("validate.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
