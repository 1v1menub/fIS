from cfinal import *
import sys

@app.route('/')
def home():
    return '<div><a href="/addsubscriber"><button> register subscriber </button></a><a href="/addpublisher"><button> register publisher </button></a></div>'

@app.route("/addsubscriber")
def adduser():
    return render_template("subscriber.html")

@app.route("/addpublisher")
def validateuser():
    return render_template("publisher.html")

@app.route("/subadd", methods=['POST'])
def subadd():
    username = request.form["username"]
    password = request.form["password"]
    entry = client(username, password, False)
    db.session.add(entry)
    db.session.commit()

    return render_template("read.html")

@app.route("/pubadd", methods=['POST'])
def pubadd():
    username = request.form["username"]
    password = request.form["password"]
    entry = client(username, password, True)
    db.session.add(entry)
    db.session.commit()

    return render_template("publish.html")

@app.route("/messageadd", methods=['POST'])
def messageadd():
    topic = request.form["topic"]
    text = request.form["text"]
    entry = message(topic, text)
    db.session.add(entry)
    db.session.commit()

    return render_template("publish.html")


@app.route("/searchtopic", methods=['GET'])
def searchtopic():
    topic = request.args.get('topic')
    print(topic, file=sys.stderr)
    showmessage = None
    result = []
    for result in db.engine.execute("SELECT * FROM message WHERE topic="+"'"+topic+"'"):
        print(result, file=sys.stderr)
        print(result[1], file=sys.stderr)
    if(len(result) >= 1):
        showmessage = 'Messages found'
    else:
        showmessage = 'No messages for that topic'
    return render_template("read.html", showmessage=showmessage)


if __name__ == '__main__':
    app.run(debug=True)
