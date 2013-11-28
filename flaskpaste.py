from flask import Flask, render_template, request, redirect
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
mongo = PyMongo(app)

@app.route('/store_paste', methods=['POST'])
def store_paste():
    id = get_next_paste_id()
    store = {'_id': id,
             'code': '\n'+request.form['code'],
             'language': request.form['language']}
    mongo.db.pastes.insert(store)
    return redirect('/get_paste/%d' % id)


def get_next_paste_id():
    cursor = mongo.db.pastes.find({}, {'_id'}).sort('_id', -1).limit(1)
    try:
        return cursor[0]['_id']+1
    except IndexError:
            return 0


@app.route('/get_paste/<int:pasteid>')
def get_paste(pasteid=0):
    paste = mongo.db.pastes.find_one_or_404({'_id': pasteid})
    return render_template('show_code.html', paste=paste)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7800)
