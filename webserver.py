from flask import Flask, request
from resouces import Entry
from entrymanager import EntryManager

app = Flask(__name__)
FOLDER = '/Users/waldemarquast/Desktop/test'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/entries/")
def get_entries():
    entrys = EntryManager(FOLDER)
    entrys.load()
    result = []
    for i in entrys.entries:
        result.append(i.json())
    return result


@app.route('/api/save_entries/', methods=['POST'])
def save_entries():
    ret_request = request.get_json()
    entry_manager = EntryManager(FOLDER)
    for item in ret_request:
        liste = Entry.from_json(item)
        entry_manager.entries.append(liste)
    entry_manager.save()
    return {'status': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)


