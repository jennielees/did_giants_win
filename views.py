import os

from flask import Flask, render_template

from baseball import did_giants_win

app = Flask(__name__)
app.secret_key = "asdfasdfasdfGIANTSasdf"

@app.route('/')
def index():
    print "I wanted the index"

    did_they_win = did_giants_win()

    return render_template('giants.html',
        did_they_win=did_they_win)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',debug=True,port=port)
